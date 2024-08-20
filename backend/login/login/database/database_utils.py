import mysql.connector
from django.conf import settings

def create_database_connection():
    # Connect to the MySQL database using Django's settings
    cnx = mysql.connector.connect(
        host=settings.DATABASES['default']['HOST'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        database=settings.DATABASES['default']['NAME']
    )

    return cnx

def create_cursor(connection):
    # Create a cursor object to execute queries
    return connection.cursor()
