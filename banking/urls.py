from django.urls import path
from .views import *

app_name = 'bms'

urlpatterns = [
    path('', login_view, name='login'),
    path('transaction_record/', transaction_record, name='transaction_record'),
    path('loan_application/', loan_application, name='loan_application'),
    path('feedback/', feedback_view, name='feedback'),
    path('submit-feedback/', submit_feedback_view, name='submit_feedback'),
    path('register-customer/', register_customer, name='register_customer'),
    path('customer/', customer, name='customer'),
    path('emp/', emp, name='emp'),
    # Remove or modify the 'manager/' URL pattern as needed
]
