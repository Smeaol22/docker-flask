import json

from flask import Flask, request, Response


def launch():
    port = 8180
    app = Flask(__name__)

    @app.route('/')
    def status():
        return "IM UP!"

    @app.route('/launch', methods=['POST'])
    def post():
        inputs = request.json
        print(inputs["toto"])
        try:
            return Response(response=json.dumps({"status": "Done"}, sort_keys=True, ensure_ascii=False),
                            mimetype='application/json')
        except Exception as err:
            return Response(
                response=json.dumps({"error": str(err)}, sort_keys=True, ensure_ascii=False),
                mimetype='application/json', status=500
            )

    app.run(host="0.0.0.0", port=port)
