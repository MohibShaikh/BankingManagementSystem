const form = document.getElementById('loginForm')

form.addEventListener('submit', function(event) {
  event.preventDefault(); 
  const ratings = document.querySelector('input[type="range"]').value;
  const concerns = document.querySelector('textarea[name="concerns"]').value;
  const suggestions = document.querySelector('textarea[name="suggestions"]').value;

  localStorage.setItem('ratings', ratings);
  localStorage.setItem('concerns', concerns);
  localStorage.setItem('suggestions', suggestions);

  var tableHTML = "<h4>THANKS FOR YOUR RESPONSE !</h4>"

  confirmationTable.innerHTML = tableHTML;
  
  confirmationModal.style.display = 'flex';

  okButton.addEventListener('click', function() {
    confirmationModal.style.display = 'none';
    window.location.href = 'customer.html';
  });
});
