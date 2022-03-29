from flask import Flask, request
import requests

app = Flask(__name__)

ALLOWED_MAGIC = "changeme" # changeme

@app.route("/")
def default():
    return "hey"

@app.route("/get/object", methods=['POST'])
def getobj():
    content = request.json
    try:
        bucket = content['bucket']
        object_name = content['object']
        magic = content['magic_str']
        if magic == ALLOWED_MAGIC:
            bucket_url = "http://" + bucket + ".s3.amazonaws.com/" + object_name
            r = requests.get(bucket_url)
            return("Content:\n" + r.text)
        else:
            return "sorry, I don't think you're allowed to do that"
    except:
        return "sorry, I don't understand"


app.run()