from login.database.database_utils import create_database_connection, create_cursor

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def fetch_data3(request):
    
    # Get the table name from the request parameter
    table_name = request.GET.get('table')

    # Connect to the MySQL database
    try:
        cnx = create_database_connection()
        cursor = create_cursor(cnx)

        # Fetch data from the specific table for the specified columns
        query = f"SELECT member_name, payment_status, month, year FROM {table_name} ORDER BY ID DESC LIMIT 5;"
        cursor.execute(query)
        data = [{'member_name': row[0], 'payment_status': row[1], 'month': row[2], 'year': row[3]} for row in cursor.fetchall()]
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
    

@csrf_exempt
def fetch_data4(request):
    
    # Get the table name from the request parameter
    table_name = request.GET.get('table')

    # Connect to the MySQL database
    try:
        cnx = create_database_connection()
        cursor = create_cursor(cnx)

        # Fetch data from the specific table for the specified columns
        query = f"SELECT coach_name,month,year FROM {table_name} ORDER BY ID DESC LIMIT 5;"
        cursor.execute(query)
        data = [{'coach_name': row[0], 'month': row[1], 'year': row[2]} for row in cursor.fetchall()]

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
    

    
