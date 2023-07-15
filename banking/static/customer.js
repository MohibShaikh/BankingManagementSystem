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
        column2.textContent = '111111111';
      } else if (column1.textContent === 'ACCOUNT HOLDER') {
        column2.textContent = 'John Doe';
      } else if (column1.textContent === 'ACCOUNT ID') {
        column2.textContent = '111111111';
      } else if (column1.textContent === 'ACCOUNT TYPE') {
        column2.textContent = 'Savings';
      } else if (column1.textContent === 'SAVINGS') {
        column2.textContent = '111111111';
      } else if (column1.textContent === 'ACCESS DATE') {
        column2.textContent = '111111111';
      } else if (column1.textContent === 'OPENING DATE') {
        column2.textContent = '111111111';
      } else if (column1.textContent === 'LOAN BALANCE') {
        column2.textContent = '0';
      }
    });
  });
