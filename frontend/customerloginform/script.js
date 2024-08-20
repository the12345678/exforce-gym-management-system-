const form = document.getElementById('form');
const customerid = document.getElementById('username');

const password = document.getElementById('password');
const password2 = document.getElementById('password2');

form.addEventListener('submit', e => {
    e.preventDefault();

    validateInputs();
});

const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success')
}

const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
};

const isValiduserid= customerid => {
    const re = "^ex/user/\d{3}$";
    return re.test(String(customerid).toLowerCase());
}

const validateInputs = () => {
    const idValue = customerid.value;
    
    const passwordValue = password.value;
    const password2Value = password2.value;    

    const formData=[];
    const formDataobject={
        idValue:idValue

    }
formData.push(formDataobject);
const realpassword=sendDataToDjango(formData);
  

    if(useridValue === '') {
        setError(userid, 'Userid is required');
    } else {
        setSuccess(userid);
    }

    if (!isValiduserid(idValue)) {
        setError(userid, 'Provide a valid email address');
    } else {
        setSuccess(userid);
    }

    if(passwordValue === '') {
        setError(password, 'Password is required');
    }else if (passwordValue !== realpassword){
        setError(password, 'Password is not correct');
    }
    else {
        setSuccess(password);
    }

    if(password2Value === '') {
        setError(password2, 'Please confirm your password');
    } else if (password2Value !== realpassword) {
        setError(password2, "Passwords doesn't match");
    } else {
        setSuccess(password2);
    }

};


function sendDataToDjango(formData) {
    // Convert form data to JSON string
    var jsonData = JSON.stringify(formData);
  
    // Send the form data to the Django backend
    fetch("http://localhost:8000/user_login/get/customer/data/", {
      method: "POST",
      body: jsonData,
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then(response => response.json())
      .then(data => {
        // Handle the response from the Django backend
        console.log("Form Data:", data);
  
        // Check if the response contains the password
        if (data.password) {
          // Use the password returned from the backend
          var password = data.password;
          console.log("Password:", password);
          return password;

  
          // Optionally, you can redirect to another page or perform any other action
        } else {
          // Handle the case where the password is not found
          console.log("Password not found.");
        }
      })
      .catch(error => {
        // Handle any errors
        console.error('Error:', error);
      });
      
  }
  