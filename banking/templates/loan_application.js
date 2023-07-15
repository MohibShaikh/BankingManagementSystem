document.addEventListener('DOMContentLoaded', function() {
    var loanForm = document.getElementById('loanForm');
    var confirmationModal = document.getElementById('confirmationModal');
    var confirmationTable = document.getElementById('confirmationTable');
    var okButton = document.getElementById('okButton');
  
    loanForm.addEventListener('submit', function(event) {
      event.preventDefault();

      var customerID = document.getElementById('customerid').value;
      var accountID = document.getElementById('accountid').value;
      var loanAmount = document.getElementById('amount').value;
      var guarantor = document.getElementById('guarantor').value;
      var purpose = document.getElementById('purpose').value;
      var duration = document.getElementById('duration').value;
  
      // Construct the confirmation table
      if (customerID.length ==10 && accountID.length == 10 && guarantor.length == 10) {
      var tableHTML =
        '<tr><td colspan="2">The process may take approximately 30 days.</td></tr>'+
        '<tr><td colspan="2"><hr>   </td></tr>'+        
        '<tr><td class="col1">Customer ID:</td><td>' + customerID + '</td></tr>' +
        '<tr><td class="col1">Account ID:</td><td>' + accountID + '</td></tr>' +
        '<tr><td class="col1">Loan Amount:</td><td>' + loanAmount + '</td></tr>' +
        '<tr><td class="col1">Guarantor:</td><td>' + guarantor + '</td></tr>';
  
      confirmationTable.innerHTML = tableHTML;
  
      confirmationModal.style.display = 'flex';
  
      okButton.addEventListener('click', function() {
        confirmationModal.style.display = 'none';
        window.location.href = 'customer.html';
      });
    }
    else{
      alert("INVALID INFORMATION");
    }
    });
  });
  