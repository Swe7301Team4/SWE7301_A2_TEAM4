from flask_restx import fields

def register_models(api):
    # Define Observation model
    observation_model = api.model('Observation', {
        'id': fields.Integer(readonly=True, description='Observation ID'),
        'temperature': fields.Float(required=True, description='Water temperature in °C'),
        'salinity': fields.Float(required=True, description='Water salinity in PSU'),
        'timestamp': fields.String(required=True, description='Observation timestamp (ISO8601)')
    })

    return {
        "observation": observation_model
    }
