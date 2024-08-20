var formData = [];

const supplementNamePattern = /^[A-Za-z0-9\s\-.,()'&]+$/;
const brandNamePattern = /^[A-Za-z0-9\s\-.,()'"&!@#$%^*+=:_;<>/?[\]{}|\\]+$/;
const descriptionPattern = /^[A-Za-z0-9\s.,!?()'"-]{1,500}$/;
const non_negative_num_pattern = /^\d+$/;
const decimalNumberPattern = /^[-+]?[0-9]+(\.[0-9]+)?$/;



// Form validation function
function validateForm() {
  // Get the form inputs
  
 
//console.log(membernameinput);
  var supplement_name = document.getElementById("name");
  var supplement_nameinput = supplement_name.value;
  var brand = document.getElementById("brand");
  var brandinput = brand.value;
  var stock= document.getElementById("stock");
  var stockinput = stock.value;

  var supplement_rate = document.getElementById("rate");
  var unitprice = supplement_rate.value;

  var quantity=document.getElementById("quantity");
  var amount=quantity.value;

 

  var description=document.getElementById("message");
  descript_detail=description.value;



  // Perform validation for each input field
 /* if (supplement_nameinput === "") {
    showDialog(supplement_name,"Please enter a name.");
    console.log("member",membernameinput);
    return false;
  }
  if (!supplementNamePattern.test(membernameinput)) {
    //alert("hellow world");
    showDialog(supplement_name, "Invalid name. Please enter a valid username.");
    return false;
  }
  if (brandinput === "") {
    showDialog(brand,"Please enter a brandname.");
    return false;
  }
  if (!brandNamePattern.test(brandinput)) {
    showDialog(brand, "Invalid brand name. Please provide a valid brandname.");
    return;
  }
  if (stockinput === "") {
    showDialog(stock,"Please enter a number.");
    return false;
  }
  if (!non_negative_num_pattern.test(stockinput)) {
    showDialog(stock, "Invalid number. Please provide a valid number.");
    return;
  }

  if (selectedDate="") {
    showDialog(datefield, "Please select a date of birth.");
    return false;
  }

  // Validate Gender
  
  if (unitprice === "") {
    showDialog(supplement_rate,"Please enter a price value .");
    return false;
  }
  if (!decimalNumberPattern.test(unitprice)) {
    showDialog(supplement_rate, "Invalid price value. Please enter a valid price value.");
    return false;
  }


  if (descript_detail === "") {
    showDialog(description,"Please enter a text");
    return false;
  }
  if (!phoneNumberPattern.test(phonenuminput)) {
    showDialog(phone_num, "Invalid text. Please enter a valid text.");
    return false;
  }*/
 var formDataObject = {
   
    supplement_name: supplement_nameinput,
    Brand: brandinput,
    stock:stockinput,
    Unit_price:unitprice,
    amount:amount,
    description:descript_detail
     };

  // Add the form data object to the array
  formData.push(formDataObject);

  // Display form data
  console.log('Form Data:', formData);

  // Send form data to Django using HTTP API method
  sendDataToDjango(formData);

  // Reset form fields
  document.getElementById("reg_form").reset();
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

  if (validateForm()) {   
   
     alert("Form submitted successfully!");
    }
  });

    // Get the form data
    const updateButton = document.querySelector('.update-btn');
  updateButton.addEventListener('click', function() {
    // Perform the action you want when the "update" button is clicked
    var supplement_name = document.getElementById("name");
    var supplement_nameinput = supplement_name.value;
    var brand = document.getElementById("brand");
    var brandinput = brand.value;
    var stock= document.getElementById("stock");
    var stockinput = stock.value;
  
     const formDataObject={
    supplement_name: supplement_nameinput,
    Brand: brandinput,
    stock:stockinput,
     };    
    

     const formData=[];
     formData.push(formDataObject);

     sendDataToDjango(formData);
     alert("data updated successfully");

  });
    
    
  function sendDataToDjango(formData) {
    // Convert form data to JSON string
    var jsonData = JSON.stringify(formData);
    var attributeCount = Object.keys(formData[0]).length;
    console.log(attributeCount);
    // Send the form data to the Django backend
    if(attributeCount===6){
    fetch("http://localhost:8000/supplement/product/data/", {
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
  else{
        fetch("http://localhost:8000/supplement/update/product/data/", {
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
      
  } } 
    