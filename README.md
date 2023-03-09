# Code Challenge Template

## Language Utilized for this challenge:
- Python
  
## Python Frameworks Utilized for this challenge:
- Framework: Django
- Framework: DRF - Django Rest Framework

## Input Data received for this challenge:
- Weather data identified by : wx_data.
- Yield data identified by : yld_data.
  
## Database Utilized for this challenge:
- SQLite

## Data folder caution:
- Please add folders - wx_data and yld_data data folder to this code as code file are large enough to be pushed to github.

## Code Structure of Code Challenge:
- wx_data  : Provides Weather data as input.
- yld_data : Provides Yield data as input.
- src : Provides codebase for django app and other custom app. 
- answers : Provides information about log generated during usage of application under debug.log

## Steps to execute the codebase:
- Firstly create and run the virtual environment using cmd: 
```bash
  pip install virtualenv
  virtualenv env
```

- To activate our virtual environment :
```bash
  env/Scripts/activate (in Windows)
  source env/bin/activate (in Linux and Mac)
```

- Install every requirements using cmd
```bash
  pip install -r requirements.txt
```

- Navigate to “src” directory under it using cmd: `cd src` in our terminal
- Now we need to migrate the db models:
```bash
  cd src
  python manage.py makemigrations weather_app
  python manage.py migrate weather_app
```

- Then we need to start ingesting our input data provided:
```bash
  python manage.py ingest
```

- Ultimately run the python server using cmd: <br>
```bash
  python manage.py runserver
```

- Rest of our functionalities can be easily accessed through the API links:
  http://127.0.0.1:8000/api/swagger/
  http://127.0.0.1:8000/api/weather/
  http://127.0.0.1:8000/api/weather/stats/

- Using query parameters it can be accessed such as:
  http://127.0.0.1:8000/api/weather/?date=20100101

## Tests
```bash
  cd src
  python manage.py test
```

# AWS Deployment

## Deploy Django API:
- Leverage AWS Elastic Beanstalk to streamline the deployment and operation of a web application, supporting various programming languages such as Python, the foundation of Django.
- Establish a load balancer to manage incoming traffic and allocate it to numerous instances of the Django application.

## Deploy database:
- Host a PostgreSQL database using Amazon Relational Database Service (RDS), which is a fully managed and secure database solution that can be scaled as needed.
- Configure secure access to the RDS instance from Django for the database.

## Data Storage:
- Use AWS EFS or S3 buckets to store text files.

## Scheduling data ingestion process:
- One approach to implement the data ingestion pipeline could be to utilize AWS ECS FARGATE to schedule the data ingestion code and ECR to store the image. 
- Amazon CloudWatch Events can be used to define a rule that triggers Fargate tasks at specific intervals, and the ingested data can be stored in the RDS database.

## Conclusion
- This method provides a way to deploy your Django API, database, and data ingestion code that is scalable, secure, and easy to manage.
- The combination of AWS Elastic Beanstalk, Amazon RDS, ECS FARGATE, and Amazon CloudWatch Events enables you to handle changes in traffic levels and run your data ingestion code as needed, all without the need for infrastructure management.

## Screen Shots:

![Alt text](/weather.png?raw=true "weather")

![Alt text](/statistics.png?raw=true "statistics")

![Alt text](/swagger_api.png?raw=true "swagger_api")