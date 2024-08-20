var formData=[];

var gymMemberUserID;
var gymMemberPassword;
var coachUserID;
var coachPassword;
var adminUserID;
var adminPassword;
var externalMemberUserID;
var externalMemberPassword;

// Function to validate Gym Member user ID
function validateGymMemberUserID(userID) {
  var regex = /^[a-z]{3}\d{4}$/i;
  return regex.test(userID);
}

// Function to validate Coach user ID
function validateCoachUserID(userID) {
  var regex = /^[a-z][a-z]{2}\d{3}$/i;
  return regex.test(userID);
}

// Function to validate Administrator user ID
function validateAdminUserID(userID) {
  var regex = /^[a-z][a-z]{2}\d{3}$/i;
  return regex.test(userID);
}

// Function to validate External Registered Member user ID
function validateExternalMemberUserID(userID) {
  var regex = /^[A-Z]{3}\d{4}$/;
  return regex.test(userID);
}

function create_password(userID) {
  // Define the password patterns for each user type
  var gymMemberPattern = /[^a-z0-9]/gi;
  var coachPattern = /[!@#$%^&*]/gi;
  var adminPattern = /[!@#$%^&*]/gi;
  var externalMemberPattern = /[!@#$%^&*]/gi;

  // Generate a random password based on the user ID pattern
  if (validateGymMemberUserID(userID)) {
    // Gym Member password
    return generateRandomPassword(gymMemberPattern);
  } else if (validateCoachUserID(userID)) {
    // Coach password
    return generateRandomPassword(coachPattern);
  } else if (validateAdminUserID(userID)) {
    // Administrator password
    return generateRandomPassword(adminPattern);
  } else if (validateExternalMemberUserID(userID)) {
    // External Registered Member password
    return generateRandomPassword(externalMemberPattern);
  } else {
    return "its me";
  }
}

// Function to generate a random password based on a given pattern
function generateRandomPassword(pattern) {
  var password = "";
  var characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";
  
  for (var i = 0; i < pattern.length; i++) {
    if (pattern[i] === "[") {
      var char = characters.charAt(Math.floor(Math.random() * characters.length));
      password += char;
    } else {
      password += pattern[i];
    }
  }
  
  return password;
}

// Function to handle button click event
function handleButtonClick() {
  var IDfield = document.getElementById('user_id');
  var userID = IDfield.value;
  console.log("vur");
  if (validateGymMemberUserID(userID)) {
    // Valid Gym Member user ID
    console.log('Gym Member user ID is valid');
    
     gymMemberUserID = userID;
     gymMemberPassword = create_password(gymMemberUserID);
    console.log('Gym Member Password:', gymMemberPassword);
    // Perform further actions for Gym Member user ID
  } else if (validateCoachUserID(userID)) {
    // Valid Coach user ID
    console.log('Coach user ID is valid');
     coachUserID = userID;
     coachPassword = create_password(coachUserID);
    console.log('Coach Password:', coachPassword);
    // Perform further actions for Coach user ID
  } else if (validateAdminUserID(userID)) {
    // Valid Administrator user ID
    console.log('Administrator user ID is valid');
    adminUserID = userID;
     adminPassword = create_password(adminUserID);
    console.log('Administrator Password:', adminPassword);
    // Perform further actions for Administrator user ID
  } else if (validateExternalMemberUserID(userID)) {
    // Valid External Registered Member user ID
    console.log('External Registered Member user ID is valid');
    externalMemberUserID = userID;
    externalMemberPassword = create_password(externalMemberUserID);
    console.log('External Registered Member Password:', externalMemberPassword);
    // Perform further actions for External Registered Member user ID
  } else {
    // Invalid user ID
    console.log("come here");
    showDialog(IDfield, 'Invalid user ID');
    console.log("comehere too");
  }
  removeDialogBox();

  var formDataObject = {
    gymMemberUserID:gymMemberUserID,
    gymMemberPassword:gymMemberPassword,
    coachUserID:coachUserID,
    coachPassword:coachPassword,
    adminUserID:adminUserID,
    adminPassword:adminPassword,
    externalMemberUserID:externalMemberPassword,
    externalMemberPassword:externalMemberPassword,
  };

  // Add the form data object to the array
  formData.push(formDataObject);

  // Display form data
  console.log('Form Data:', formData);

  // Send form data to Django using HTTP API method
  sendDataToDjango(formData);

}


function showDialog(element, message) { 
  console.log("come heree too"); 
  var errorContainer = document.createElement("div");
  errorContainer.className = "dialog-box";
  errorContainer.textContent = message;
 console.log(message);
  element.classList.add("invalid-input");

  //element.parentNode.insertBefore(errorContainer, element.nextSibling);
// Create a wrapper element for the error message
var errorWrapper = document.createElement("div");
errorWrapper.className = "error-wrapper";
errorWrapper.appendChild(errorContainer);
console.log("here");
// Insert the error wrapper after the input field
element.parentNode.insertBefore(errorWrapper, element.nextSibling);

  element.focus();
  element.scrollIntoView({ behavior: "smooth", block: "start" });

  // Remove the error message when clicking on the input field
  element.addEventListener("click", function() {
    removeDialogBox();
   });
 
   
}

  


function removeDialogBox() {
  var errorContainer = document.querySelector(".dialog-box");
  var inputElement = document.querySelector(".invalid-input");
  if (errorContainer && inputElement) {
    errorContainer.remove();
    inputElement.classList.remove("invalid-input");
  }
}

function sendDataToDjango(formData) {
  // Convert form data to JSON string
  var jsonData = JSON.stringify(formData);

  // Send the form data to the Django backend
  fetch("http://localhost:8000/registration/data/", {
    method: "POST",
    body: jsonData,
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then(response => response.json())
    .then(data => {
      // Handle the response from the Django backend
      console.log("Form Data:", formData);
      // Optionally, you can redirect to another page or perform any other action
    })
    .catch(error => {
      // Handle any errors
      console.error('Error:', error);
    });
}

