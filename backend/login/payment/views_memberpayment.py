from login.database.database_utils import create_database_connection, create_cursor

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def calculate_fee(request):
    if request.method == "POST":
        try:
            # Get the form data from the request body
            form_data = json.loads(request.body)
            user_name = form_data.get('user_name')

            # Your existing code to calculate the fee based on user_name
            cnx = create_database_connection()
            cursor = create_cursor(cnx)

            try:
                query = "SELECT experience_years FROM gym_members WHERE member_name = %s"
                cursor.execute(query, (user_name,))
                result = cursor.fetchone()

                if result:
                    work_experience = result[0]

                    if work_experience > 2:
                        fee = 10000.00
                    else:
                        fee = 15000.00

                    # Fetch all the remaining rows (if any) to avoid "Unread result found" issue
                    cursor.fetchall()

                    return JsonResponse({'fee': fee})  # Return fee as JSON response
                else:
                    raise ValueError("member name not found.")
            finally:
                cursor.close()
                cnx.close()

        except Exception as e:
            print("Error:", e)
            return JsonResponse({"message": "Error calculating fee.", "error": str(e)}, status=500)

    else:
        return JsonResponse({"message": "Invalid request method."}, status=400)
@csrf_exempt
def save_member_payment_data(request):
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
                    INSERT INTO member_payment (member_name, payment_status,month,year)
                    VALUES (%s, %s, %s,%s)

                '''

                for item in form_data:
                    membername = item.get('membername')
                    payment_status = item.get('payment_status')                    
                    month  = item.get('month')
                    year   = item.get('year')
                   
                    print(membername)
                    
                    # Execute the insert query for each form entry
                    cursor.execute(insert_query,(membername, payment_status,month,year))
                    
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


