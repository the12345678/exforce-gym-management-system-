document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('login-form');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const rememberCheckbox = document.getElementById('remember');
    const errorMessage = document.getElementById('error-message');
    const successMessage = document.getElementById('success-message');
  
    form.addEventListener('submit', (e) => {
      e.preventDefault();
  
      const username = usernameInput.value.trim();
      const password = passwordInput.value.trim();
      const remember = rememberCheckbox.checked;
  
      errorMessage.textContent = '';
      successMessage.textContent = '';
  
      if (username === '') {
        showError('Username is required');
        return;
      }
  
      if (password === '') {
        showError('Password is required');
        return;
      }
  
      // Perform your login logic here
      // Example: make an API request to authenticate the user
  
      // Simulating a successful login
      showSuccess('Login successful');
      form.reset();
      rememberCheckbox.checked = remember;
    });
  
    function showError(message) {
      errorMessage.textContent = message;
    }
  
    function showSuccess(message) {
      successMessage.textContent = message;
    }
  });
  