var formData = [];
const memberNamePattern = /^[A-Z][a-z]+\s[a-z][a-z]+$/;

const member_id_pattern = /^[a-zA-Z]{3}\d{4}\d+$/;

const phoneNumberPattern = /^(07|011)\d{8}$/;

  const addressPattern = /^[A-Za-z0-9\s,]+$/;

  const emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

  const non_negative_num_pattern = /^\d+$/;


// Form validation function
function validateForm() {
  // Get the form inputs
  
  var user_id = document.getElementById("user_id");
  var user_idinput=user_id.value;

//console.log(membernameinput);
  var password = document.getElementById("password");
  var passwordinput = password.value;
  var password_re = document.getElementById("re_password");
  var password_reinput = password_re.value;
  
  // Perform validation for each input field
 /* if (membernameinput === "") {
    showDialog(member_name,"Please enter your name.");
    console.log("member",membernameinput);
    return false;
  }
  if (!memberNamePattern.test(membernameinput)) {
    //alert("hellow world");
    showDialog(member_name, "Invalid username. Please enter a valid username.");
    return false;
  }
  if (address1input === "") {
    showDialog(address1,"Please enter your address.");
    return false;
  }
  if (!addressPattern.test(address1input) || address1input.length > 20 || /\s{2,}/.test(address1input)) {
    showDialog(address1, "Invalid address. Please provide a valid address.");
    return;
  }
  if (address2input === "") {
    showDialog(address2,"Please enter your address.");
    return false;
  }
  if (!addressPattern.test(address2input) || address2input.length > 20 || /\s{2,}/.test(address2input)) {
    showDialog(address2, "Invalid address. Please provide a valid address.");
    return;
  }

  
  /*if (!selectedCoach) {
    showDialog(coach, "Please select a coach.");
    return false;
  }

  if (!selectedPurpose) {
    showDialog(purpose, "Please select a purpose.");
    return false;
  }

  if (!imageFile) {
    showDialog(image, "Please upload an image.");
    return false;
  }
  */ var formDataObject = {
    User_id: user_idinput,
    password: passwordinput,
   
     };

  // Add the form data object to the array
  formData.push(formDataObject);

  // Display form data
  console.log('Form Data:', formData);

  // Send form data to Django using HTTP API method
  sendDataToDjango(formData);

  // Reset form fields
 
  return true;
}

 

function showDialog(element, message) {  
  var errorContainer = document.createElement("div");
  errorContainer.className = "dialog-box";
  errorContainer.textContent = message;

  element.classList.add("invalid-input");

  //element.parentNode.insertBefore(errorContainer, element.nextSibling);
// Create a wrapper element for the error message
var errorWrapper = document.createElement("div");
errorWrapper.className = "error-wrapper";
errorWrapper.appendChild(errorContainer);

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







//Refresh button click handler
document.querySelector('button[name="refresh"]').addEventListener("click", function() {
  event.preventDefault();
  // Prevent default button behavior
  document.getElementById("reg_form").reset(); // Reset the form

  //removeDialogBox();
});

document.querySelector('button[name="submit"]').addEventListener("click", function(event) {
  event.preventDefault(); // Prevent default button behavior
 // removeDialogBox();
  if (validateForm()) {   
   
    
     alert("Form submitted successfully!");
    }
  });

    // Get the form data
    
    
    // Get the image file
    //var imagedata = formData.get("image");
    // Append the image file to the FormData if it exists
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
          console.log("Form Data:");
        
          // Optionally, you can redirect to another page or perform any other action
        })
        .catch(error => {
          // Handle any errors
          console.error('Error:', error);
        });
    }
    