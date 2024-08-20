from django.shortcuts import render
from datetime import date
from login.database.database_utils import create_database_connection, create_cursor

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def save_change_table_data(request):
    if request.method == "POST":
        try:
            # Get the form data from the request body
            form_data = json.loads(request.body)

            if isinstance(form_data, list):
                # Connect to the MySQL database
                cnx = create_database_connection()
                cursor = create_cursor(cnx)
                # Create a table if it doesn't exist
                purchase_date = date.today()
                

                for item in form_data:
                  
                    customer_id = item.get("customer_id")   
                    amount = item.get('amount')
                    total_price = item.get('total_price')
                    id=item.get("num")
                    print("id",id)
                    # Insert the form data into the suppliment_book table
                    insert_query = '''
    INSERT INTO suppliment_book (`customer_id`,`supplement_id`, `amount`,`total_price(Rs.)`,`purchase_date`)
    VALUES (%s, %s, %s,%s,%s)
    ON DUPLICATE KEY UPDATE  `amount`=`amount`+ %s, supplement_id=%s,`total_price(Rs.)`=`total_price(Rs.)`+ %s,`purchase_date`=%s
'''

                    cursor.execute(insert_query, (customer_id,id,amount, total_price, purchase_date,amount,id,total_price,purchase_date))

                   
                    update_query1 = '''
                        UPDATE supplement_details
                        SET stock = stock - %s
                        WHERE supplement_id = %s
                    '''
                    cursor.execute(update_query1, (amount,id))
                    print("yes")
                # Commit the changes
                cnx.commit()

                # Close the cursor and connection
                cursor.close()
                cnx.close()

                return JsonResponse({"message": "Form submitted successfully."})
            else:
                return JsonResponse({"message": "Invalid form data format. Expected a list."}, status=400)
        except Exception as e:
            print("Error:", e)
            return JsonResponse({"message": "Failed to save the form data.", "error": str(e)}, status=500)
    else:
        return JsonResponse({"message": "Invalid request method."}, status=400)
