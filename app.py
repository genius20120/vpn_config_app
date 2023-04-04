from flask import Flask
from config_info import create_response

app = Flask(__name__)


@app.route("/<name>", methods=["GET"])
def get_information(name):
    if name == "favicon.ico":
        return None
    
    response = create_response(name)
    return response
    # return json.dumps(response)

if __name__=="__main__":
    app.run(port=5000,host="0.0.0.0")
