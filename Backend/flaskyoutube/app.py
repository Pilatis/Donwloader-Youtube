import yt_dlp as yt
import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
download_dir = "downloads"
ydl_opts = {
    "outtmpl": os.path.join(download_dir, "%(title)s.%(ext)s"),
    "format": "best",
}
"""@app.route É um decorator fornecido pelo Flask que é usado para associar uma função Python a uma URL específica. Em outras palavras,
ele diz ao Flask que, quando um cliente faz uma solicitação para essa URL, a função abaixo do decorator deve ser chamada."""
"""método POST é usado para enviar dados ao servidor para criar ou atualizar um recurso."""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download", methods=["POST"])
def download_video():
    # pega a url do corpo da solicitação
    video_url = request.form.get("url")
    # junta de forma correta o caminho para o arquivo
    ydl_opts = {
        "outtmpl": os.path.join(download_dir, "%(title)s.%(ext)s"),
        "format": "best",
    }
    # criar um diretório caso ele não exista
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    try:
        with yt.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return jsonify({"message": "vídeo baixado com sucesso!"})
    except Exception as erro:
        # O código 400 é um código de status HTTP que indica "Bad Request" (Solicitação Inválida).
        return jsonify({"error": str(erro)}), 400


if __name__ == "__main__":
    app.run(debug=True)
