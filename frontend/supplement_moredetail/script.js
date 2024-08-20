function redirectToPage(direction) {
  if (direction === 'welcome_page') {
    // Replace 'your_coach_registration_page_url' with the actual URL for coach registration page
    window.location.href = '../welcomepage/landing_page.html';
  } 
}


var num=0;
var amount=0;
var data =[];
var formData=[];
var formDataObject={};

const modal = document.getElementById('customMessageBox');
const messageText = document.getElementById('messageText');
const btnOK = document.getElementById('btnOK');
const btnClose = document.getElementById('btnClose');

function updatecarddetails() {
    fetch('http://127.0.0.1:8000/supplement/get/product_data/')
        .then(response => response.json())
        .then(data => {
            console.log("yes");
            const card_content = document.querySelectorAll('.card-content');
            console.log("success");
            
            const secondObjectData = data.second_object;

            // Ensure firstObjectData and secondObjectData are arrays before iterating
            if (Array.isArray(secondObjectData)) {
                // Update the content of each card content box
                card_content.forEach((box, index) => {
                    const data1 = box.querySelector('.access1');
                    const data2 = box.querySelector('.access2');
                    const data3 = box.querySelector('.access3');
                    const data4 = box.querySelector('.access4');
                    const data5 =box.querySelector('access5');

                    // Update the content of each data element in the box
                    data1.textContent = secondObjectData[index].name;
                    data2.textContent = secondObjectData[index].quantity_perunit;
                    data3.textContent = secondObjectData[index].unit_price_Rs;
                    data4.textContent = secondObjectData[index].stock;
                    data5.textcontent= firstObjectData[index].valid_booking_period;
                });
            } else {
                console.error('Data format is not as expected');
            }
        })
        .catch(error => console.error('Error fetching coach data:', error));
}

window.onload = updatecarddetails;

function get_userinput(num){
   
const prices = document.getElementsByClassName('access3');
const stocks = document.getElementsByClassName('access4');

console.log(prices);
console.log("number:",num);
console.log(typeof num);
switch (num) {
    case 1:
      console.log("come")
      data[0]=prices[0].textContent;
      console.log("data:",data[0]);
      data[1]=stocks[0].textContent;
    break;

    case 2:
        data[0]=prices[1].textContent;
        data[1]=stocks[1].textContent;
      break;

    case 3:
        data[0]=prices[2].textContent;
        data[1]=stocks[2].textContent;
      break;

    case 4:
        data[0]=prices[3].textContent;
        data[1]=stocks[3].textContent;
      break;

    default:
        break;
}
return data;
}

function bookingtransaction_processing(num) {

   
   amount=+document.getElementById("amount").value;

    const data=get_userinput(num);

    if(amount<=data[1]-5){
    message="your total cart("+amount+") price is Rs."+data[0]*amount;
    return message
  }

    else{
       message="sorry.stock available("+(data[1]-5)+")  is not enough for your booking";
      return message;
    }
  }

  function displayMessageBox(message) {
    messageText.innerHTML = message; // Set the innerHTML of the <p> element
    modal.style.display = 'block';
  }
  
  // Function to hide the custom message box
  function hideMessageBox() {
    modal.style.display = 'none';
  }

  document.querySelector('button[name="cart"]').addEventListener("click", function(event) {
    event.preventDefault(); // Prevent default button behavior
    num=parseInt(event.target.id);

    customer_id_validation();

    var custommessage =bookingtransaction_processing(num);
  displayMessageBox(custommessage);
      
  })

function customer_id_validation(){
  customer_id=document.getElementById("id").value;
  if(customer_id!==previous_id(customer_id)){
    formDataObject.customer_id=customer_id;
  }
}

function previous_id(id){
  tempid=id;
  id=prev_id;
  prev_id=tempid;
  return id;

}
  btnOK.addEventListener('click', function() {
   
   
    hideMessageBox(); 
    // Hide the message box on OK button click
     formDataObject.amount=amount;
     formDataObject.total_price=data[0]*amount;
     formDataObject.num=num;
      
    
  
    // Add the form data object to the array
    formData.push(formDataObject);
  
    // Display form data
    console.log('Form Data:', formData);
  
    // Send form data to Django using HTTP API method
    sendDataToDjango(formData);
  
  });

  btnClose.addEventListener('click', function() {
    console.log('Close button clicked');
    
    hideMessageBox();
    amount=-document.getElementById("amount").value; 
  })


  function sendDataToDjango(formData) {
    // Convert form data to JSON string
    var jsonData = JSON.stringify(formData);
  
    // Send the form data to the Django backend
    fetch("http://localhost:8000/supplement/send/product_data/", {
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