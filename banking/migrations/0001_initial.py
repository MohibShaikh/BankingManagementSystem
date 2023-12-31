# Generated by Django 4.2.3 on 2023-07-13 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('acc_id', models.AutoField(primary_key=True, serialize=False)),
                ('open_date', models.DateField(auto_now_add=True)),
                ('type', models.CharField(max_length=50)),
                ('acc_balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('loan_balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cust_id', models.AutoField(primary_key=True, serialize=False)),
                ('cust_name', models.CharField(max_length=100)),
                ('CNIC', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.AutoField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=50)),
                ('no_of_emp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('designation', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('hire_date', models.DateField(auto_now_add=True)),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banking.department')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_no', models.IntegerField()),
                ('concerns', models.CharField(max_length=100)),
                ('suggestions', models.CharField(max_length=100)),
                ('ratings', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banking.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('loan_id', models.IntegerField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('acc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banking.account')),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banking.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('manager_id', models.AutoField(primary_key=True, serialize=False)),
                ('position', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transac_no', models.IntegerField()),
                ('transac_type', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('acc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banking.account')),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banking.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=50)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banking.designation')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banking.customer')),
                ('feed_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banking.feedback')),
                ('manager_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banking.manager')),
            ],
        ),
        migrations.CreateModel(
            name='Portals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pwd', models.CharField(max_length=128)),
                ('cust_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portal', to='banking.customer')),
                ('emp_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portal', to='banking.employee')),
                ('manager_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portal', to='banking.manager')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_no', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banking.employee')),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banking.loan')),
            ],
        ),
        migrations.AddField(
            model_name='manager',
            name='staff',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='banking.staff'),
        ),
        migrations.AddField(
            model_name='loan',
            name='manager_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banking.manager'),
        ),
        migrations.AddField(
            model_name='employee',
            name='staff',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='banking.staff'),
        ),
        migrations.AddField(
            model_name='department',
            name='manager_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banking.manager'),
        ),
        migrations.AddField(
            model_name='account',
            name='customers',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='banking.customer'),
        ),
    ]
