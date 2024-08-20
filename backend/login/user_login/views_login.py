from django.shortcuts import render
from login.database.database_utils import create_database_connection, create_cursor

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_admin_password(request):
    try:
        cnx = create_database_connection()
        cursor = create_cursor(cnx)
        formdata=json.loads(request.body)

        # Query to fetch the password based on the userid
        select_query = '''
            SELECT password FROM administrator WHERE admin_id = %s
        '''
        for item in formdata:
          idValue=item.get("idValue")
          
        # Execute the query
          cursor.execute(select_query, (idValue,))
          print("yes2")
          result = cursor.fetchone()
          print("result:",result)
        # Close the cursor and connection
        cursor.close()
        cnx.close()

        if result:
          return JsonResponse({'password':result})
         # Return the password
        else:
            return None  # Return None if the userid doesn't exist in the table
    except Exception as e:
        print("Error:", e)
        return None
    

@csrf_exempt
def get_customer_password(request):
    try:
        cnx = create_database_connection()
        cursor = create_cursor(cnx)
        formdata=json.loads(request.body)

        # Query to fetch the password based on the userid
        select_query = '''
            SELECT CustomerPassword FROM customer WHERE CustomerID = %s
        '''
        for item in formdata:
          idValue=item.get("idValue")
          
        # Execute the query
          cursor.execute(select_query, (idValue,))
        
          result = cursor.fetchone()
          
        # Close the cursor and connection
        cursor.close()
        cnx.close()

        if result:
          return JsonResponse({'password':result})
         # Return the password
        else:
            return None  # Return None if the userid doesn't exist in the table
    except Exception as e:
        print("Error:", e)
        return None
    

    