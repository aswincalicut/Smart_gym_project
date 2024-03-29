from django.urls import path

from app1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('log', views.log, name='log'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('sign', views.sign, name='sign'),
    path('customer_register', views.customer_register, name='customer_register'),

    ############################## ADMIN SECTION ##############################
    path('admin_home', views.admin_home, name='admin_home'),
    path('instructor_register', views.instructor_register, name='instructor_register'),
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
    path('accepted_instructors', views.accepted_instructors, name='accepted_instructors'),

    ####################################################################################

    path('batch_register', views.batch_register, name='batch_register'),
    path('view_batch', views.view_batch, name='view_batch'),
    path('update_batch/<int:id>/', views.update_batch, name='update_batch'),
    path('delete_batch/<int:id>/', views.delete_batch, name='delete_batch'),
    path('add_equipment', views.add_equipment, name='add_equipment'),
    path('view_equipment', views.view_equipment, name='view_equipment'),
    path('update_equipment/<int:id>/', views.update_equipment, name='update_equipment'),
    path('delete_equipment/<int:id>/', views.delete_equipment, name='delete_equipment'),

    ################################################################################

    path('customer_panel', views.customer_panel, name='customer_panel'),
    path('customerview_equipment', views.customerview_equipment, name='customerview_equipment'),
    path('customerbatch_details', views.customerbatch_details, name='customerbatch_details'),
    path('complaint_register', views.complaint_register, name='complaint_register'),
    path('view_complaint', views.view_complaint, name='view_complaint'),
    path('delete_complaint/<int:id>/', views.delete_complaint, name='delete_complaint'),
    path('admin_viewcomplaint', views.admin_viewcomplaint, name='admin_viewcomplaint'),
    path('status_reply/<int:id>/', views.status_reply, name='status_reply'),
    path('register_service', views.register_service, name='register_service'),
    path('view_service', views.view_service, name='view_service'),
    path('customerview_service', views.customerview_service, name='customerview_service'),
    path('update_service/<int:id>/', views.update_service, name='update_service'),
    path('delete_service/<int:id>/', views.delete_service, name='delete_service'),
    path('complaint_reply/<int:id>/', views.complaint_reply, name='complaint_reply'),
    path('replysee', views.replysee, name='replysee'),
    path('customerview_reply', views.customerview_reply, name='customerview_reply'),

    ############################### ATTENDANCE ##################################

    path('attendance_register', views.attendance_register, name='attendance_register'),
    path('viewcustomer_attendance', views.viewcustomer_attendance, name='viewcustomer_attendance'),
    path('viewinstructor_attendance', views.viewinstructor_attendance, name='viewinstructor_attendance'),
    path('view_attendance', views.view_attendance, name='view_attendance'),
    path('delete_attendance/<int:id>/', views.delete_attendance, name='delete_attendance'),
    path('update_attendance/<int:id>/', views.update_attendance, name='update_attendance'),

    ########################## instructor panel #################################

    path('instructor_panel', views.instructor_panel, name='instructor_panel'),
    path('batch_details', views.batch_details, name='batch_details'),
    # path('viewattendance',views.viewattendance,name='viewattendance'),
    path('add_attendance', views.add_attendance, name='add_attendance'),
    path('update_instructor_attendance/<int:id>/', views.update_instructor_attendance,
         name='update_instructor_attendance'),
    path('delete_instructor_attendance/<int:id>/', views.delete_instructor_attendance,
         name='delete_instructor_attendance'),
    path('checkout_customers', views.checkout_customers, name='checkout_customers'),
    # path('instructor_viewCustomer',views.instructor_viewCustomer,name='instructor_viewCustomer'),

    ############################## physician panel ##############################

    path('physician_panel', views.physician_panel, name='physician_panel'),
    path('customer_log', views.customer_log, name='customer_log'),

    ############################# testing appointment ######################
    path('schedule_customer', views.schedule_customer, name='schedule_customer'),
    path('view_allschedule', views.view_allschedule, name='view_allschedule'),
    path('update_allschedule/<int:id>/', views.update_allschedule, name='update_allschedule'),
    path('delete_allschedule/<int:id>/', views.delete_allschedule, name='delete_allschedule'),
    path('customer_view_schedule', views.customer_view_schedule, name='customer_view_schedule'),
    path('view_physician_schedules', views.view_physician_schedules, name='view_physician_schedules'),
    path('take_appointment/<int:id>/', views.take_appointment, name='take_appointment'),

    path('approve_reject_appointment', views.approve_reject_appointment, name='approve_reject_appointment'),
    path('accept_appointment/<int:id>/', views.accept_appointment, name='accept_appointment'),
    path('reject_appointment/<int:id>/', views.reject_appointment, name='reject_appointment'),
    path('view_approved', views.view_approved, name='view_approved'),

    ########################### payments #########################################

    path('register_payment', views.register_payment, name='register_payment'),
    path('view_payment', views.view_payment, name='view_payment'),
    path('delete_payment/<int:id>/', views.delete_payment, name='delete_payment'),
    path('pay_bill/<int:id>/', views.pay_bill, name='pay_bill'),
    path('bill_history', views.bill_history, name='bill_history'),
    path('admin_view_payment', views.admin_view_payment, name='admin_view_payment'),
    path('pay_in_direct/<int:id>/', views.pay_in_direct, name='pay_in_direct'),
    path('view_invoice/<int:id>/', views.view_invoice, name='view_invoice'),
    path('get_invoice/<int:id>/', views.get_invoice, name='get_invoice'),
    path('add_firstaid', views.add_firstaid, name='add_firstaid'),
    path('view_firstaid', views.view_firstaid, name='view_firstaid'),
    path('customer_view_firstaid', views.customer_view_firstaid, name='customer_view_firstaid'),

    path('ask_medical_doubt', views.ask_medical_doubt, name='ask_medical_doubt'),
    path('customer_view_medical_doubt', views.customer_view_medical_doubt, name='customer_view_medical_doubt'),
    path('physician_view_doubt', views.physician_view_doubt, name='physician_view_doubt'),
    path('physician_reply_doubt/<int:id>/', views.physician_reply_doubt, name='physician_reply_doubt'),
    path('medical_doubt_reply/<int:id>/', views.medical_doubt_reply, name='medical_doubt_reply'),
    path('customer_view_doubt_reply', views.customer_view_doubt_reply, name='customer_view_doubt_reply'),
    path('medical_doubt_delete/<int:id>/', views.medical_doubt_delete, name='medical_doubt_delete')

]
