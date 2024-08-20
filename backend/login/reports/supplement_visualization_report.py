from login.database.database_utils import create_database_connection, create_cursor
import plotly.graph_objects as go
import plotly.offline as opy
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def graph_view(request):
    
     cnx = create_database_connection()
     cursor = create_cursor(cnx)
                # Create a table if it doesn't exist
     query = "SELECT Supplement_id, SUM(`total_price(Rs.)`) AS total_price_sum FROM suppliment_book GROUP BY Supplement_id;"
     cursor.execute(query)
     data = cursor.fetchall() 
     # Commit the changes
     cnx.commit()

     # Close the cursor and connection
     cursor.close()
     cnx.close()
       

     supplement_ids = [item[0] for item in data]
     total_prices = [item[1] for item in data]

     graph_data = {
        'supplement_ids': supplement_ids,
        'total_prices': total_prices,
    }

     return JsonResponse(graph_data)

             
     # views.py

import json
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from django.http import HttpResponse, JsonResponse


# Rest of the code remains unchanged...

def generate_pdf_report(request):
    if request.method == "GET":
        try:
            # Connect to the MySQL database
            cnx = create_database_connection()
            cursor = cnx.cursor()

            # Query to join the SupplementDetail and SupplementBook tables
            query = '''
                SELECT sb.customer_id, sd.`supplement name`, sb.amount, sb.amount * sd.unit_price_Rs AS total_price
                FROM suppliment_book sb
                INNER JOIN supplement_details sd ON sb.supplement_id = sd.supplement_id
            '''

            # Execute the query and fetch data
            cursor.execute(query)
            data = cursor.fetchall()

            # Generate the PDF report
            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer, pagesize=letter)

            # Add an image above the report title
            image_path = 'E:/backend/login/reports/images.jpg'  # Replace with the actual image path
            image = Image(image_path, width=200, height=50)
            elements = [image]

            # Set report content
            title_style = "Helvetica-Bold"
            data_style = "Helvetica"
            title = "Supplement Sales Report"
            title_table = Table([[title]], colWidths=[500], rowHeights=[50])
            title_table.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                             ('FONT', (0, 0), (-1, -1), title_style)]))
            elements.append(title_table)

            table_data = [['Customer ID', 'Supplement Name', 'Amount', 'Total Price']]
            for item in data:
                customer_id = item[0]
                supplement_name = item[1]
                amount = item[2]
                total_price = item[3]
                table_data.append([customer_id, supplement_name, amount, total_price])

            table = Table(table_data, colWidths=[100, 200, 100, 100])
            table_style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), '#CCCCCC'),
                                      ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                      ('FONT', (0, 0), (-1, 0), title_style),
                                      ('FONT', (0, 1), (-1, -1), data_style),
                                      ('GRID', (0, 0), (-1, -1), 1, "#000000")])
            table.setStyle(table_style)
            elements.append(table)

            doc.build(elements)

            buffer.seek(0)

            # Prepare the PDF response
            response = HttpResponse(buffer.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="supplement_report.pdf"'

            # Close the cursor and connection
            cursor.close()
            cnx.close()

            return response
        except Exception as e:
            print("error", e)
            return JsonResponse({"message": "Failed to generate the supplement report.", "error": str(e)}, status=500)
    else:
        return JsonResponse({"message": "Invalid request method."}, status=400)
