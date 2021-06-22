from django.contrib import messages, auth
from django.utils.html import strip_tags
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection

from LoginSystem.forms import Registration_form, RegularMaster_form, FrequencyMaster_form, \
    Registration_Update, SignupForm, TaxMaster_form, Form_ReturnMaster_form
from LoginSystem.models import regulator_master, RegistrationData, frequency_master, tax_master, form_return_master, \
    SignupData

def index(request):
    return render(request, 'index.html')


@login_required(login_url='calendar_login')
def homepage(request):
    return render(request, 'calendar.html')


@login_required(login_url='calendar_login')
@user_passes_test(lambda u: u.is_superuser)
def home(request):
    regulator_data = regulator_master.objects.all()
    frequency_data = frequency_master.objects.all()
    taxPayer_data = tax_master.objects.all()
    form_return_data = form_return_master.objects.all()
    if request.method == 'POST':
        form = Registration_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Task Added')
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request, 'Please enter the valid details')
            return redirect('home')
    context = {'regulator_data': regulator_data, 'frequency_data': frequency_data, 'taxPayer_data': taxPayer_data,
               'form_return_data': form_return_data}
    return render(request, 'event/event.html', context)


@login_required(login_url='calendar_login')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('calendar_login')


@login_required(login_url='calendar_login')
def report(request):
    return render(request, 'report.html')


@login_required(login_url='calendar_login')
def calendar(request):
    task_master = RegistrationData.objects.all()
    count = RegistrationData.objects.all().count()
    context = {'count': count,'task_master': task_master}
    return render(request, 'calendar.html', context)


@login_required(login_url='calendar_login')
@user_passes_test(lambda u: u.is_superuser)
def add_regulator(request):
    if request.method == 'POST':
        if regulator_master.objects.filter(regulator=request.POST['regulator']).exists():
            messages.error(request, 'The Regulator Already Exits')
            return redirect('add_regulator')
        form = RegularMaster_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Regulator Added')
            return redirect('home')
        else:
            messages.error(request, 'Please enter the valid details')
            return redirect('add_regulator')
    return render(request, 'add_regulator.html')


@login_required(login_url='calendar_login')
@user_passes_test(lambda u: u.is_superuser)
def add_frequency(request):
    if request.method == 'POST':
        if frequency_master.objects.filter(frequency=request.POST['frequency']).exists():
            messages.error(request, 'The Frequency Already Exits')
            return redirect('add_frequency')
        form = FrequencyMaster_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Frequency Added')
            return redirect('home')
        else:
            messages.error(request, 'Please enter the valid details')
            return redirect('add_frequency')
    return render(request, 'add_frequency.html')



@login_required(login_url='calendar_login')
@user_passes_test(lambda u: u.is_superuser)
def add_tax_payer(request):
    if request.method == 'POST':
        if tax_master.objects.filter(tax_payer=request.POST['tax_payer']).exists():
            messages.error(request, 'The Tax Payer Already Exits')
            return redirect('add_tax_payer')
        form = TaxMaster_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Tax Payer Added')
            return redirect('home')
        else:
            messages.error(request, 'Please enter the valid details')
            return redirect('add_tax_payer')
    return render(request, 'add_tax_payer.html')


@login_required(login_url='calendar_login')
@user_passes_test(lambda u: u.is_superuser)
def add_form_return(request):
    if request.method == 'POST':
        if form_return_master.objects.filter(form_return=request.POST['form_return']).exists():
            messages.error(request, 'The Form/Return Already Exits')
            return redirect('add_form_return')
        form = Form_ReturnMaster_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Form/Return Added')
            return redirect('home')
        else:
            messages.error(request, 'Please enter the valid details')
            return redirect('add_form_return')
    return render(request, 'add_form_return.html')


@login_required(login_url='calendar_login')
def cal_data(request):
    if request.method == 'POST':
        form = calendarMaster_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Event Added')
            return redirect('calendar')
        else:
            print(form.errors)
            messages.error(request, 'Please enter the valid details')
            return redirect('calendar')
    return render(request, 'calendar.html')


def calendar_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have successfully login!')
            return redirect('calendar')
        else:
            messages.success(request, ' Error Logging In / Please try again !')
            return redirect('calendar_login')
    return render(request, 'calendar_login.html')


