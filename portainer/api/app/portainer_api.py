from flask import Flask, jsonify, render_template
import requests
from dotenv import load_dotenv
import os
import json
import urllib3

urllib3.disable_warnings()

app = Flask(__name__)

load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv("API_KEY")
PORTAINER_API = os.getenv("PORTAINER_API")
DOCKER_ENDPOINT = os.getenv("DOCKER_ENDPOINT")
containers_file = "/opt/portainer_api/containers.json"

with open(containers_file, "r") as f:
    container_map = {
        container["container_name"]: container["container_id"]
        for container in json.load(f)["container_names"]
    }

headers = {"X-API-Key": API_KEY}


@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)


@app.route("/")
def list_conatiners():
    container_names = list(container_map.keys())
    return render_template("index.html", container_names=container_names)


@app.route("/<container_name>")
def container_options(container_name):
    container_id = container_map.get(container_name)
    if container_id:
        return render_template("container.html", container_name=container_name)
    else:
        return jsonify({"message": f"Container {container_name} not found"}), 404


@app.route("/<container_name>/start")
def start_container(container_name):
    container_id = container_map.get(container_name)
    if container_id:
        endpoint_url = f"{PORTAINER_API}/endpoints/{DOCKER_ENDPOINT}/docker/containers"
        response = requests.post(
            f"{endpoint_url}/{container_id}/start",
            headers=headers,
            verify=False,
        )
        if response.status_code == 204:
            return f"Start {container_name}: {response.status_code}"
        else:
            return (
                jsonify(
                    {
                        "message": f"Failed to start {container_name} container",
                        "error": response.text,
                    }
                ),
                response.status_code,
            )

        if response.status_code == 204:
            container_status = "Running"
        else:
            container_status = "Stopped"

    else:
        return jsonify({"message": f"Container {container_name} not found"}), 404


@app.route("/<container_name>/stop")
def stop_container(container_name):
    container_id = container_map.get(container_name)
    if container_id:
        endpoint_url = f"{PORTAINER_API}/endpoints/{DOCKER_ENDPOINT}/docker/containers"
        response = requests.post(
            f"{endpoint_url}/{container_id}/stop",
            headers=headers,
            verify=False,
        )
        if response.status_code == 204:
            return f"Stop {container_name}: {response.status_code}"
        else:
            return (
                jsonify(
                    {"message": "Failed to stop container", "error": response.text}
                ),
                response.status_code,
            )
    else:
        return jsonify({"message": f"Container {container_name} not found"}), 404


@app.route("/<container_name>/restart")
def restart_container(container_name):
    container_id = container_map.get(container_name)
    if container_id:
        endpoint_url = f"{PORTAINER_API}/endpoints/{DOCKER_ENDPOINT}/docker/containers"
        response = requests.post(
            f"{endpoint_url}/{container_id}/restart",
            headers=headers,
            verify=False,
        )
        if response.status_code == 204:
            return f"Restart {container_name}: {response.status_code}"
        else:
            return (
                jsonify(
                    {"message": "Failed to restart container", "error": response.text}
                ),
                response.status_code,
            )
    else:
        return jsonify({"message": f"Container {container_name} not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
