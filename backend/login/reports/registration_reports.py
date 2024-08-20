from login.database.database_utils import create_database_connection, create_cursor

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt


def fetch_data1(request):
    
    # Get the table name from the request parameter
    table_name = request.GET.get('table')

    # Connect to the MySQL database
    try:
        cnx = create_database_connection()
        cursor = create_cursor(cnx)

        # Fetch data from the specific table for the specified columns
        query = f"SELECT member_name, address1, email, phone_num FROM {table_name} ORDER BY member_id DESC LIMIT 7;"
        cursor.execute(query)
        data = [{'member_name': row[0], 'address1': row[1], 'email': row[2], 'phone_num': row[3]} for row in cursor.fetchall()]
        print(data)
        # Close the database connection
        cursor.close()
        cnx.close()

        return JsonResponse(data,safe=False)

    except ImportError as err:
        print(f"Error connecting to the database: {err}")
        return JsonResponse({'error': 'Error connecting to the database'})

    except Exception as e:
        print(f"Error fetching data: {e}")
        return JsonResponse({'error': 'Error fetching data'})
    


def fetch_data2(request):
    
    # Get the table name from the request parameter
    table_name = request.GET.get('table')

    # Connect to the MySQL database
    try:
        cnx = create_database_connection()
        cursor = create_cursor(cnx)

        # Fetch data from the specific table for the specified columns
        query = f"SELECT CustomerName, Address,EmailAddress,PhoneNumber FROM {table_name} ORDER BY CustomerID DESC LIMIT 7;"
        cursor.execute(query)
        data = [{'CustomerName': row[0], 'Address': row[1], 'EmailAddress': row[2], 'PhoneNumber': row[3]} for row in cursor.fetchall()]

        # Close the database connection
        cursor.close()
        cnx.close()

        return JsonResponse(data,safe =False)

    except ImportError as err:
        print(f"Error connecting to the database: {err}")
        return JsonResponse({'error': 'Error connecting to the database'})

    except Exception as e:
        print(f"Error fetching data: {e}")
        return JsonResponse({'error': 'Error fetching data'})
    

    
