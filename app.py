# app.py
1  import os
2  import flask
3  from flask_cors import CORS
4
5  app = flask.Flask(__name__)
6
7  # Hardcoded secret — Aikido should flag this.
8  app.config['SECRET_KEY'] = "supersecret_demo_12345"
9
10 # Debug mode enabled — Aikido / SAST will report.
11 app.debug = True
12
13 # Insecure CORS policy
14 CORS(app, resources={r"/*": {"origins": "*"}})
15
16 @app.route("/ping")
17 def ping():
18     return "pong"
19
20 # Command injection: using os.popen on user input
21 @app.route("/run/<cmd>")
22 def run(cmd):
23     # vulnerable: calling shell through user-provided string
24     return os.popen(cmd).read()
25
26 # Unsafe deserialization example for demo
27 import pickle
28 @app.route("/load", methods=["POST"])
29 def load():
30     data = flask.request.data
31     # insecure: untrusted pickle.loads
32     obj = pickle.loads(data)
33     return f"Loaded {type(obj)}"
34
35 if __name__ == "__main__":
36     app.run(host="0.0.0.0", port=5000)
