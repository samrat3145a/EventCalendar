from django.db import models


class RegistrationData(models.Model):
    regulator = models.CharField(max_length=100)
    financial_year = models.CharField(max_length=100)
    assessment_year = models.CharField(max_length=100)
    period_from = models.DateField()
    period_to = models.DateField()
    form_return = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    date_of_entry = models.DateField(auto_now=True)
    type_of_tax_payer = models.CharField(max_length=100)
    actual_due_date = models.DateField()
    Description = models.CharField(max_length=100)
    due_date_1 = models.CharField(max_length=100, default='-', null=True)
    due_date_1_remarks = models.CharField(max_length=100, default='-', null=True)
    due_date_2 = models.CharField(max_length=100, default='-', null=True)
    due_date_2_remarks = models.CharField(max_length=100, default='-', null=True)
    due_date_3 = models.CharField(max_length=100, default='-', null=True)
    due_date_3_remarks = models.CharField(max_length=100, default='-', null=True)
    due_date_4 = models.CharField(max_length=100, default='-', null=True)
    due_date_4_remarks = models.CharField(max_length=100, default='-', null=True)
    due_date_5 = models.CharField(max_length=100, default='-', null=True)
    due_date_5_remarks = models.CharField(max_length=100, default='-', null=True)
    latest_due_date =models.CharField(max_length=100)

    class Meta:
        db_table = "Task Master"


class regulator_master(models.Model):
    regulator = models.CharField(unique=True, max_length=100)
    color_palette = models.CharField(max_length=100)

    class Meta:
        db_table = "Regulator Master"


class frequency_master(models.Model):
    frequency = models.CharField(unique=True, max_length=100)

    class Meta:
        db_table = "Frequency Master"


class tax_master(models.Model):
    tax_payer = models.CharField(unique=True, max_length=100)

    class Meta:
        db_table = "Tax Master"


class form_return_master(models.Model):
    form_return = models.CharField(unique=True, max_length=100)

    class Meta:
        db_table = "Form/Return Master"



class SignupData(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    qualification = models.CharField(max_length=20)

    class Meta:
        db_table = "Signup Data"