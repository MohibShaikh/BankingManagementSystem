document.getElementById('loginForm').addEventListener('submit', handleLogin);

function handleLogin(e) {
  e.preventDefault();
  const email = document.getElementById('emailInput').value;
  const password = document.getElementById('passwordInput').value;
  const role = document.getElementById('roleSelect').value;

  if (email && password) {
    // Perform login authentication here
    if (role == "employee"){
      alert('Login successful!');
      clearForm();
      window.location.href = 'employcash.html';
    }
    else if (role == 'client'){
      alert('Login successful!');
      clearForm();
      window.location.href = 'customer.html';
    }
    // alert('Login successful!');
    // clearForm();
  } else {
    alert('Please fill in all the required fields.');
  }
}

function clearForm() {
  document.getElementById('emailInput').value = '';
  document.getElementById('passwordInput').value = '';
  document.getElementById('roleSelect').value = 'role';
}
