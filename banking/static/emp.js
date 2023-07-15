// Dummy employee data
const employee = {
    name: "John Doe",
    position: "Bank Employee",
    workingHours: {
      startTime: "08:00 AM",
      endTime: "05:00 PM",
      totalHours: "8 hours"
    }
  };
  
  // Function to display employee details
  function displayEmployeeDetails() {
    const nameElement = document.getElementById("employeeName");
    const positionElement = document.getElementById("employeePosition");
    const startTimeElement = document.getElementById("startTime");
    const endTimeElement = document.getElementById("endTime");
    const totalHoursElement = document.getElementById("totalHours");
  
    // Update the DOM with employee data
    nameElement.textContent = employee.name;
    positionElement.textContent = employee.position;
    startTimeElement.textContent = employee.workingHours.startTime;
    endTimeElement.textContent = employee.workingHours.endTime;
    totalHoursElement.textContent = employee.workingHours.totalHours;
  }
  
  // Function to update the clock
  function updateClock() {
    const clockElement = document.getElementById("clock");
    const currentTime = new Date().toLocaleTimeString();
    clockElement.textContent = currentTime;
  }
  
  // Function to handle form submission
  function handleSubmit(event) {
    event.preventDefault();
    // Perform form submission logic
    console.log("Form submitted!");
  }
  
  // Display employee details
  displayEmployeeDetails();
  
  // Update clock every second
  setInterval(updateClock, 1000);
  
  // Event listener for form submission
  const form = document.getElementById("transactionForm");
  form.addEventListener("submit", handleSubmit);
  