from flask import Flask
from flask_restx import Api, Resource
from models import register_models

app = Flask(__name__)
api = Api(app, doc='/swagger', title='BlueWave API',
          description='Telemetry and Desalination API')

# Register models
models = register_models(api)
observation_model = models["observation"]

# Fake in-memory DB
observations = [
    {"id": 1, "temperature": 23.5, "salinity": 35.1, "timestamp": "2025-08-28T00:45:00Z"}
]

@api.route('/observations')
class Observations(Resource):
    @api.marshal_list_with(observation_model)
    def get(self):
        """Get all observations"""
        return observations

    @api.expect(observation_model, validate=True)
    @api.marshal_with(observation_model, code=201)
    def post(self):
        """Create a new observation"""
        new_obs = api.payload
        new_obs['id'] = len(observations) + 1
        observations.append(new_obs)
        return new_obs, 201


if __name__ == '__main__':
    app.run(debug=True)
