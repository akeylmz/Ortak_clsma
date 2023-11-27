from django.http.response import HttpResponse
from django.db.models import Case, When, Value, IntegerField, F, Count, Sum
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectForm, ExpensesForm, IncomesForm, JobHistoryForm, ClientsForm, SupplierForm
from .models import Project, Expenses, Incomes, PaymentFirms, CompanyNames, JobHistory, ProjectNames, MyCompanyNames, PaymentFirms, Clients , Supplier
from django.db.models import Q
from django import template

register = template.Library()

@register.simple_tag
def update_widget_attrs(field, attrs):
    field.widget.attrs.update(attrs)
    return field

'''def get_realized_cost_data(project_name, payment_firms_names):
    # JobHistory ve Expenses tablolarını birleştirip firma adına göre gruplayın
    data = (
        JobHistory.objects.filter(
            Q(ProjectName_JobHistory=project_name) & Q(ProjectName_Job_JobHistory__in=payment_firms_names)
        )
        .values('ProjectName_Job_JobHistory')
        .annotate(
            total_job_tl=Sum('Amount_TL_JobHistory'),
            total_job=Sum('Amount_JobHistory'),
            total_expense_tl=Value(0, output_field=IntegerField()),
            total_expense=Value(0, output_field=IntegerField()),
        )
        .union(
            Expenses.objects.filter(
                Q(ProjectName_Expenses=project_name) & Q(ProjectName_Paying_Expenses__in=payment_firms_names)
            )
            .values('CompanyName_Paying_Expenses')
            .annotate(
                total_expense_tl=Sum('Amount_TL_Expenses'),
                total_expense=Sum('Amount_Expenses'),
                total_job_tl=Value(0, output_field=IntegerField()),
                total_job=Value(0, output_field=IntegerField()),
            )
        )
        .order_by('CompanyName_Job_JobHistory')
    )

    result_data = []
    for entry in data:
        result_data.append({
            'company_name': entry.get('CompanyName_Job_JobHistory') or entry.get('CompanyName_Paying_Expenses'),
            'total_job_tl': entry.get('total_job_tl', 0),
            'total_job': entry.get('total_job', 0),
            'total_expense_tl': entry.get('total_expense_tl', 0),
            'total_expense': entry.get('total_expense', 0),
        })

    return result_data'''


# Create your views here.
def expenses_edit(request, expenses_id):
    expenses_edit = get_object_or_404(Expenses, id=expenses_id)
    my_company = MyCompanyNames.objects.all()
    supplier = Supplier.objects.all()
    banks = Banks.objects.all()
    details = Details.objects.all()
   
    if request.method == 'POST':
        edit_form = ExpensesForm(request.POST, instance=expenses_edit)
        
        if edit_form.is_valid():
          
          edit_form.save()
          return redirect('realized_cost', project_name=expenses_edit.ProjectName_Expenses)
    else:
        edit_form = ExpensesForm(instance=expenses_edit)
    context = {
        'edit_form': edit_form,
        'expenses_edit': expenses_edit,
        'my_company': my_company,
        'supplier': supplier,
        'banks': banks,
        'details': details,
    }
    return render(request, "expenses_edit.html", context)

def jobhistory_edit(request, jobhistory_id):
    jobhistory_edit = get_object_or_404(JobHistory, id=jobhistory_id)
    my_company = MyCompanyNames.objects.all()
    supplier = Supplier.objects.all()
    if request.method == 'POST':
        edit_form = JobHistoryForm(request.POST, instance=jobhistory_edit)
        
        if edit_form.is_valid():
          
          edit_form.save()
          return redirect('realized_cost', project_name=jobhistory_edit.ProjectName_JobHistory)
    else:
        edit_form = JobHistoryForm(instance=jobhistory_edit)
    context = {
        'edit_form': edit_form,
        'jobhistory_edit': jobhistory_edit,
        'my_company': my_company,
        'supplier': supplier
    }
    return render(request, "jobhistory_edit.html", context)

def income_edit(request, income_id):
    income_edit = get_object_or_404(Incomes, id=income_id)
    my_company = MyCompanyNames.objects.all()

    if request.method == 'POST':
        edit_form = IncomesForm(request.POST, instance=income_edit)
        
        if edit_form.is_valid():
          
          edit_form.save()
          return redirect('income_details', project_name=income_edit.ProjectName_Incomes)
    else:
        edit_form = IncomesForm(instance=income_edit)
    context = {
        'edit_form': edit_form,
        'income_edit': income_edit,
        'my_company': my_company
    }
    return render(request, "income_edit.html", context)

