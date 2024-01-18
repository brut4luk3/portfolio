document.querySelectorAll('.dropdown-item').forEach(item => {
    item.addEventListener('click', (event) => {
        event.preventDefault();
        const selectedValue = event.target.getAttribute('data-value');
        document.getElementById('modo-hidden').value = selectedValue;
        document.getElementById('modo').innerText = event.target.innerText;
    });
});

function copiarCurl(id) {
    var curlCode = document.getElementById(id);
    var textoCurl = curlCode.innerText;

    navigator.clipboard.writeText(textoCurl).then(function() {
        alert('cURL copiada com sucesso!');
    }, function() {
        alert('Erro ao copiar a cURL.');
    });
}