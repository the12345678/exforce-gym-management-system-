
import base64
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
from django.http import HttpResponse
from login.database.database_utils import create_database_connection, create_cursor
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def generate_member_attendance_report(request):
    if request.method == "POST":
        try:
            # Fetch the attendance data from the XAMPP database
            cnx = create_database_connection()
            cursor = create_cursor(cnx)
            select_query = '''
                SELECT ID, date, entrance_time, `Member name`
                FROM member_attendance
            '''
            cursor.execute(select_query)
            attendance_data = cursor.fetchall()

            # Create a PDF document
            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer, pagesize=letter)
            elements = []

            # Add the image
            image_path = 'E:/backend/login/reports/images.jpg'  # Replace with the actual image file path
            image = Image(image_path, width=200, height=100)
            elements.append(image)

            # Add the topic above the table
            styles = getSampleStyleSheet()
            elements.append(Paragraph("Member Attendance Report", styles['Title']))

            # Prepare the data for the table
            table_data = [["ID", "Date", "Entrance Time", "Member Name"]]
            for item in attendance_data:
                table_data.append(list(item))

            # Create the table
            table = Table(table_data)

            # Set table style
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))

            # Add the table to the elements list
            elements.append(table)

            # Build the PDF content
            doc.build(elements)

            buffer.seek(0)

            # Convert the PDF to a Base64-encoded string
            pdf_content = base64.b64encode(buffer.getvalue()).decode('utf-8')

            buffer.seek(0)
            buffer.close()

            # Create the response with the PDF content
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="attendance_report.pdf"'

            # Set the PDF content in the response
            response.write(base64.b64decode(pdf_content))

            # Close the cursor and connection
            cursor.close()
            cnx.close()

            return response
        except Exception as e:
            print("error:", e)
            return HttpResponse("Failed to generate the attendance report.", status=500)
    else:
        return HttpResponse("Invalid request method.", status=400)

@csrf_exempt
def generate_coach_attendance_report(request):
    if request.method == "POST":
        try:
            # Fetch the attendance data from the XAMPP database
            cnx = create_database_connection()
            cursor = create_cursor(cnx)
            select_query = '''
                SELECT  `Coach name`,date
                FROM coach_attendance
            '''
            cursor.execute(select_query)
            attendance_data = cursor.fetchall()

            # Create a PDF document
            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer, pagesize=letter)
            elements = []

            # Add the image
            image_path = 'E:/backend/login/reports/images.jpg'  # Replace with the actual image file path
            image = Image(image_path, width=200, height=100)
            elements.append(image)

            # Add the topic above the table
            styles = getSampleStyleSheet()
            elements.append(Paragraph("Coach Attendance Report", styles['Title']))

            # Prepare the data for the table
            table_data = [["Coach Name","Date"]]
            for item in attendance_data:
                table_data.append(list(item))

            # Create the table
            table = Table(table_data)

            # Set table style
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))

            # Add the table to the elements list
            elements.append(table)

            # Build the PDF content
            doc.build(elements)

            buffer.seek(0)

            # Convert the PDF to a Base64-encoded string
            pdf_content = base64.b64encode(buffer.getvalue()).decode('utf-8')

            buffer.seek(0)
            buffer.close()

            # Create the response with the PDF content
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="attendance_report.pdf"'

            # Set the PDF content in the response
            response.write(base64.b64decode(pdf_content))

            # Close the cursor and connection
            cursor.close()
            cnx.close()

            return response
        except Exception as e:
            print("error:", e)
            return HttpResponse("Failed to generate the attendance report.", status=500)
    else:
        return HttpResponse("Invalid request method.", status=400)
