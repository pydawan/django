  const fileInput = document.querySelector('#id_file_upload input[type=file]');
  fileInput.onchange = () => {
    if (fileInput.files.length > 0) {
      const fileName = document.querySelector('#id_file_upload .file-name');
      fileName.textContent = fileInput.files[0].name;
    }
  }