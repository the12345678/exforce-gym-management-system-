document.addEventListener('DOMContentLoaded', () => {
  // Initialize Stripe with your public key
  const stripe = Stripe('your_stripe_public_key');

  // Create an instance of elements
  const elements = stripe.elements();
  const cardElement = elements.create('card');

  // Mount the card element to the HTML form
  cardElement.mount('#card-element');

  // Handle form submission
  const form = document.getElementById('payment-form');
  form.addEventListener('submit', async (event) => {
    event.preventDefault();

    // Collect payment information and create a payment token
    const { token, error } = await stripe.createToken(cardElement);

    if (error) {
      // Display payment errors
      const errorElement = document.getElementById('card-errors');
      errorElement.textContent = error.message;
    } else {
      // Send the payment token to your server (e.g., Django backend)
      // Modify the URL according to your backend endpoint
      const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
      const response = await fetch('/process_payment/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({ token: token.id }),
      });

      const data = await response.json();

      // Handle the response from the server (backend)
      if (data.message) {
        // Payment success
        alert(data.message);
      } else if (data.error) {
        // Payment failure
        alert('Payment failed: ' + data.error);
      }
    }
  });
});
