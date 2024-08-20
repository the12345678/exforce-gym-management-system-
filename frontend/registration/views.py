
from login.database.database_utils import create_database_connection, create_cursor

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def save_registration_data(request):
    if request.method == "POST":
        try:
            # Get the form data from the request body
            form_data = json.loads(request.body)

            if isinstance(form_data, list):
                # Connect to the MySQL database
                cnx = create_database_connection()
                cursor = create_cursor(cnx)
                # Create a table if it doesn't exist
                create_table_query = '''
                    CREATE TABLE IF NOT EXISTS registration (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        member_name VARCHAR(255),
                        address1 VARCHAR(255),
                        address2 VARCHAR(255),
                        dob DATE,
                        gender VARCHAR(10),
                        email VARCHAR(255),
                        phone_num VARCHAR(20)
                    )
                '''
                cursor.execute(create_table_query)

                # Insert the form data into the table
                insert_query = '''
                    INSERT INTO registration (member_name, address1, address2, dob, gender, email, phone_num)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                '''

                for item in form_data:
                    member_name = item.get('membername')
                    address1 = item.get('address1')
                    address2 = item.get('address2')
                    dob = item.get('dob')
                    gender = item.get('gender')
                    email = item.get('email')
                    phone_num = item.get('phone_no')

                    # Execute the insert query for each form entry
                    cursor.execute(insert_query, (member_name, address1, address2, dob, gender, email, phone_num))

                # Commit the changes
                cnx.commit()

                # Close the cursor and connection
                cursor.close()
                cnx.close()

                return JsonResponse({"message": "Form submitted successfully."})
            else:
                return JsonResponse({"message": "Invalid form data format. Expected a list."}, status=400)
        except Exception as e:
            return JsonResponse({"message": "Failed to save the form data.", "error": str(e)}, status=500)
    else:
        return JsonResponse({"message": "Invalid request method."}, status=400)