def supplier_edit(request, supplier_name):
    supplier_edit = get_object_or_404(Supplier, CompanyName_Supplier=supplier_name)
    locations = Locations.objects.all()
   
    if request.method == 'POST':
        edit_form = SupplierForm(request.POST, instance=supplier_edit)
        
        if edit_form.is_valid():
          
          edit_form.save()
          return redirect('supplier')
    else:
        edit_form = SupplierForm(instance=supplier_edit)
    context = {
        'edit_form': edit_form,
        'supplier_edit': supplier_edit,
        'locations': locations
    
    }
    return render(request, "supplier_edit.html", context)

def client_edit(request, client_name):
    client_edit = get_object_or_404(Clients, CompanyName_Clients=client_name)
    locations = Locations.objects.all()

    if request.method == 'POST':
        edit_form = ClientsForm(request.POST, instance=client_edit)
       
        if edit_form.is_valid():
          
          edit_form.save()
          return redirect('client')
    else:
        edit_form = ClientsForm(instance=client_edit)
    context = {
        'edit_form': edit_form,
        'client_edit': client_edit,
        'locations': locations
    }
    return render(request, "client_edit.html", context)

def project_edit(request, project_name):
    project_edit = get_object_or_404(Project, ProjectName=project_name)
    my_company = MyCompanyNames.objects.all()
    client = Clients.objects.all()
    locations = Locations.objects.all()
    terrain_roof = Terrain_Roof.objects.all()
    situations = Situations.objects.all()


   
    if request.method == 'POST':
        edit_form = ProjectForm(request.POST, instance=project_edit)
        if edit_form.is_valid():
          edit_form.save()
          return redirect('projects')
    else:
        edit_form = ProjectForm(instance=project_edit)
    context = {
        'edit_form': edit_form,
        'project_edit': project_edit,
        'my_company':my_company,
        'client':client,
        'locations':locations,
        'terrain_roof':terrain_roof,
        'situations':situations,
    }
    return render(request, "project_edit.html", context)

def index(request):
    if request.method == 'POST':
        index_form = JobHistoryForm(request.POST)
        if index_form.is_valid():
            index_form.save()
            return redirect('index')
    else:
        index_form = JobHistoryForm()

    context = {
        'index_form': index_form,
    
    }

    return render(request, 'index.html', context)

def home(request):
    return render(request, "home.html")

def client(request):
    if request.method == 'POST':
        client_form = ClientsForm(request.POST)
        if client_form.is_valid():
            client_form.save()
            return redirect('client')
    else:
        client_form = ClientsForm()

    clients = Clients.objects.all()

    context = {
        'clients': clients,
        'client_form': client_form
    }

    return render(request, 'client.html', context)

def supplier(request):
    if request.method == 'POST':
        supplier_form = SupplierForm(request.POST)
        if supplier_form.is_valid():
            supplier_form.save()
            return redirect('supplier')
    else:
        supplier_form = SupplierForm()

    supplier = Supplier.objects.all()

    context = {
        'supplier': supplier,
        'supplier_form': supplier_form
    }
    return render(request, "supplier.html", context)

def project_details(request, project_name):
    project = Project.objects.filter(ProjectName=project_name).first()
    return render(request, 'project_details.html', {'project': project})

