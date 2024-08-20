from login.database.database_utils import create_database_connection, create_cursor

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def save_coach_payment_data(request):
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
                    INSERT INTO coach_payment (coach_name, salary,month,year)
                    VALUES (%s, %s, %s,%s)

                '''

                for item in form_data:
                    Coachname = item.get('coachname')
                    salary = item.get('salary')
                    month  = item.get('month')
                    year   = item.get('year')
                    print(Coachname)
                    
                    # Execute the insert query for each form entry
                    cursor.execute(insert_query,(Coachname, salary,month,year))
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

