Original path: devops-health-api/app/main.py
Note: this PDF displays the file's text. It is not a runnable replacement for the original .py, .sql, .yml, or configuration file.
"""Small Flask API with health and version endpoints."""
import os
from flask import Flask, jsonify
def create_app() -> Flask:
 app = Flask(__name__)
 version = os.getenv("APP_VERSION", "1.0.0")
 @app.get("/health")
 def health():
 return jsonify({"status": "ok"}), 200
 @app.get("/version")
 def get_version():
 return jsonify({"name": "devops-health-api", "version": version}), 200
 @app.get("/")
 def index():
 return jsonify({"service": "devops-health-api", "endpoints": ["/health", "/version"]}), 200
 @app.errorhandler(404)
 def not_found(_error):
 return jsonify({"error": "not_found"}), 404
 return app
app = create_app()
if __name__ == "__main__":
 app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
