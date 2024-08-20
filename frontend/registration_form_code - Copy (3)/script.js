var formData = [];

function populateCoachSelect() {
  fetch("http://localhost:8000/registration/coach-ids/") // Assuming the backend endpoint is '/coach-names/' that returns the coach names
    .then(response => response.json())
    .then(data => {
      const selectElement = document.getElementById('form_coach');

      data.forEach(coachName => {
        const option = document.createElement('option');
        option.value = coachName;
        option.textContent = coachName;
        selectElement.appendChild(option);
      });
    })
    .catch(error => console.error(error));
}

// Call the function to populate the select element
populateCoachSelect();


var memberNamePattern = /^[A-Z][a-z]+\s[a-z][a-z]+$/;

//var userIdPattern = /^ex_\d{4}_\d{3}\*\*$/;
var phoneNumberPattern = /^(07|011)\d{8}$/;

  var addressPattern = /^[A-Za-z0-9\s,]+$/;

  var emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

 
// Example usage:




// Form validation function
function validateForm() {
  // Get the form inputs
  
  var member_name = document.getElementById("form_name");
  var membernameinput=member_name.value;

//console.log(membernameinput);
  var address1 = document.getElementById("form_address1");
  var address1input = address1.value;
  var address2 = document.getElementById("form_address2");
  var address2input = address2.value;
  var selectedDate= document.getElementById("datepicker").value;

  var formattedDate = moment(selectedDate, "DD/MM/YYYY").format("YYYY-MM-DD");
  console.log("Formatted date: " + formattedDate);

  //var dob = document.getElementById("form_dob");
 // var dobValue = dob.value;

  //var gender = document.querySelector('input[name="gender"]:checked');
  var genderInputs = document.querySelectorAll('input[name="gender"]');
  var selectedGender = "";
  for (var i = 0; i < genderInputs.length; i++) {
    if (genderInputs[0].checked) {
      selectedGender = "Male";
      break;
    }
    if (genderInputs[1].checked) {
      selectedGender = "Female";
      break;
    }

  }
  var email= document.getElementById("form_mail");
  var emailinput = email.value;

  var phone_num = document.getElementById("form_phone");
  var phonenuminput = phone_num.value;



  /*var coach = document.getElementById("form_coach");
  var selectedCoach = coach.value !== "";

  var purpose = document.getElementById("form_purpose");
  var selectedPurpose = purpose.value !== "";

  var image = document.getElementById("form_image");
  var imageFile = image.files[0];*/


  // Perform validation for each input field
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

  if (selectedDate="") {
    showDialog(dob, "Please select a date of birth.");
    return false;
  }

  // Validate Gender
  if (selectedGender==="") {
   // showDialog(genderInputs, "Please select a gender.");
   alert("please select a gender");
    return false;
  }
  if (emailinput === "") {
    showDialog(email,"Please enter your email address.");
    return false;
  }
  if (!emailPattern.test(emailinput)) {
    showDialog(email, "Invalid email address. Please enter a valid email address.");
    return false;
  }


  if (phonenuminput === "") {
    showDialog(phone_num,"Please enter your phone number.");
    return false;
  }
  if (!phoneNumberPattern.test(phonenuminput)) {
    showDialog(phone_num, "Invalid phone number. Please enter a valid phone number.");
    return false;
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

  if (validateForm()) {   
    removeDialogBox();
    
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
    