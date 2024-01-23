from flask import Flask, request, Response

app = Flask(__name__)


@app.route("/generate", methods=["POST"])
def generate():
    print(request.json)
    return Response("onnistui")


if __name__ == "__main__":
    app.debug = True
    app.run()
