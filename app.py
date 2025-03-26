import os
from flask import Flask, jsonify
from azure.cosmos import CosmosClient
from dotenv import load_dotenv

# Load secrets from .env
load_dotenv()

app = Flask(__name__)

# Cosmos DB Config (Using Environment Variables)
ENDPOINT = os.getenv("COSMOS_ENDPOINT")
KEY = os.getenv("COSMOS_KEY")
DATABASE = "weatherDB"
CONTAINER = "weatherData"

client = CosmosClient(ENDPOINT, KEY)
database = client.get_database_client(DATABASE)
container = database.get_container_client(CONTAINER)

@app.route('/weather', methods=['GET'])
def get_weather():
    items = list(container.read_all_items())
    return jsonify(items)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
