from django import forms
from datetime import datetime
from .models import Project, ProjectNames, Expenses, Incomes, JobHistory ,CompanyNames, MyCompanyNames, Locations, Terrain_Roof, Banks, Clients, Supplier, Details, Situations
   
min_date = datetime(2000, 1, 1)
max_date = datetime(2099, 12, 30) 

class MyModelChoiceWidget(forms.widgets.Select):
    def build_attrs(self, base_attrs, extra_attrs=None, **kwargs):
        attrs = super().build_attrs(base_attrs, extra_attrs, **kwargs)
        attrs['class'] = 'js-example-basic-single'
        return attrs

class ProjectForm(forms.ModelForm):
   

    ProjectName = forms.CharField(max_length=63, label="Proje Adını Giriniz")
    ProjectCode = forms.CharField(max_length=63)
    CompanyName = forms.ModelChoiceField(
        queryset=Clients.objects.all().order_by('CompanyName_Clients'),
        empty_label="Firma Adını Seçiniz",
        widget=MyModelChoiceWidget,
    )  
    CompanyUndertakingWork = forms.ModelChoiceField(
        queryset=MyCompanyNames.objects.all(),
        empty_label="İşi Üstlenen Firma Adını Seçiniz",
    )    
    Location = forms.ModelChoiceField(
        queryset=Locations.objects.all(),
        empty_label= 'Konum Seçiniz',
        required=False,
        widget=MyModelChoiceWidget,
    )    
    Cost_NotIncludingKDV = forms.FloatField(required=False)        
    AC_Power = forms.IntegerField(required=False,)
    DC_Power = forms.IntegerField(required=False,)
    CalculatedCost_NotIncludingKDV = forms.DecimalField(  
        max_digits=17,
        decimal_places=4,
        required=False,
    )
    RealizedCost_NotIncludingKDV = forms.DecimalField(  
        max_digits=17,
        decimal_places=4,
        required=False,
    )
    Incentive = forms.ChoiceField(
        choices=[(False, 'Hayır'), (True, 'Evet')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False,
    )
    CalculatedProfit_Loss = forms.DecimalField(  
        max_digits=17,
        decimal_places=4,
        required=False,
    )
    RealizedProfit_Loss = forms.DecimalField(  
        max_digits=17,
        decimal_places=4,
        required=False,
    )
    CalculatedProfitRate = forms.DecimalField(  
        max_digits=8,
        decimal_places=4,
        required=False,
    )
    RealizedProfitRate = forms.DecimalField(  
        max_digits=8,
        decimal_places=4,
        required=False,
    )
    Terrain_Roof = forms.ModelChoiceField(
        queryset=Terrain_Roof.objects.all(),
        required=False,
        empty_label= 'Seçiniz',
    )    
    KDV_Rate = forms.DecimalField(  
        max_digits=6,
        decimal_places=4,
        required=False,
        initial=20.0
    )
    Situation = forms.ModelChoiceField(
        queryset=Situations.objects.all(),
        required=False,
        empty_label= 'Seçiniz',
    )    
    StartDate = forms.DateField(
        label='Tarih Seçiniz', 
        widget=forms.widgets.DateInput(attrs={'type': 'date', 'min': min_date, 'max': max_date}),
        required=False,
    )
    FinishDate = forms.DateField(
        label='Tarih Seçiniz', 
        widget=forms.widgets.DateInput(attrs={'type': 'date', 'min': min_date, 'max': max_date}),
        required=False,
    )

    class Meta:
        model = Project
        fields = ['CompanyName', 'Location', 'AC_Power', 'DC_Power', 'CompanyUndertakingWork',
                'CalculatedCost_NotIncludingKDV', 'RealizedCost_NotIncludingKDV','CalculatedProfit_Loss', 
                'RealizedProfit_Loss', 'CalculatedProfitRate', 'RealizedProfitRate', 'Cost_NotIncludingKDV', 
                'KDV_Rate', 'Terrain_Roof', 'Incentive','Situation',
                  'StartDate', 'FinishDate','ProjectName','ProjectCode']
        
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

class ExpensesForm(forms.ModelForm):
    ProjectName_Expenses_Copy = forms.CharField(max_length=63, required=False)
    ProjectName_Expenses = forms.ModelChoiceField(
        queryset=ProjectNames.objects.all().order_by('ProjectName'),
        label='Project Name',
        empty_label="Proje Adını Seçiniz",
        required=False, 
        widget=MyModelChoiceWidget,
    )
    CompanyName_Expenses = forms.ModelChoiceField(
        queryset=CompanyNames.objects.all().order_by('CompanyName'),
        empty_label="Firma Adını Seçiniz",
        required=False,
        widget=MyModelChoiceWidget,
    )
    CompanyName_FromPaymentMade_Expenses = forms.ModelChoiceField(
        queryset=MyCompanyNames.objects.all(),
        empty_label="Firma Adını Seçiniz",
        required=False
    )
    CompanyName_Paying_Expenses = forms.ModelChoiceField(
        queryset=Supplier.objects.all().order_by('CompanyName_Supplier'),
        empty_label="Firma Adını Seçiniz",
        widget=MyModelChoiceWidget,
    )
    ExpensDetails_Expenses = forms.ModelChoiceField(
        queryset=Details.objects.all(),
        widget=MyModelChoiceWidget,
    )
    Amount_Expenses = forms.DecimalField(  
        max_digits=17,
        decimal_places=4,
        required=False,
    )
    Dollar_Rate_Expenses = forms.DecimalField(  
        max_digits=8,
        decimal_places=4,
        required=False,
    )
    Bank_Expenses = forms.ModelChoiceField(
        queryset=Banks.objects.all(),
        empty_label="Banka Seçiniz",
        required=False,
        widget=MyModelChoiceWidget,
    )
    Date_Expenses = forms.DateField(
        label='Tarih Seçiniz',
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        required=False,
    )

    class Meta:
        model = Expenses
        fields = ['CompanyName_Expenses', 'CompanyName_FromPaymentMade_Expenses', 'CompanyName_Paying_Expenses',
                  'ExpensDetails_Expenses', 'Amount_Expenses', 'Dollar_Rate_Expenses', 'Bank_Expenses',
                  'Date_Expenses', 'ProjectName_Expenses', 'ProjectName_Expenses_Copy']   

class JobHistoryForm(forms.ModelForm):
    ProjectName_JobHistory_Copy = forms.CharField(max_length=63, required=False)
    ProjectName_JobHistory = forms.ModelChoiceField(
        queryset=ProjectNames.objects.all().order_by('ProjectName'),
        label='ProjectName',
        empty_label= "Proje Adını Seçiniz",
        required=False,
        widget=MyModelChoiceWidget,
    )
    #CompanyName = forms.CharField(required=False, max_length=63)
    CompanyName_FromJobMade_JobHistory = forms.ModelChoiceField(
        queryset=MyCompanyNames.objects.all(),
        empty_label="Firma Adını Seçiniz",
        required=False,
        label='CompanyName_FromJobMade'
    )
    CompanyName_Job_JobHistory = forms.ModelChoiceField(
        queryset=Supplier.objects.all().order_by('CompanyName_Supplier'),  # 'company_name' yerine sıralamak istediğiniz alanı kullanın
        empty_label="Firma Adını Seçiniz",
        widget=MyModelChoiceWidget,
    )
  
    ExpensDetails_JobHistory = forms.CharField(required=False, max_length=1000, initial='Diğer')
    Invoice_No_JobHistory = forms.CharField(required=False, max_length=63)
    Amount_JobHistory = forms.DecimalField(  
        max_digits=17,
        decimal_places=4,
        required=False,
    )
    Dollar_Rate_JobHistory = forms.DecimalField(
        max_digits=8,
        decimal_places=4,
        required=False,
       )
    Date_JobHistory = forms.DateField(
        label='Tarih Seçiniz',
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        required=False
    )

    class Meta:
        model = JobHistory
        fields = ['ProjectName_JobHistory', 'CompanyName_FromJobMade_JobHistory', 'CompanyName_Job_JobHistory','ProjectName_JobHistory_Copy',
                  'ExpensDetails_JobHistory', 'Amount_JobHistory', 'Dollar_Rate_JobHistory', 'Date_JobHistory', 'Invoice_No_JobHistory']

class IncomesForm(forms.ModelForm):
    ProjectName_Incomes_Copy = forms.CharField(max_length=63, required=False)
    ProjectName_Incomes = forms.ModelChoiceField(
        queryset=ProjectNames.objects.all().order_by('ProjectName'),
        empty_label= "Proje Adını Seçiniz",
        widget=MyModelChoiceWidget,        required=False,
    )       
    CompanyName_ReceivePayment_Incomes = forms.ModelChoiceField(
        queryset=MyCompanyNames.objects.all(),
        empty_label= "Firma Adını Seçiniz",
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    CompanyName_Pay_Incomes = forms.ModelChoiceField(
        queryset=Clients.objects.all().order_by('CompanyName_Clients'),  # 'company_name' yerine sıralamak istediğiniz alanı kullanın
        empty_label="Firma Adını Seçiniz",
        widget=MyModelChoiceWidget,
    )
    Amount_Incomes_Incomes = forms.DecimalField(  
        max_digits=17,
        decimal_places=4,
        required=False,
    )
    Dollar_Rate_Incomes = forms.DecimalField(
        max_digits=8,
        decimal_places=4,
        required=False,
       )
    PaymentType_Incomes = forms.ChoiceField(
        choices=[('','Ödeme Yöntemi Seçiniz'), ('Kredi Kartı', 'Kredi Kartı'), ('EFT', 'EFT'), ('Çek', 'Çek')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False,
    )
    ChekDate_Incomes = forms.DateField(
        required=False,
        widget=forms.SelectDateWidget(attrs={'class': 'form-control'}),
        )
    LastChekDate_Incomes = forms.DateField(
        required=False,
        widget=forms.SelectDateWidget(attrs={'class': 'form-control'}),
        )

    class Meta:
        model = Incomes
        fields = ['ProjectName_Incomes','CompanyName_ReceivePayment_Incomes','Dollar_Rate_Incomes','ProjectName_Incomes_Copy',
                   'Amount_Incomes','PaymentType_Incomes','ChekDate_Incomes', "LastChekDate_Incomes","CompanyName_Pay_Incomes"
                  ]

class ClientsForm(forms.ModelForm):
    CompanyName_Clients_New = forms.CharField(max_length=63, required=False)
    CompanyName_Clients = forms.CharField(max_length=63)
    ContactPerson = forms.CharField(max_length=63, required=False)
    PhoneNumber = forms.CharField(max_length=11, required=False)
    Email= forms.CharField(max_length=63, required=False)
    Location = forms.ModelChoiceField(
        queryset=Locations.objects.all(),
        empty_label= "Konum Seçiniz",
        required=False,
        widget=MyModelChoiceWidget,

    ) 
    class Meta:
        model = Clients 
        fields = '__all__'

class SupplierForm(forms.ModelForm):
    CompanyName_Supplier_New = forms.CharField(max_length=63, required=False)
    CompanyName_Supplier = forms.CharField(max_length=63)
    ContactPerson = forms.CharField(max_length=63, required=False)
    PhoneNumber = forms.CharField(max_length=11, required=False)
    Email= forms.CharField(max_length=63, required=False)
    Location = forms.ModelChoiceField(
        queryset=Locations.objects.all(),
        empty_label= "Konum Seçiniz",
        required=False,
        widget=MyModelChoiceWidget,

    )    
    class Meta:
        model = Supplier 
        fields = '__all__'