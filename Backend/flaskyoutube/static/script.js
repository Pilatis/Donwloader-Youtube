document.getElementById('download-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const form = event.target;
    const url = form.url.value;
    const feedback = document.getElementById('feedback');

    feedback.innerHTML = 'Iniciando download...';

    //request
    fetch('download', {
        method: 'POST',
        body: new FormData(form),
    }).then(response => {
        const reader = response.body.getReader();
        const decoder = newTextDecoder();

        function read() {
            reader.read().then(({ done, value }) => {
                if (done) {
                    feedback.innerHTML += "Download completo!";
                    return;
                }

                const text = decoder.decode(value);
                feedback.innerHTML += text + "<br>";
                read();
            });
        }

        read();

    }).catch(error => {
        feedback.innerHTML += "Erro durante o download: " + error
    });
})