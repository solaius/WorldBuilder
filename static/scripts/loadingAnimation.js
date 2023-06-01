// Show the loading spinner
function showLoadingSpinner() {
    document.getElementById('loading-spinner').style.display = 'block';
  }
  
  // Hide the loading spinner
  function hideLoadingSpinner() {
    document.getElementById('loading-spinner').style.display = 'none';
  }
  
   // Attach event listener to the form submission
   document.getElementById('settingForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission
    showLoadingSpinner(); // Show the loading spinner
    
  });