def calendar_register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            qualification = request.POST['qualification']
            user = authenticate(username=username, password=password)
            New_Data = SignupData(user_name=username, password=password,qualification=qualification)
            New_Data.save()
            messages.success(request, 'Account created successfully')
            return redirect('calendar_login')
        else:
            x=form.errors.as_json
            print(x)
            messages.success(request,'Please enter the Valid Details!')
            return redirect('calendar_register')
    else:
        form = SignupForm()
    return render(request, 'calendar_register.html', {'form': form})


###########################################################################
@login_required(login_url='calendar_login')
@user_passes_test(lambda u: u.is_superuser)
def view_query_event(request):
    all_offer = RegistrationData.objects.all()
    return render(request, 'event/event_search.html', {'all_offer': all_offer})



@login_required(login_url='calendar_login')
@user_passes_test(lambda u: u.is_superuser)
def view_query_show_event(request):
    all_offer = RegistrationData.objects.all()
    if request.method == 'GET':
        search_by_date = request.GET.get("key1")
        search_id = request.GET.get("key2")
        if search_by_date and search_id:
            match = RegistrationData.objects.filter(actual_due_date__contains=search_by_date, id__contains=search_id)
            if match:
                return render(request, "event/event_search.html", {'mfind': match})
            else:
                match = RegistrationData.objects.filter(due_date_1__contains=search_by_date, id__contains=search_id)
                if match:
                    return render(request, "event/event_search.html", {'mfind': match})
                else:
                    match = RegistrationData.objects.filter(due_date_2__contains=search_by_date, id__contains=search_id)
                    if match:
                        return render(request, "event/event_search.html", {'mfind': search_by_date})
                    else:
                        match = RegistrationData.objects.filter(due_date_3__contains=search_by_date,
                                                                id__contains=search_id)
                        if match:
                            return render(request, "event/event_search.html", {'mfind': match})
                        else:
                            match = RegistrationData.objects.filter(due_date_4__contains=search_by_date,
                                                                    id__contains=search_id)
                            if match:
                                return render(request, "event/event_search.html", {'mfind': match})
                            else:
                                match = RegistrationData.objects.filter(due_date_5__contains=search_by_date,
                                                                        id__contains=search_id)
                                if match:
                                    return render(request, "event/event_search.html", {'mfind': match})
                                else:
                                    messages.warning(request, "Doesnt Match any Field!Try Again!")
                                    return render(request, "event/event_search.html")
        elif search_by_date:
            match = RegistrationData.objects.filter(actual_due_date__contains=search_by_date)
            if match:
                return render(request, "event/event_search.html", {'mfind': match})
            else:
                match = RegistrationData.objects.filter(due_date_1__contains=search_by_date)
                if match:
                    return render(request, "event/event_search.html", {'mfind': match})
                else:
                    match = RegistrationData.objects.filter(due_date_2__contains=search_by_date)
                    if match:
                        return render(request, "event/event_search.html", {'mfind': match})
                    else:
                        match = RegistrationData.objects.filter(due_date_3__contains=search_by_date)
                        if match:
                            return render(request, "event/event_search.html", {'mfind': match})
                        else:
                            match = RegistrationData.objects.filter(due_date_4__contains=search_by_date)
                            if match:
                                return render(request, "event/event_search.html", {'mfind': match})
                            else:
                                match = RegistrationData.objects.filter(due_date_5__contains=search_by_date)
                                if match:
                                    return render(request, "event/event_search.html", {'mfind': match})
                                else:
                                    messages.warning(request, "Doesnt Match any Field!Try Again!")
                                    return render(request, "event/event_search.html")
        elif search_id:
            match = RegistrationData.objects.filter(id__contains=search_id)
            if match:
                return render(request, "event/event_search.html", {'mfind': match})
            else:
                match = RegistrationData.objects.filter(regulator__contains=search_id)
                if match:
                    return render(request, "event/event_search.html", {'mfind': match})
                else:
                    match = RegistrationData.objects.filter(frequency__contains=search_id)
                    if match:
                        return render(request, "event/event_search.html", {'mfind': match})
                    else:
                        match = RegistrationData.objects.filter(financial_year__contains=search_id)
                        if match:
                            return render(request, "event/event_search.html", {'mfind': match})
                        else:
                            match = RegistrationData.objects.filter(form_return__contains=search_id)
                            if match:
                                return render(request, "event/event_search.html", {'mfind': match})
                            else:                             
                                messages.warning(request, "Doesnt Match any Field ! Try Again !")
                                return render(request, "event/event_search.html")
        else:
            messages.warning(request, "Invalid Input!")
            return render(request, "event/event_search.html")
    return render(request, "event/event_search.html", {'all_offer': all_offer})


