# Generated by Django 4.2.7 on 2023-11-25 13:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AFM", "0009_alter_expenses_projectname_expenses"),
    ]

    operations = [
        migrations.AddField(
            model_name="incomes",
            name="ProjectName_Incomes_Copy",
            field=models.CharField(blank=True, max_length=63, null=True),
        ),
        migrations.AddField(
            model_name="jobhistory",
            name="ProjectName_JobHistory_Copy",
            field=models.CharField(blank=True, max_length=63, null=True),
        ),
    ]
