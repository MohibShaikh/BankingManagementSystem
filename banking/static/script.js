document.getElementById('registrationForm').addEventListener('submit', handleSubmit);

function handleSubmit(e) {
  e.preventDefault();
  const firstName = document.getElementById('firstNameInput').value;
  const lastName = document.getElementById('lastNameInput').value;
  const contact = document.getElementById('contactInput').value;
  const nic = document.getElementById('nicInput').value;
  const dob = document.getElementById('dobInput').value;
  const gender = document.getElementById('genderSelect').value;
  const email = document.getElementById('emailInput').value;
  const password = document.getElementById('passwordInput').value;
  const role = document.getElementById('roleSelect').value;

  if (
    firstName !== '' &&
    lastName !== '' &&
    contact !== '' &&
    nic !== '' &&
    dob !== '' &&
    gender !== 'gender' &&
    email !== '' &&
    password !== '' &&
    role !== 'role'
  ) {
    if (password.length >= 8 && contact.length == 11 && nic.length == 13) {
      alert('Account created!');
      clearForm();
    } else {
      document.getElementById('passwordError').textContent =
        password.length < 8 ? 'Password should have at least 8 characters' : '';
      document.getElementById('contacterror').textContent =
        contact.length !== 11 ? 'Contact should be 11 digits' : '';
      document.getElementById('nicerror').textContent =
        nic.length !== 13 ? 'NIC should be 13 digits long' : '';
      document.getElementById('emailerror').textContent =
        !email.includes('@') || !email.includes('.com') ? 'Invalid email address' : '';
    }
  } else {
    alert('Please fill in all the required fields.');
  }
}

function clearForm() {
  document.getElementById('firstNameInput').value = '';
  document.getElementById('lastNameInput').value = '';
  document.getElementById('contactInput').value = '';
  document.getElementById('nicInput').value = '';
  document.getElementById('dobInput').value = '';
  document.getElementById('genderSelect').value = 'gender';
  document.getElementById('emailInput').value = '';
  document.getElementById('passwordInput').value = '';
  document.getElementById('contacterror').textContent = '';
  document.getElementById('nicerror').textContent = '';
  document.getElementById('emailerror').textContent = '';
  document.getElementById('passwordError').textContent = '';
  document.getElementById('roleSelect').value = 'role';
}
