from django.core.management.base import BaseCommand
import sys
import glob
import csv
import logging
import datetime
from django.db.models import Avg, Sum
from weather_app.models import *
from django.db.models.functions import Substr

path_log_file = "answers/debug.log"
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[logging.FileHandler(path_log_file), logging.StreamHandler(sys.stdout)])
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Helps for Data Ingestion'

    def get_weather_data(self):
        '''
        @param: 
        @feature: It is used for importing & saving input data : wx_data into our sqlite db.
        @return: None
        '''
        path = 'wx_data'
        start_time = datetime.datetime.now()

        logger.info("Initiating Weather Data Ingestion process.")
        try:
            file_list = glob.glob(path + "/*.txt")
            weather = [Weather(
                date=str(row[0]),
                max_temp=int(row[1]),
                min_temp=int(row[2]),
                precipitation=int(row[3]),
                station_name=file_list[i][-15:-4])
                for i in range(len(file_list))
                for row in csv.reader(open(file_list[i], "r", encoding="utf8"), delimiter="\t")]
            Weather.objects.bulk_create(weather, 5000, ignore_conflicts=True)
            end_time = datetime.datetime.now()
            logger.info("Weather Data Ingestion process completed successfully")
            logger.info(
                f"Time taken: {(end_time-start_time).total_seconds()}\t Number of records inserted: {len(weather)}")
        except Exception as err:
            logger.error(f"{err}")

    def get_statistics_data(self):
        '''
        @param: 
        @feature: It is used getting statistics data.
        @return: None
        '''
        try:
            result = Weather.objects.filter(
                max_temp__gt=-9999,
                min_temp__gt=-9999,
                precipitation__gt=-9999
            ).values(
                'station_name',
                year=Substr('date', 1, 4),
            ).annotate(
                max_temp_avg=Avg('max_temp'),
                min_temp_avg=Avg('min_temp'),
                ppt_sum=Sum('precipitation')
            )

            statistics = [Statistics(
                station_name=res['station_name'],
                date=res['year'],
                avg_max_temp=res['max_temp_avg'],
                avg_min_temp=res['min_temp_avg'],
                total_acc_ppt=res['ppt_sum']
            ) for res in result]
            Statistics.objects.bulk_create(statistics, 5000, ignore_conflicts=True)
            logger.info("Executed Succesfully")
        except Exception as err:
            logger.error(f"{err}")

    def handle(self, *args, **kwargs):
        self.get_weather_data()
        self.get_statistics_data()
