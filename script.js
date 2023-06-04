function processImage() {
    var fileInput = document.getElementById('uploadImage');
    var file = fileInput.files[0];
    var formData = new FormData();
    formData.append('image', file);

    fetch('/process_image', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        var resultDiv = document.getElementById('result');
        if (data.success) {
            resultDiv.innerHTML = '<h2>Title:</h2><p>' + data.title + '</p>' +
                                '<h2>Artist:</h2><p>' + data.artist + '</p>';
        } else {
            resultDiv.innerHTML = '<p>No matching lyrics found.</p>';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
