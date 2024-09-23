document.getElementById('download-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const form = event.target;
    const url = form.url.value;
    const feedback = document.getElementById('feedback');

    feedback.innerHTML = 'Iniciando download...'
})