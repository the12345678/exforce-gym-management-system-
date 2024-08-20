var formData = [];


// Example usage:




// Form validation function
function validateForm() {
  // Get the form inputs
  
  var member_name = document.getElementById("form_name");
  var membernameinput=member_name.value;

//console.log(membernameinput);
 
  if (membernameinput === "") {
    showDialog(member_name,"Please enter your name.");
    console.log("member",membernameinput);
    return false;
  }
  if (!memberNamePattern.test(membernameinput)) {
    //alert("hellow world");
    showDialog(member_name, "Invalid username. Please enter a valid username.");
    return false;
  }
  
  var formDataObject = {
    membername: membernameinput,
    address1: address1input,
    address2: address2input,
    dob:formattedDate,
    gender:selectedGender,
    email:emailinput,
    phone_no: phonenuminput,
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

  //alert("Form submitted successfully!");*/
   // Return true if all validations pass


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

  removeDialogBox();
});

document.querySelector('button[name="submit"]').addEventListener("click", function(event) {
  event.preventDefault(); // Prevent default button behavior
  removeDialogBox();
  if (validateForm()) {   
    
    
     alert("Form submitted successfully!");
    }
  });
  removeDialogBox();
 

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
          for (var pair of formData.entries()) {
            console.log(pair[0] + ": " + pair[1]);
          }
          // Optionally, you can redirect to another page or perform any other action
        })
        .catch(error => {
          // Handle any errors
          console.error('Error:', error);
        });
    }
    