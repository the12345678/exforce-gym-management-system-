from django.urls import path
from . import supplement_visualization_report,attendance_reports,registration_reports,payment_reports


app_name = 'reports'
urlpatterns = [
    path('visualization/data/', supplement_visualization_report.graph_view, name='graph_view'),
    path('supplement/data/', supplement_visualization_report.generate_pdf_report, name='generate_pdf_report'),    
    path('member/attendance/data/', attendance_reports.generate_member_attendance_report, name=' generate_member_attendance_report'),
    path('coach/attendance/data/', attendance_reports. generate_coach_attendance_report, name=' generate_coach_attendance_report'),
    path('member/registration/data/', registration_reports.fetch_data1, name='fetch_data1'),
    path('customer/registration/data/', registration_reports.fetch_data2, name='fetch_data2'),
    path('member/payment/data/', payment_reports.fetch_data3, name='fetch_data3'),
    path('coach/payment/data/', payment_reports.fetch_data4, name='fetch_data4'),
    
]