@login_required(login_url='calendar_login')
@user_passes_test(lambda u: u.is_superuser)
def delete_event(request, pk, template="event/event_delete.html"):
    contact = get_object_or_404(RegistrationData, pk=pk)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, "Successfully Deleted!")
        return redirect('view_query_event')
    return render(request, template, {'object': contact})


@login_required(login_url='calendar_login')
@user_passes_test(lambda u: u.is_superuser)
def update(request, pk):
    context = {}
    obj = get_object_or_404(RegistrationData, pk=pk)
    form = Registration_Update(request.POST or None, instance=obj)
    task_form = RegistrationData.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Updated !")
        else:
            messages.error(request,"Error Updating ! Please Try Again !")
    context={'form':form,'task_form':task_form,'obj':obj}
    return render(request, "event/event_update.html", context)



@login_required(login_url='calendar_login')
@user_passes_test(lambda u: u.is_superuser)
def default_data(request):
    cursor = connection.cursor()
    if cursor.execute('''SELECT * FROM `regulator master` ''') <= 0:
        cursor.execute('''INSERT INTO `regulator master` VALUES('1','GST','#e66465')''')
        cursor.execute('''INSERT INTO `regulator master` VALUES('2','INCOME TAX','#e66465')''')
        cursor.execute('''INSERT INTO `regulator master` VALUES('3','RBI','#e66465')''')
        cursor.execute('''INSERT INTO `regulator master` VALUES('4','PF','#e66465')''')
        cursor.execute('''INSERT INTO `regulator master` VALUES('5','ESIC','#e66465')''')
        cursor.execute('''INSERT INTO `regulator master` VALUES('6','PTAX','#e66465')''')
        cursor.execute('''INSERT INTO `regulator master` VALUES('7','SEBI','#e66465')''')

    if cursor.execute('''SELECT * FROM `frequency master` ''') <= 0:
        cursor.execute('''INSERT INTO `frequency master` VALUES('1','Monthly')''')
        cursor.execute('''INSERT INTO `frequency master` VALUES('2','Anually')''')
        cursor.execute('''INSERT INTO `frequency master` VALUES('3','Quaterly')''')

    if cursor.execute('''SELECT * FROM `form/return master` ''') <= 0:
        cursor.execute('''INSERT INTO `form/return master` VALUES('1','GSTR-3B')''')
        cursor.execute('''INSERT INTO `form/return master` VALUES('2','GSTR-1')''')

    if cursor.execute('''SELECT * FROM `tax master` ''') <= 0:
        cursor.execute('''INSERT INTO `tax master` VALUES('1','Composite')''')
        cursor.execute('''INSERT INTO `tax master` VALUES('2','Regular')''')
        cursor.execute('''INSERT INTO `tax master` VALUES('3','Individual')''')
        cursor.execute('''INSERT INTO `tax master` VALUES('4','Partnership')''')
        cursor.execute('''INSERT INTO `tax master` VALUES('5','Private Limited')''')
        cursor.execute('''INSERT INTO `tax master` VALUES('6','Public Limited')''')
        cursor.execute('''INSERT INTO `tax master` VALUES('8','Listed')''')
        cursor.execute('''INSERT INTO `tax master` VALUES('9','Unlisted')''')
        cursor.execute('''INSERT INTO `tax master` VALUES('10','Trust')''')
    messages.success(request, "Successfully stored all defaut value !")
    return redirect(home)



