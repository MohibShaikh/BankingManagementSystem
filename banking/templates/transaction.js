//// Function to fetch the transactions for the logged-in customer
//function fetchTransactions() {
//    // Make an AJAX request to the server-side endpoint
//    fetch('/api/customer/transactions')
//        .then(response => response.json())
//        .then(data => {
//            // Process and display the retrieved data
//            populateTransactionTable(data);
//        })
//        .catch(error => {
//            console.error('Error:', error);
//        });
//}
//
//// Function to populate the transaction table with data
//function populateTransactionTable(transactions) {
//    // Get the transaction table body element
//    const transactionBody = document.getElementById('transactionBody');
//
//    // Clear any existing rows in the table
//    transactionBody.innerHTML = '';
//
//    // Iterate over the transactions and create table rows
//    transactions.forEach(transaction => {
//        // Create a new table row
//        const row = document.createElement('tr');
//
//        // Create table cells for each data field
//        const transactype = document.createElement('td');
//        transactype.textContent = transaction.type;
//        row.appendChild(transactype);
//
//        const dateCell = document.createElement('td');
//        dateCell.textContent = transaction.date;
//        row.appendChild(dateCell);
//
//        const amountCell = document.createElement('td');
//        amountCell.textContent = transaction.amount.toFixed(2);
//        row.appendChild(amountCell);
//
//        const recipientCell = document.createElement('td');
//        recipientCell.textContent = transaction.recipient;
//        row.appendChild(recipientCell);
//
//        // Append the row to the table body
//        transactionBody.appendChild(row);
//    });
//}
//
//// Call the function to fetch and populate the transaction table on page load
//document.addEventListener('DOMContentLoaded', () => {
//    fetchTransactions();
//});
