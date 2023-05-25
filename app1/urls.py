from django.urls import path

from app1 import views

urlpatterns = [
    path('',views.home,name='home'),
    path('log',views.log,name='log'),
    path('sign',views.sign,name='sign'),
    path('customer_register',views.customer_register,name='customer_register'),


    ############################## ADMIN SECTION ##############################
    path('admin_home',views.admin_home,name='admin_home'),
    path('instructor_register',views.instructor_register,name='instructor_register'),
    path('physician_register', views.physician_register, name='physician_register'),
    path('view_instructor', views.view_instructor, name='view_instructor'),
    path('accept_instructor/<int:id>/', views.accept_instructor, name='accept_instructor'),
    path('view_customer', views.view_customer, name='view_customer'),
    path('view_physician', views.view_physician, name='view_physician'),
    path('update_customer/<int:id>/', views.update_customer, name='update_customer'),
    path('delete_customer/<int:id>/', views.delete_customer, name='delete_customer'),
    path('update_instructor/<int:id>/', views.update_instructor, name='update_instructor'),
    path('delete_instructor/<int:id>/', views.delete_instructor, name='delete_instructor'),
    path('update_physician/<int:id>/', views.update_physician, name='update_physician'),
    path('delete_physician/<int:id>/', views.delete_physician, name='delete_physician'),
    path('accepted_instructors',views.accepted_instructors,name='accepted_instructors'),


    ####################################################################################

    path('batch_register',views.batch_register,name='batch_register'),
    path('view_batch',views.view_batch,name='view_batch'),
    path('update_batch/<int:id>/',views.update_batch,name='update_batch'),
    path('delete_batch/<int:id>/',views.delete_batch,name='delete_batch'),
    path('add_equipment',views.add_equipment,name='add_equipment'),
    path('view_equipment',views.view_equipment,name='view_equipment'),
    path('update_equipment/<int:id>/',views.update_equipment,name='update_equipment'),
    path('delete_equipment/<int:id>/',views.delete_equipment,name='delete_equipment'),

    ################################################################################

    path('customer_panel',views.customer_panel,name='customer_panel'),
    path('customerview_equipment',views.customerview_equipment,name='customerview_equipment'),
    path('customerbatch_details',views.customerbatch_details,name='customerbatch_details'),
    path('complaint_register',views.complaint_register,name='complaint_register'),
    path('view_complaint',views.view_complaint,name='view_complaint'),
    path('delete_complaint/<int:id>/',views.delete_complaint,name='delete_complaint'),
    path('admin_viewcomplaint',views.admin_viewcomplaint,name='admin_viewcomplaint'),
    path('register_service',views.register_service,name='register_service'),
    path('view_service',views.view_service,name='view_service'),
    path('customerview_service',views.customerview_service,name='customerview_service'),
    path('update_service/<int:id>/',views.update_service,name='update_service'),
    path('delete_service/<int:id>/',views.delete_service,name='delete_service'),
    path('complaint_reply/<int:id>/',views.complaint_reply,name='complaint_reply'),
    path('replysee',views.replysee,name='replysee'),

    ############################### ATTENDANCE ##################################

    path('attendance_register',views.attendance_register,name='attendance_register'),
    path('viewcustomer_attendance',views.viewcustomer_attendance,name='viewcustomer_attendance'),
    path('view_attendance',views.view_attendance,name='view_attendance'),
    path('delete_attendance/<int:id>/',views.delete_attendance,name='delete_attendance'),
    path('update_attendance/<int:id>/',views.update_attendance,name='update_attendance'),


    ########################## instructor panel #################################

    path('instructor_panel',views.instructor_panel,name='instructor_panel'),

    ############################## physician panel ##############################

    path('physician_panel',views.physician_panel,name='physician_panel'),
    path('customer_log',views.customer_log,name='customer_log'),

    ########################### payments #########################################

    path('register_payment',views.register_payment,name='register_payment'),
    path('view_payment',views.view_payment,name='view_payment'),
    path('delete_payment/<int:id>/',views.delete_payment,name='delete_payment'),
    path('pay_bill/<int:id>/',views.pay_bill,name='pay_bill'),
    path('bill_history',views.bill_history,name='bill_history'),
    path('pay_in_direct/<int:id>/',views.pay_in_direct,name='pay_in_direct'),
    path('view_invoice/<int:id>/',views.view_invoice,name='view_invoice'),
    path('get_invoice/<int:id>/',views.get_invoice,name='get_invoice')


]