@login_required(login_url='calendar_login')
def view_query_show_report(request):
    all_offer = RegistrationData.objects.all()
    if request.method == 'GET':
        search_by_date = request.GET.get("key1")
        search_id = request.GET.get("key2")
        search_by_start_date = request.GET.get("start_date")
        search_by_end_date = request.GET.get("end_date")
        if search_by_date and search_id:
            match = RegistrationData.objects.filter(actual_due_date__contains=search_by_date, id__contains=search_id)
            if match:
                return render(request, "report.html", {'mfind': match})
            else:
                match = RegistrationData.objects.filter(due_date_1__contains=search_by_date, id__contains=search_id)
                if match:
                    return render(request, "report.html", {'mfind': match})
                else:
                    match = RegistrationData.objects.filter(due_date_2__contains=search_by_date, id__contains=search_id)
                    if match:
                        return render(request, "report.html", {'mfind': search_by_date})
                    else:
                        match = RegistrationData.objects.filter(due_date_3__contains=search_by_date,
                                                                id__contains=search_id)
                        if match:
                            return render(request, "report.html", {'mfind': match})
                        else:
                            match = RegistrationData.objects.filter(due_date_4__contains=search_by_date,
                                                                    id__contains=search_id)
                            if match:
                                return render(request, "report.html", {'mfind': match})
                            else:
                                match = RegistrationData.objects.filter(due_date_5__contains=search_by_date,
                                                                        id__contains=search_id)
                                if match:
                                    return render(request, "report.html", {'mfind': match})
                                else:
                                    messages.warning(request, "Doesnt Match any Field ! Try Again !")
                                    return render(request, "report.html")
        elif search_by_date:
            match = RegistrationData.objects.filter(actual_due_date__contains=search_by_date)
            if match:
                return render(request, "report.html", {'mfind': match})
            else:
                match = RegistrationData.objects.filter(due_date_1__contains=search_by_date)
                if match:
                    return render(request, "report.html", {'mfind': match})
                else:
                    match = RegistrationData.objects.filter(due_date_2__contains=search_by_date)
                    if match:
                        return render(request, "report.html", {'mfind': match})
                    else:
                        match = RegistrationData.objects.filter(due_date_3__contains=search_by_date)
                        if match:
                            return render(request, "report.html", {'mfind': match})
                        else:
                            match = RegistrationData.objects.filter(due_date_4__contains=search_by_date)
                            if match:
                                return render(request, "report.html", {'mfind': match})
                            else:
                                match = RegistrationData.objects.filter(due_date_5__contains=search_by_date)
                                if match:
                                    return render(request, "report.html", {'mfind': match})
                                else:
                                    messages.warning(request, "Doesnt match any due date ! Please Try Again !")
                                    return render(request, "report.html")
        elif search_id:
            match = RegistrationData.objects.filter(id__contains=search_id)
            if match:
                return render(request, "report.html", {'mfind': match})
            else:
                match = RegistrationData.objects.filter(regulator__contains=search_id)
                if match:
                    return render(request, "report.html", {'mfind': match})
                else:
                    match = RegistrationData.objects.filter(frequency__contains=search_id)
                    if match:
                        return render(request, "report.html", {'mfind': match})
                    else:
                        match = RegistrationData.objects.filter(financial_year__contains=search_id)
                        if match:
                            return render(request, "report.html", {'mfind': match})
                        else:
                            match = RegistrationData.objects.filter(form_return__contains=search_id)
                            if match:
                                return render(request, "report.html", {'mfind': match})
                            else:                             
                                messages.warning(request, "Doesnt Match any Field !Try Again !")
                                return render(request, "report.html")
        elif search_by_start_date and search_by_end_date:
            match = RegistrationData.objects.filter(actual_due_date__range=(search_by_start_date, search_by_end_date))
            return render(request, "report.html", {'mfind': match})
        else:
            messages.warning(request, "Invalid Input ! Please Try Again !")
            return render(request, "report.html") 
    return render(request, "report.html", {'all_offer': all_offer})


@login_required(login_url='calendar_login')
@user_passes_test(lambda u: u.is_superuser)
def view_query_get_event(request):
    if request.method == 'GET':
        search_by_date = request.GET.get("date")
        if search_by_date:
            match = calendar_master.objects.filter(date__contains=search_by_date)
            return render(request, 'calendar.html', {'match': match})
        else:
            messages.error(request, "Date Not Found !")
    return render(request, 'calendar.html')


@login_required(login_url='calendar_login')
def all_event(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        mfind = RegistrationData.objects.filter(latest_due_date__contains=date)
        context = {'mfind':mfind,'date':date}
        return render(request, 'event/all_event.html', context)
    return render(request, 'event/all_event.html')