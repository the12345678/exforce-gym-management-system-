from login.database.database_utils import create_database_connection, create_cursor

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def save_administrator_data(request):
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
                    INSERT INTO administrator (admin_id,password, `admin name`, address, `email address`, `phone number`)
                    VALUES (%s, %s, %s, %s, %s,%s)
                '''

                for item in form_data:
                    admin_id = item.get('userID')
                    admin_password=item.get("password")
                    admin_name = item.get('username')
                    address = item.get('address')
                    email = item.get('email')
                    phone_num = item.get('phone_no')

                    # Execute the insert query for each form entry
                    cursor.execute(insert_query, (admin_id,admin_password, admin_name, address, email, phone_num))

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



@csrf_exempt
def delete_admin_registration_data(request, admin_id):
    if request.method == "POST":
        try:
            # Connect to the MySQL database
            cnx = create_database_connection()
            cursor = create_cursor(cnx)

            # Delete the row with the given member_id from the table
            delete_query = '''
                DELETE FROM administrator  WHERE admin_id = %s
            '''
            cursor.execute(delete_query, (admin_id,))

            # Commit the changes
            cnx.commit()

            # Close the cursor and connection
            cursor.close()
            cnx.close()

            return JsonResponse({"message": "Row deleted successfully."})
        except Exception as e:
            print("Error:", e)
            return JsonResponse({"message": "Failed to delete the row.", "error": str(e)}, status=500)
    else:
        return JsonResponse({"message": "Invalid request method."}, status=400)
