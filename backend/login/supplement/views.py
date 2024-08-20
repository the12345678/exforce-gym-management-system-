from django.shortcuts import render

from login.database.database_utils import create_database_connection, create_cursor

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def send_supplement_data(request):
    # Connect to the database
    cnx = create_database_connection()
    cursor = create_cursor(cnx)

    # Execute a query to fetch the supplement data (name, unit price, quantity per unit, stock)
    query = "SELECT `supplement name`, `unit_price_Rs`, `quantity_perunit`, `stock`,`valid_booking_period` FROM supplement_details"
    cursor.execute(query)

    # Fetch all the supplement data from the result
    all_supplement_data = cursor.fetchall()

    # Close the cursor and the database connection
    cursor.close()
    cnx.close()

    # Divide the data into two sets of four rows each
    first_object_data = all_supplement_data[:4]
    second_object_data = all_supplement_data[4:8]

    # Create objects for the two sets of data
    first_object = [{'name': row[0], 'unit_price_Rs': row[1], 'quantity_perunit': row[2], 'stock': row[3],'valid_booking_period':row[4]} for row in first_object_data]
    second_object =[{'name': row[0], 'unit_price_Rs': row[1], 'quantity_perunit': row[2], 'stock': row[3],'valid_booking_period':row[4]} for row in second_object_data]
   
    # Return the objects as JSON responses with different URLs
    response_data = {
        'first_object': first_object,
        'second_object': second_object
    }

    return JsonResponse(response_data, safe=False)


@csrf_exempt
def save_gym_supplement_data(request):
    if request.method == "POST":
        try:
            # Get the form data from the request body
            form_data = json.loads(request.body)

            if isinstance(form_data, list):
                # Connect to the MySQL database
                cnx = create_database_connection()
                cursor = create_cursor(cnx)
                # Create a table if it doesn't exist
               
                   
                

                # Insert the form data into the table
                insert_query = '''
                    INSERT INTO supplement_details ( `supplement name`, unit_price_RS,quantity_perunit, stock,brand,valid_booking_period)
                    VALUES (%s, %s, %s, %s, %s,%s)
                '''

                for item in form_data:
                  
                    supplement_name = item.get('supplement_name')
                    unit_price = item.get('Unit_price')
                    quantity=item.get("amount")
                    stock_amount= item.get('stock')
                    brand_name = item.get('Brand')
                    period= item.get('period')

                    # Execute the insert query for each form entry
                    cursor.execute(insert_query, (supplement_name,unit_price,quantity,stock_amount,brand_name,period))

                # Commit the changes
                cnx.commit()

                # Close the cursor and connection
                cursor.close()
                cnx.close()

                return JsonResponse({"message": "Form submitted successfully."})
            else:
                return JsonResponse({"message": "Invalid form data format. Expected a list."}, status=400)
        except Exception as e:
            print("error:",e)
            return JsonResponse({"message": "Failed to save the form data.", "error": str(e)}, status=500)
    else:
        return JsonResponse({"message": "Invalid request method."}, status=400)

# Create your models here.

# Create your views here.
   
@csrf_exempt
def update_gym_supplement_data(request):
    if request.method == "POST":
        try:
            # Get the form data from the request body
            form_data = json.loads(request.body)

            if isinstance(form_data, list):
                # Connect to the MySQL database
                cnx = create_database_connection()
                cursor = create_cursor(cnx)
                # Create a table if it doesn't exist
               
                   
                

                # Insert the form data into the table
                insert_query = '''
                   UPDATE supplement_details
                   SET stock = %s
                   WHERE TRIM(`supplement name`) = %s
                   AND TRIM(brand) = %s;

                '''

                for item in form_data:
                  
                    supplement_name = item.get('supplement_name')
                    brand = item.get('Brand')
                 
                    stock_amount= int(item.get('stock'))
                    print(supplement_name)
                    print(brand)
                    print(stock_amount)
                   
                    # Execute the insert query for each form entry
                    cursor.execute(insert_query, (stock_amount,supplement_name,brand))

                # Commit the changes
                cnx.commit()

                # Close the cursor and connection
                cursor.close()
                cnx.close()

                return JsonResponse({"message": "Form submitted successfully."})
            else:
                return JsonResponse({"message": "Invalid form data format. Expected a list."}, status=400)
        except Exception as e:
            print("error:",e)
            return JsonResponse({"message": "Failed to save the form data.", "error": str(e)}, status=500)
    else:
        return JsonResponse({"message": "Invalid request method."}, status=400)

# Create your models here.

# Create your views here.
