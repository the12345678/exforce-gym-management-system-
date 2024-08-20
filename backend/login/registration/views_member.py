
from login.database.database_utils import create_database_connection, create_cursor

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def get_coach_names(request):
    # Connect to the database
    cnx = create_database_connection()
    cursor = create_cursor(cnx)

    # Execute a query to fetch the coach IDs
    query = "SELECT `coach name` FROM coach"
    cursor.execute(query)

    # Fetch all the coach IDs from the result
    coach_names = [row[0] for row in cursor.fetchall()]
    print("coach names: ",coach_names)

    # Close the cursor and the database connection
    cursor.close()
    cnx.close()

    # Return the coach IDs as a JSON response
    return JsonResponse(coach_names, safe=False)





@csrf_exempt
def save_member_registration_data(request):
    if request.method == "POST":
        try:
            # Get the form data from the request body
            form_data = json.loads(request.body)
            print(type(form_data))
            if isinstance(form_data, list):
                # Connect to the MySQL database
                cnx = create_database_connection()
                cursor = create_cursor(cnx)
                # Create a table if it doesn't exist
               
                   
                

                # Insert the form data into the table
                insert_query = '''
                    INSERT INTO test_gymmember(member_name, address1, address2,NIC, dob, gender, email, phone_num,coach_id,experience_years)
                    VALUES ( %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)
                '''

                for item in form_data:
                  
                    member_name = item.get('membername')
                    address1 = item.get('address1')
                    address2 = item.get('address2')
                    NIC=item.get("NIC")                 
                    dob = item.get('dob')
                    gender = item.get('gender')
                    email = item.get('email')
                    phone_num = item.get('phone_no')
                    coach_name=item.get('coachname')
                    experience= int(item.get('experience'))
                  

                    select_query = 'SELECT coach_id FROM coach WHERE `coach name` = %s'
                    cursor.execute(select_query, (coach_name,))
                  
        # Fetch the coach_id (assuming coach_name is unique)
                    coach_id_tuple = cursor.fetchone()
                    coach_id=coach_id_tuple[0]
                  
                   
                   
                    # Execute the insert query for each form entry
                try:
    # Pass the parameters as a tuple to the cursor.execute() method
                    cursor.execute(insert_query, (member_name, address1, address2,NIC,dob, gender, email, phone_num,coach_id,experience))
                   
                    print(member_name,address1,address2,NIC,dob,gender,email,phone_num,coach_id,experience)
    # If you are using a connection with autocommit disabled, remember to commit the transaction.
    # connection.commit()
    
                except Exception as e:
    # Log the error or print the exception for debugging
                    print("Error:", e)

                # Close the cursor and connection
                cnx.commit()
                print("ok")
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
    




