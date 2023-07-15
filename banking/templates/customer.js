const checkButton = document.querySelector('#checkButton');
const applyButton = document.querySelector('#applyButton');
const submitButton = document.querySelector('#submitButton');

checkButton.addEventListener('click', function() {
  window.location.href = '/transaction-record/';
});

applyButton.addEventListener('click', function() {
  window.location.href = '/loan-service/';
});

submitButton.addEventListener('click', function() {
  window.location.href = '/feedback/';
});


window.addEventListener('DOMContentLoaded', () => {
    const table = document.querySelector('table');
    const rows = table.querySelectorAll('tr');

    rows.forEach(row => {
      const column1 = row.querySelector('.col1');
      const column2 = column1.nextElementSibling;

      if (column1.textContent === 'CUSTOMER ID') {
        column2.textContent = '{{ customer.cust_id }}';
      } else if (column1.textContent === 'ACCOUNT HOLDER') {
        column2.textContent = '{{ customer.cust_name }}';
      } else if (column1.textContent === 'ACCOUNT ID') {
        column2.textContent = '{{ customer.acc_id }}';
      } else if (column1.textContent === 'ACCOUNT TYPE') {
        column2.textContent = '{{ customer.acc_type }}';
      } else if (column1.textContent === 'SAVINGS') {
        column2.textContent = '{{ customer.savings }}';
      } else if (column1.textContent === 'ACCESS DATE') {
        column2.textContent = '{{ customer.access_date }}';
      } else if (column1.textContent === 'OPENING DATE') {
        column2.textContent = '{{ customer.opening_date }}';
      } else if (column1.textContent === 'LOAN BALANCE') {
        column2.textContent = '{{ customer.loan_balance }}';
      }
    });
});
