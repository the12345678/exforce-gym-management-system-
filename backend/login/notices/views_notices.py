from django.shortcuts import render
from login.database.database_utils import create_database_connection, create_cursor

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse

@csrf_exempt
def get_notice_data(request):
    # Connect to the database
    cnx = create_database_connection()
    cursor = create_cursor(cnx)

    # Execute a query to fetch the coach data (title and description)
    query = "SELECT `title`, `details` FROM notices"
    cursor.execute(query)

    # Fetch all the coach data from the result
    notice_data = [{'title': row[0], 'details': row[1]} for row in cursor.fetchall()]
    print("notice data: ", notice_data)

    # Close the cursor and the database connection
    cursor.close()
    cnx.close()

    # Return the coach data as a JSON response
    return JsonResponse(notice_data, safe=False)

@csrf_exempt
def save_noticeinput_data(request):
    if request.method == "POST":
        try:
            # Get the form data from the request body
            form_data = json.loads(request.body)

            if isinstance(form_data, list):
                # Connect to the MySQL database
                cnx = create_database_connection()
                cursor = create_cursor(cnx)
                # Create a table if it doesn't exist
                 # Fetch the number of rows from the 'notices' table
                cursor.execute("SELECT COUNT(*) FROM notices")
                num_rows = cursor.fetchone()[0]
                
                if num_rows == 3:
                    # Delete all rows from the 'notices' table
                    delete_query = "DELETE FROM notices"
                    id_change_query="ALTER TABLE notices AUTO_INCREMENT = 1;"
                    cursor.execute(delete_query)
                    cursor.execute(id_change_query)
                # Insert the form data into the table
                insert_query = '''
                    INSERT INTO notices (title,details)
                    VALUES (%s, %s)

                '''

                for item in form_data:
                    
                    notice_title = item.get('notice_title')                    
                    description  = item.get('description')
                  
                    # Execute the insert query for each form entry
                    cursor.execute(insert_query,( notice_title,description))
                    
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


@csrf_exempt
def update_notice_data(request):
    try:
        # Get the form data from the request body
        form_data = json.loads(request.body)

       
        # Connect to the MySQL database
        cnx = create_database_connection()
        cursor = create_cursor(cnx)

        # Generate the update query based on the provided data
        update_query = 'UPDATE notices SET details = %s WHERE ID =%s'

        for item in form_data: 

            # Extract relevant fields
            notice_id = item.get('notice_id')                
            description= item.get('description')
       
            cnx = create_database_connection()
            cursor = create_cursor(cnx)       
       

        # Execute the update query
        cursor.execute(update_query,(description,notice_id))

        # Commit the changes
        cnx.commit()

        # Close the cursor and connection
        cursor.close()
        cnx.close()

        return JsonResponse({"message": "Registration updated successfully."})
    except Exception as e:
        print("Error:", e)
        return JsonResponse({"message": "Failed to update registration.", "error": str(e)}, status=500)
# Create your views here.
