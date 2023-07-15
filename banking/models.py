# Create your models here.
from django.db import models


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=50)
    designation = models.ForeignKey('Designation', on_delete=models.CASCADE)

    def __str__(self):
        return self.staff_name


class Designation(models.Model):
    designation = models.CharField(primary_key=True, max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    dept_id = models.ForeignKey('Department', on_delete=models.CASCADE)
    hire_date = models.DateField(auto_now_add=True)


class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)


class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=100)
    CNIC = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    email = models.EmailField()
    birth_date = models.DateField()

    def __str__(self):
        return self.cust_name

    def __str__(self):
        return self.cust_name
    # acc_id = models.ForeignKey('Account', on_delete=models.CASCADE)


class Account(models.Model):
    acc_id = models.AutoField(primary_key=True)
    open_date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=50)
    acc_balance = models.DecimalField(max_digits=10, decimal_places=2)
    loan_balance = models.DecimalField(max_digits=10, decimal_places=2)
    customers = models.ForeignKey('Customer', on_delete=models.CASCADE, default=None)

    def __str__(self):
        self.name = str(self.customers) + ' (' + str(self.type) + ')'
        return self.name


class Transaction(models.Model):
    acc_id = models.ForeignKey('Account', on_delete=models.CASCADE)
    transac_no = models.IntegerField()
    transac_type = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    emp_id = models.ForeignKey('Employee', on_delete=models.CASCADE)


class Loan(models.Model):
    loan_id = models.IntegerField(primary_key=True)
    cust_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
    acc_id = models.ForeignKey('Account', on_delete=models.CASCADE)
    manager_id = models.ForeignKey('Manager', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='pending')
    date = models.DateField(auto_now_add=True)


class Payment(models.Model):
    loan_id = models.ForeignKey('Loan', on_delete=models.CASCADE)
    pay_no = models.IntegerField()
    emp_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)


class Feedback(models.Model):
    cust_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
    feed_no = models.IntegerField()
    concerns = models.CharField(max_length=100)
    suggestions = models.CharField(max_length=100)
    ratings = models.IntegerField(choices=zip(range(1, 11), range(1, 11)))


class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    manager_id = models.ForeignKey('Manager', on_delete=models.CASCADE)
    dept_name = models.CharField(max_length=50)
    no_of_emp = models.IntegerField()

    def __str__(self):
        return self.dept_name


class ServiceEvaluation(models.Model):
    cust_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
    feed_no = models.ForeignKey('Feedback', on_delete=models.CASCADE)
    manager_id = models.ForeignKey('Manager', on_delete=models.CASCADE)
    RELATION_STATUS_CHOICES = [
        ('satisfactory', 'Satisfactory'),
        ('good', 'Good'),
        ('best', 'Best'), ]


class Portals(models.Model):
    manager_id = models.OneToOneField(Manager, on_delete=models.CASCADE, related_name='portal', null=True, blank=True)
    emp_id = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='portal', null=True, blank=True)
    cust_id = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='portal', null=True, blank=True)
    pwd = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        # Determine the related model based on which field is not None
        if self.cust_id:
            related_model = self.cust_id
        elif self.emp_id:
            related_model = self.emp_id
        elif self.manager_id:
            related_model = self.manager_id
        else:
            raise ValueError("No related model found for Portals object.")

        # Set the portal attribute of the related model to self
        setattr(related_model, 'portal', self)

        # Save the Portals object
        super().save(*args, **kwargs)
