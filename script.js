document.getElementById('pdf-upload').addEventListener('change', function(e) {
    const fileName = e.target.files[0]?.name || 'No file selected';
    document.getElementById('file-name').textContent = fileName;
  });
  
  function handleSubmit() {
    const fileInput = document.getElementById('pdf-upload');
    if (!fileInput.files.length) {
      alert('Please upload a PDF file before submitting.');
      return;
    }
    alert('Form submitted successfully!');
  }