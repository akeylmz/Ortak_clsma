# Generated by Django 4.2.7 on 2023-11-15 17:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BankName', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyName_Clients', models.CharField(blank=True, max_length=63, null=True)),
                ('ContactPerson', models.CharField(blank=True, max_length=63, null=True)),
                ('PhoneNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('Email', models.CharField(blank=True, max_length=63, null=True)),
                ('Location', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyName', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectName_Expenses', models.CharField(blank=True, max_length=63, null=True)),
                ('ProjectCode_Expenses', models.CharField(blank=True, max_length=63, null=True)),
                ('CompanyName_Expenses', models.CharField(blank=True, max_length=63, null=True)),
                ('CompanyName_FromPaymentMade_Expenses', models.CharField(blank=True, max_length=63, null=True)),
                ('CompanyName_Paying_Expenses', models.CharField(blank=True, max_length=63, null=True)),
                ('ExpensDetails_Expenses', models.CharField(blank=True, max_length=1000, null=True)),
                ('Amount_Expenses', models.FloatField(blank=True, null=True)),
                ('Amount_TL_Expenses', models.FloatField(blank=True, null=True)),
                ('Dollar_Rate_Expenses', models.FloatField(blank=True, null=True)),
                ('Bank_Expenses', models.CharField(blank=True, max_length=63, null=True)),
                ('Date_Expenses', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Incomes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectName_Incomes', models.CharField(blank=True, max_length=63, null=True)),
                ('CompanyName_ReceivePayment_Incomes', models.CharField(blank=True, max_length=63, null=True)),
                ('Amount_Incomes', models.FloatField(blank=True, null=True)),
                ('Dollar_Rate_Incomes', models.FloatField(blank=True, null=True)),
                ('PaymentType_Incomes', models.CharField(blank=True, max_length=63, null=True)),
                ('ChekDate_Incomes', models.DateField(default=django.utils.timezone.now)),
                ('LastChekDate_Incomes', models.DateField(blank=True, null=True)),
                ('Amount_Usd_Incomes', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectName_JobHistory', models.CharField(blank=True, max_length=63, null=True)),
                ('CompanyName_JobHistory', models.CharField(blank=True, max_length=63, null=True)),
                ('CompanyName_FromJobMade_JobHistory', models.CharField(blank=True, max_length=63, null=True)),
                ('CompanyName_Job_JobHistory', models.CharField(blank=True, max_length=63, null=True)),
                ('ExpensDetails_JobHistory', models.CharField(blank=True, max_length=1000, null=True)),
                ('Invoice_No_JobHistory', models.CharField(blank=True, max_length=63, null=True)),
                ('Amount_JobHistory', models.FloatField(blank=True, null=True)),
                ('Amount_TL_JobHistory', models.FloatField(blank=True, null=True)),
                ('Dollar_Rate_JobHistory', models.FloatField(blank=True, null=True)),
                ('Date_JobHistory', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='MyCompanyNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MyCompanyName', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentFirms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PaymentFirmsName', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectName', models.CharField(blank=True, max_length=63, null=True)),
                ('ProjectCode', models.CharField(blank=True, max_length=63, null=True)),
                ('CompanyName', models.CharField(blank=True, max_length=63, null=True)),
                ('CompanyUndertakingWork', models.CharField(blank=True, max_length=63, null=True)),
                ('Location', models.CharField(blank=True, max_length=200, null=True)),
                ('Cost_NotIncludingKDV', models.FloatField(blank=True, null=True)),
                ('AC_Power', models.IntegerField(blank=True, null=True)),
                ('DC_Power', models.IntegerField(blank=True, null=True)),
                ('CalculatedCost_NotIncludingKDV', models.FloatField(blank=True, null=True)),
                ('RealizedCost_NotIncludingKDV', models.FloatField(blank=True, null=True)),
                ('CalculatedProfit_Loss', models.FloatField(blank=True, null=True)),
                ('RealizedProfit_Loss', models.FloatField(blank=True, null=True)),
                ('CalculatedProfitRate', models.FloatField(blank=True, null=True)),
                ('RealizedProfitRate', models.FloatField(blank=True, null=True)),
                ('Situation', models.CharField(default='Onay Bekliyor', max_length=63)),
                ('StartDate', models.DateField(default=django.utils.timezone.now)),
                ('FinishDate', models.DateField(default=django.utils.timezone.now)),
                ('KDV_Rate', models.FloatField(blank=True, default=20, null=True)),
                ('Terrain_Roof', models.CharField(blank=True, max_length=63, null=True)),
                ('Incentive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectName', models.CharField(max_length=63)),
                ('ProjectCode', models.CharField(blank=True, max_length=63, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Situations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Situation', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyName_Supplier', models.CharField(blank=True, max_length=63, null=True)),
                ('ContactPerson', models.CharField(blank=True, max_length=63, null=True)),
                ('PhoneNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('Email', models.CharField(blank=True, max_length=63, null=True)),
                ('Location', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Terrain_Roof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Terrain_Roof', models.CharField(max_length=63)),
            ],
        ),
    ]
