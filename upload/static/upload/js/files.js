const fileInput = document.querySelector('#id_file_upload input[type=file]');
fileInput.onchange = () => {
    if (fileInput.files.length > 0) {
        const fileName = document.querySelector('#id_file_upload .file-name');
        var text = ''
        let files_name_list = fileInput.files
        for (i = 0; i < files_name_list.length; i++) {
            text += files_name_list[i].name + ', '
        }
        console.log(text)
        fileName.textContent = text;
    }
}