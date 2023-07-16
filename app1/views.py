from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from .utils import render_to_pdf


from app1.forms import customuserform, instructorform, physicianform, batchform, machineform, complaintsform, \
    serviceform, replyform, attendanceform, paybillform, billform, scheduleform
from app1.models import customuser, batch, equipments, complaints, servicemodel, attendancemodel, Bill, creditcard, \
    schedule, appointment


# Create your views here.
def home(request):
    return render(request,'index.html')


########################### ADMIN VIEWS ############################
def admin_home(request):
    if request.user.is_superuser:
        return render(request,'admintemp/dashmin.html')

####################### instructor section start #######################

def instructor_register(request):
    form = instructorform()
    if request.method == 'POST':
        form = instructorform(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_instructor=True
            user.save()
            messages.info(request,'instructor registered successfully')
            return redirect('view_instructor')
    return render(request,'admintemp/instructor_register.html',{'form':form})

def view_instructor(request):
    data = customuser.objects.filter(is_instructor=True)
    return render(request,'admintemp/instructor_view.html',{'data':data})

def accept_instructor(request,id):
    data=customuser.objects.get(id=id)
    data.status=1
    data.save()
    return redirect('view_instructor')

def accepted_instructors(request):
    accepted_users = customuser.objects.filter(status=1)
    context = {'data': accepted_users}
    return render(request, 'admintemp/accepted_instructors.html', context)

def update_instructor(request,id):
    data = customuser.objects.get(id=id)
    form = instructorform(instance=data)
    if request.method == 'POST':
        form = instructorform(request.POST or None,request.FILES or None,instance=data or None)
        if form.is_valid():
            form.save()
            return redirect('view_instructor')
    return render(request,'admintemp/instructor_update.html',{'form':form})


def delete_instructor(request,id):
    customuser.objects.get(id=id).delete()
    return redirect('accepted_instructors')

##################### instructor section end ############################


##################### customer section start ##################################

def customer_register(request):
    form = customuserform()
    if request.method == 'POST':
        form = customuserform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_customer=True
            user.save()
            messages.info(request,'customer  registered successfully')
            return redirect('view_customer')
    return render(request,'customer_register.html',{'form':form})


def view_customer(request):
    data = customuser.objects.filter(is_customer=True)
    return render(request,'admintemp/customer_view.html', {'data':data})

def update_customer(request,id):
    data = customuser.objects.get(id=id)
    form = customuserform(instance=data)
    if request.method == 'POST':
        form = customuserform(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_customer')
    return render(request,'admintemp/customer_update.html',{'form':form})

def delete_customer(request,id):
    customuser.objects.get(id=id).delete()
    return redirect('view_customer')

########################## customer section end ##########################

######################### physician section start ########################
def physician_register(request):
    form = physicianform()
    if request.method == 'POST':
        form = physicianform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_physician = True
            user.save()
            messages.info(request,'physician registered successfully')
            return redirect('view_physician')
    return render(request,'admintemp/physician_register.html',{'form':form})

def view_physician(request):
    data = customuser.objects.filter(is_physician=True)
    return render(request,'admintemp/physician_view.html',{'data':data})

def update_physician(request,id):
    data = customuser.objects.get(id=id)
    form = physicianform(instance=data)
    if request.method == 'POST':
        form = physicianform(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_physician')
    return render(request,'admintemp/physician_update.html', {'form':form})

def delete_physician(request,id):
    customuser.objects.get(id=id).delete()
    return redirect('view_physician')

######################## physician section end #######################

####################### log/sign section ###########################

def log(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect('admin_home')
            elif user.is_customer:
                return redirect('customer_panel')
            elif user.is_instructor:
                return redirect('instructor_panel')
            elif user.is_physician:
                return redirect('physician_panel')
        else:
            messages.info(request,'invalid credentials')
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('log')


def customer_log(request):
    return render(request,'customer/customer_log.html')

def sign(request):
    return render(request,'sign-up.html')

####################### log/sign section end ###########################

####################### batch section start ###########################
def batch_register(request):
    form = batchform()
    if request.method == 'POST':
        form = batchform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'batch registered successfully')
            return redirect('view_batch')
    return render(request,'batchinfo/batch_register.html',{'form':form})

def view_batch(request):
    data = batch.objects.filter()
    return render(request,'batchinfo/batch_view.html',{'data':data})

def update_batch(request,id):
    data = batch.objects.get(id=id)
    form = batchform(instance=data)
    if request.method=='POST':
        form = batchform(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_batch')
    return render(request,'batchinfo/update_batch.html',{'form':form})

def delete_batch(request,id):
    batch.objects.get(id=id).delete()
    return redirect('view_batch')

####################### batch section end ###########################

####################### equipment section start ###########################

def add_equipment(request):
    form = machineform()
    if request.method == 'POST':
        form = machineform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_equipment')
    return render(request,'equipments/add_equipment.html',{'form':form})

def view_equipment(request):
    data = equipments.objects.filter()
    return render(request,'equipments/view_equipment.html',{'data':data})

def update_equipment(request,id):
    data = equipments.objects.get(id=id)
    form = machineform(instance=data)
    if request.method == 'POST':
        form = machineform(request.POST or None,request.FILES or None,instance=data or None)
        if form.is_valid():
            form.save()
            return redirect('view_equipment')
    return render(request,'equipments/update_equipment.html',{'form':form})

def delete_equipment(request,id):
    equipments.objects.get(id=id).delete()
    return redirect('view_equipment')

####################### equipment section end ########################

################### customer_panel ###################################

def customer_panel(request):
    return render(request,'customer/customer_panel.html')

def customerview_equipment(request):
    data = equipments.objects.filter()
    return render(request,'customer/customer_equipment.html',{'data':data})

def customerbatch_details(request):
    data = batch.objects.filter()
    return render(request,'customer/customerbatch_details.html',{'data':data})

#################### complaints section start #################################

def complaint_register(request):
    form = complaintsform()
    if request.method == 'POST':
        form = complaintsform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_complaint')
    return render(request,'complaints/complaint_reg.html',{'form':form})

def view_complaint(request):
    data = complaints.objects.filter()
    return render(request,'complaints/view_complaints.html',{'data':data})

def delete_complaint(request,id):
    complaints.objects.get(id=id).delete()
    return redirect('view_complaint')

def admin_viewcomplaint(request):
    data = complaints.objects.filter()
    return render(request,'complaints/view_complaint_admin.html',{'data':data})

def complaint_reply(request,id):
    data = complaints.objects.get(id=id)
    form = replyform()
    if request.method=='POST':
        form = replyform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('replysee')
    return render(request,'complaints/complaint_reply.html',{'form':form})

def replysee(request):
    data = complaints.objects.filter()
    return render(request,'complaints/reply_see.html',{'data':data})

#################### complaints section end ###############################

#################### service section start ###############################

def register_service(request):
    form = serviceform()
    if request.method == 'POST':
        form = serviceform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_service')
    return render(request,'services/service_register.html',{'form':form})

def view_service(request):
    data = servicemodel.objects.filter()
    return render(request,'services/view_service.html',{'data':data})

def customerview_service(request):
    data = servicemodel.objects.filter()
    return render(request,'services/customer_view.html',{'data':data})

def update_service(request,id):
    data = servicemodel.objects.get(id=id)
    form = serviceform(instance=data)
    if request.method == 'POST':
        form = serviceform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_service')
    return render(request,'services/update_service.html',{'form':form})

def delete_service(request,id):
    servicemodel.objects.get(id=id).delete()
    return redirect('view_service')

#################### service section end ###############################

#################### attendance section start ###############################

def attendance_register(request):
    form = attendanceform()
    if request.method == 'POST':
        form = attendanceform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewcustomer_attendance')
    return render(request,'attendance/customer_attendance.html',{'form':form})

def viewcustomer_attendance(request):
    data = attendancemodel.objects.all()
    return render(request,'attendance/customerview_attendance.html',{'data':data})

def view_attendance(request):
    data = attendancemodel.objects.filter(customer=request.user)
    return render(request,'attendance/customer_view.html',{'data':data})

def update_attendance(request,id):
    data = attendancemodel.objects.get(id=id)
    form = attendanceform(instance=data)
    if request.method == 'POST':
        form = attendanceform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_attendance')
    return render(request,'attendance/update_attendance.html',{'form':form})


def delete_attendance(request,id):
    attendancemodel.objects.get(id=id).delete()
    return redirect('viewcustomer_attendance')


def register_payment(request):
    form = billform()
    if request.method == 'POST':
        form = billform(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_customer = True
            user.save()
            return redirect('view_payment')
    return render(request,'payments/customer_payment.html',{'form':form})


def view_payment(request):
    data = Bill.objects.all()
    return render(request,'payments/view_payment.html',{'data':data})

def delete_payment(request,id):
    Bill.objects.get(id=id).delete()
    return redirect('view_payment')

# def customerview_payment(request):
#     data = Bill.objects.filter(name=request.user)
#     return render(request,'payments/customerview_payment.html',{'data':data})

def pay_bill(request,id):
    bi = Bill.objects.get(id=id)
    if request.method == 'POST':
        card = request.POST.get('card')
        cvv = request.POST.get('cvv')
        expiry = request.POST.get('exp')
        creditcard(card_no=card,card_cvv=cvv,expiry_date=expiry,bill=bi).save()
        bi.status = 1
        bi.save()
        messages.info(request,'Bill paid succesfully')
        return redirect('bill_history')
    return render(request,'payments/pay_bill.html')


def pay_in_direct(request,id):
    bi = Bill.objects.get(id=id)
    bi.status = 2
    bi.save()
    messages.info(request,'Choosed to pay Fee Direct in Office')
    return redirect('bill_history')

def bill_history(request):
    u = request.user
    print(u)
    data = customuser.objects.get(username=request.user)
    print(data)
    bill = Bill.objects.filter(name=data,status__in=[0,1,2])
    print(bill)
    # u = customuser.objects.get(name=request.user)
    # bill = Bill.objects.filter(name=u, status__in=[1,2])
    return render(request, 'payments/view_bill_history.html',{'bill': bill})




def get_invoice(request,id):
    data = customuser.objects.get(username=request.user)
    bill = Bill.objects.get(id=id)
    template = get_template('payments/invoice.html')
    html = template.render({'data':bill})
    pdf = render_to_pdf('payments/invoice.html',{'data':bill})

    return HttpResponse(pdf, content_type='application/pdf')


def view_invoice(request,id):
    u = customuser.objects.get(username=request.user)
    bill = Bill.objects.filter(id=id)
    return render(request,'payments/invoice.html',{'data':bill})


#################### instructor panel start ###########################

def instructor_panel(request):
    return render(request, 'instructortemp/instructor_panel.html')


def batch_details(request):
    data = batch.objects.all()
    return render(request, 'instructortemp/batch_details.html', {'data': data})

def instructor_viewattendance(request):
    data = attendancemodel.objects.all()
    return render(request,'instructortemp/view_attendance.html',{'data':data})

def add_attendance(request):
    form = attendanceform()
    if request.method=='POST':
        form = attendanceform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instructor_viewattendance')
    return render(request,'instructortemp/add_attendance.html',{'form':form})

def update_instructor_attendance(request,id):
    data = attendancemodel.objects.get(id=id)
    form = attendanceform(instance=data)
    if request.method=='POST':
        form = attendanceform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('instructor_viewattendance')
    return render(request,'instructortemp/update_attendance.html',{'form':form})

def delete_instructor_attendance(request,id):
    attendancemodel.objects.get(id=id).delete()
    return redirect('instructor_viewattendance')

def checkout_customers(request):
    data = customuser.objects.filter(is_customer=True)
    return render(request,'instructortemp/checkout_customer.html',{'data':data})


#################### instructor panel end ###########################

#################### physician panel start ###########################

def physician_panel(request):
    return render(request,'physiciantemp/physician_panel.html')

# def appointment_available(request):
#     username = request.user.username
#     if request.user.is_physician:
#         form = appointmentform(request.user)
#         if request.method == 'POST':
#             form = appointmentform(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('all_available_appointments')
#         return render(request,'physiciantemp/appointment_available.html', {'form': form,'username': username})

# def all_available_appointments(request):
#     data = appointment.objects.all()
#     return render(request,'physiciantemp/appointment_all.html',{'data': data})
#
# def customer_view_appointment(request):
#     data = appointment.objects.all()
#     return render(request,'physiciantemp/customer_view_appointment.html',{'data': data})

@login_required
def schedule_customer(request):
    username = request.user.username
    if request.user.is_physician:
        form = scheduleform(initial={'physician_name':request.user})
        form.fields['physician_name'].queryset = customuser.objects.filter(is_physician=True,username=request.user.username)
        if request.method == 'POST':
            form = scheduleform(request.POST)
            if form.is_valid():
                form.save()
                return redirect('view_allschedule')
        return render(request,'physiciantemp/schedule_customer.html',{'form':form, 'username':username})


def view_allschedule(request):
    data = schedule.objects.all()
    return render(request,'physiciantemp/schedule_all.html',{'data':data})

def update_allschedule(request,id):
    data = schedule.objects.get(id=id)
    form = scheduleform( instance=data, initial={'physician_name':request.user})
    form.fields['physician_name'].queryset = customuser.objects.filter(is_physician=True,username=request.user.username)
    if request.method == 'POST':
        form = scheduleform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect(view_allschedule)
    return render(request,'physiciantemp/update_scheduleall.html',{'form':form})

def delete_allschedule(request,id):
    schedule.objects.get(id=id).delete()
    return redirect('view_allschedule')


def customer_view_schedule(request):
    data = schedule.objects.all()
    return render(request,'physiciantemp/customer_view_schedule.html',{'data': data})

def view_physician_schedules(request):
    user = request.user
    data = schedule.objects.filter(physician_name=user)
    return render(request,'physiciantemp/physician_view_appointment.html',{'data':data})

def take_appointment(request,id):
    s = schedule.object.get(id=id)
    c = customuser.objects.get(user=request.user)
    appo = schedule.objects.filter(physician_name=c, Schedule=s)
    if appo.exists():
        messages.info(request,'You have already requested for this schedule')
        return redirect('customer_view_schedule')
    else:
        if request.method == 'POST':
            obj = appointment
            obj.physician_name = c
            obj.Schedule = s
            obj.save()
            messages.info(request,'Appointment requested successfully')
    return render(request,'customer/take_appointment.html',{'Schedule':s})



###################### payments ####################################















