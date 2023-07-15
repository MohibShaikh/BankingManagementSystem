from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Portals, Manager, Employee, Customer, Feedback, Transaction

def emp(request):
    employee = Employee.objects.get(emp_id=request.session['emp_id'])

    if request.method == 'POST':
        customer_email = request.POST.get('customerEmail')
        transaction_type = request.POST.get('transac_type')
        amount = request.POST.get('amount')

        # Retrieve the customer based on the provided email
        try:
            customer = Customer.objects.get(email=customer_email)
        except Customer.DoesNotExist:
            # Handle case when customer does not exist
            return redirect('customer_not_found')

        # Create a new transaction
        transaction = Transaction(
            acc_id=employee.staff.acc_id,  # Assuming the employee is associated with a specific account
            transac_type=transaction_type,
            amount=amount,
            emp_id=employee,
            cust_id=customer
        )
        print(transaction.acc_id,transaction.amount,transaction.transac_type)
        transaction.save()

        # Redirect to a success page or perform other actions
        return redirect('success_page')

    return render(request, 'emp.html', {'employee': employee})

def login_view(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        logger_id = request.POST.get('email')
        password = request.POST.get('password')
        print(logger_id,password)

        try:
            portal = None
            if role == 'manager':
                portal = Portals.objects.get(manager_id__staff_id=logger_id)
            elif role == 'employee':
                portal = Portals.objects.get(emp_id__emp_id=logger_id)
            elif role == 'customer':
                portal = Portals.objects.get(cust_id__cust_id=logger_id)
            else:
                # Handle invalid role
                return render(request, 'login.html')

            if portal.pwd == password:
                # Login successful
                if role == 'customer':
                    request.session['cust_id'] = portal.cust_id.cust_id  # Store the cust_id in session
                    cus_tomer = Customer.objects.get(cust_id=portal.cust_id.cust_id)
                    return render(request, 'customer.html', {'cus_tomer': cus_tomer})
                elif role == 'employee':
                    request.session['emp_id'] = portal.emp_id.emp_id  # Store the emp_id in session
                    empdata = Employee.objects.get(emp_id=portal.emp_id.emp_id)
                    return render(request, 'emp.html', {'employee': empdata})
                elif role == 'manager':
                    request.session['manager_id'] = portal.manager_id.manager_id  # Store the manager_id in session
                    manag_er = Manager.objects.get(manager_id=portal.manager_id.manager_id)
                    return render(request, 'manager_dashboard.html', {'manager': manag_er})
            else:
                # Incorrect password
                print('Incorrect password')
                return render(request,'login.html')


        except Portals.DoesNotExist:
            if role == 'manager':
                try:
                    Manager.objects.get(staff_id=logger_id)
                    messages.error(request, f"Invalid password")
                except Manager.DoesNotExist:
                    messages.error(request, f"Manager with ID {logger_id} does not exist.")
            elif role == 'employee':
                try:
                    Employee.objects.get(emp_id=logger_id)
                    messages.error(request, f"Invalid password")
                except Employee.DoesNotExist:
                    messages.error(request, f"Employee with ID {logger_id} does not exist.")
            elif role == 'customer':
                try:
                    Customer.objects.get(cust_id=logger_id)
                    messages.error(request, f"Invalid password")
                except Customer.DoesNotExist:
                    messages.error(request, f"Customer with ID {logger_id} does not exist.")
            else:
                messages.error(request, f"Invalid credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')

@login_required
def transaction_record(request):
    if request.method == 'GET':
        cust_id = request.session.get('cust_id')  # Retrieve the cust_id from session
        customer = Customer.objects.filter(cust_id=cust_id).first()
        transactions = Transaction.objects.filter(acc_id__customers=customer)
        return render(request, 'transactions.html', {'customer': customer, 'transactions': transactions})
    else:
        return redirect('login')

def customer(request):
    return render(request,'customer')
@login_required
def loan_application(request):
    if request.method == 'GET':
        cust_id = request.session.get('cust_id')  # Retrieve the cust_id from session
        customer = Customer.objects.filter(cust_id=cust_id).first()
        return render(request, 'loan_application.html', {'customer': customer})
    else:
        return redirect('login')

@login_required
def feedback_view(request):
    if request.method == 'GET':
        cust_id = request.session.get('cust_id')  # Retrieve the cust_id from session
        customer = Customer.objects.filter(cust_id=cust_id).first()
        return render(request, 'feedback.html', {'customer': customer})
    else:
        return redirect('http:/127.0.0.1:8000/login')


def submit_feedback_view(request):
    if request.method == 'POST':
        cust_id = request.session.get('cust_id')  # Retrieve the cust_id from session
        customer = Customer.objects.filter(cust_id=cust_id).first()
        concerns = request.POST.get('concerns')
        suggestions = request.POST.get('suggestions')
        ratings = int(request.POST.get('ratings'))

        feedback = Feedback.objects.create(cust_id=customer, concerns=concerns, suggestions=suggestions,
                                           ratings=ratings)

        return redirect('customer')

    return redirect('submit_feedback')


def register_customer(request):
    if request.method == 'POST':
        cust_name = request.POST.get('cust_name')
        contact = request.POST.get('contact')
        CNIC = request.POST.get('CNIC')
        address = request.POST.get('address')
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = Customer.objects.create(cust_name=cust_name, contact=contact, CNIC=CNIC, address=address,
                                           email=email)

        # Retrieve the cust_id of the newly created customer
        cust_id = customer.cust_id

        portal = Portals.objects.create(cust_id=cust_id, pwd=password)

        return redirect('login')

    return render(request, 'index.html')
