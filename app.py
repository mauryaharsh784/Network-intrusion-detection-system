from flask import Flask, render_template, jsonify
import threading
import capture

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    return jsonify({
        "logs": capture.logs,
        "normal": capture.normal_count,
        "attack": capture.attack_count,
        "mode": "Simulation Mode"
    })

def start_detection():
    capture.detect()

if __name__ == "__main__":
    t = threading.Thread(target=start_detection)
    t.daemon = True
    t.start()
    app.run(debug=True)