def realized_cost(request, project_name):
    payment_firms = PaymentFirms.objects.all()
    payment_firms_names = [pf.PaymentFirmsName for pf in payment_firms]

    project = get_object_or_404(Project, ProjectName=project_name)
    expenses = Expenses.objects.filter(Q(ProjectName_Expenses=project.ProjectName) & Q(CompanyName_Paying_Expenses__in=payment_firms_names))
    jobhistory = JobHistory.objects.filter(ProjectName_JobHistory=project_name)

    # Get distinct companies from PaymentFirms
    distinct_payment_firms = PaymentFirms.objects.all().values('PaymentFirmsName').distinct()

    # Get distinct companies from Expenses and JobHistory
    distinct_expenses_companies = Expenses.objects.filter(ProjectName_Expenses=project_name).values('CompanyName_Paying_Expenses').distinct()
    distinct_job_history_companies = JobHistory.objects.filter(ProjectName_JobHistory=project_name).values('CompanyName_Job_JobHistory').distinct()

    # Combine the distinct companies from Expenses and JobHistory
    distinct_expenses_companies_names = [expense['CompanyName_Paying_Expenses'] for expense in distinct_expenses_companies]
    distinct_job_history_companies_names = [history['CompanyName_Job_JobHistory'] for history in distinct_job_history_companies]

    # Merge the distinct companies from both models
    merged_distinct_companies = set(distinct_expenses_companies_names) | set(distinct_job_history_companies_names)

    # Filter distinct_payment_firms based on merged_distinct_companies
    filtered_payment_firms = distinct_payment_firms.filter(PaymentFirmsName__in=merged_distinct_companies)

    # Prepare the list of distinct company names
    distinct_company_names = [company['PaymentFirmsName'] for company in filtered_payment_firms]

    if request.method == 'POST':
        expenses_form = ExpensesForm(request.POST)
        jobhistory_form = JobHistoryForm(request.POST)
        supplier_form = SupplierForm(request.POST)

        if expenses_form.is_valid():
           
            expenses_form.save()
            return redirect(request.path)

        if jobhistory_form.is_valid():
            # Do something with the valid JobHistoryForm data
            jobhistory_form.save()
            return redirect(request.path)
        
        if supplier_form.is_valid():
            # Do something with the valid JobHistoryForm data
            supplier_form.save()
            return redirect(request.path)
    else:
        expenses_form = ExpensesForm()
        jobhistory_form = JobHistoryForm()
        supplier_form = SupplierForm()

    context = {
        "project": project,
        "expenses": expenses,   
        "jobhistory": jobhistory,
        "expenses_form": expenses_form,
        "jobhistory_form": jobhistory_form,
        "supplier_form": supplier_form,
        "distinct_company_names": distinct_company_names,
        #"result_data": result_data,
    }
    return render(request, "realized_cost.html", context)

def income_details(request, project_name):
    project = Project.objects.filter(ProjectName=project_name).first()
    incomes = Incomes.objects.filter(ProjectName_Incomes=project_name)
    incomes_form = IncomesForm()

    if request.method == 'POST':
        incomes_form = IncomesForm(request.POST)
        if incomes_form.is_valid():
            incomes_form.instance.CompanyName_Incomes = project.CompanyName
            incomes_form.instance.save()
            return redirect('income_details', project_name=project_name)
        else:
            incomes_form = IncomesForm()

    context = {
        "project": project,
        "incomes": incomes,
        "incomes_form": incomes_form,
    }
    return render(request, "income_details.html", context)

def projects(request):
    project = Project.objects.annotate(
        custom_order_situation=Case(
            When(Situation="Onay Bekliyor", then=Value(1)),
            When(Situation="Devam Ediyor", then=Value(2)),
            When(Situation="Tamamlandı", then=Value(3)),
            default=Value(4),
            output_field=IntegerField()
        ),
        custom_order_date=F('StartDate')
    ).order_by('custom_order_situation', 'custom_order_date')

    
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        
        if form_type == 'expenses_form':
            expenses_form = ExpensesForm(request.POST)
            if expenses_form.is_valid():
                expenses_form.save()
                return redirect(request.path)
        
        elif form_type == 'incomes_form':
            incomes_form = IncomesForm(request.POST)
            if incomes_form.is_valid():
                incomes_form.save()
                return redirect(request.path)
            
        elif form_type == 'jobhistory_form':
            jobhistory_form = JobHistoryForm(request.POST)
            if jobhistory_form.is_valid():
                jobhistory_form.save()
                return redirect(request.path)
        
        elif form_type == 'client_form':
            client_form = ClientsForm(request.POST)
            if client_form.is_valid():
                client_form.save()
                return redirect(request.path)
        
        elif form_type == 'supplier_form':
            supplier_form = SupplierForm(request.POST)
            if supplier_form.is_valid():
                supplier_form.save()
                return redirect(request.path)
        
        elif form_type == 'form':
            form = ProjectForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(request.path)
        
    else:
        supplier_form = SupplierForm()
        client_form = ClientsForm()
        expenses_form = ExpensesForm()
        incomes_form = IncomesForm()
        jobhistory_form = JobHistoryForm()
        form = ProjectForm()
        

    context = {
        "project": project,
        "form": form,
        "expenses_form": expenses_form,  # Şimdi gider formunu da şablona ekleyin
        "incomes_form": incomes_form,
        "jobhistory_form": jobhistory_form,
        'client_form': client_form,
        'supplier_form': supplier_form
    }

    return render(request, "projects.html", context)
