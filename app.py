import connexion
import json
from Styrofoam import Styrofoam
from ProduceFoam import ProduceFoam
from connexion import NoContent
from flask_cors import CORS, cross_origin

HEADERS = { "content-type": "application/json" }

def get_styrofoam(width=0, thickness=0, height=0, orderNum=0):
    return NoContent, 200

def add_styrofoam(width, thickness, height, orderNum):
    return NoContent, 200

def get_cut_format(width, thickness, height, amount):
    s = Styrofoam(width, thickness, height)
    p = ProduceFoam(s, amount)
    cut_format = p.get_optimized_results(1)
    json_data = json.loads(json.dumps(cut_format[0].__dict__))
    print(json_data)
    return json_data, 200

def calculate_cut_formats(styrofoamFormats):
    print(styrofoamFormats)
    cut_formats = []
    for styrofoamFormat in styrofoamFormats:
        s = Styrofoam(styrofoamFormat["width"], styrofoamFormat["thickness"], styrofoamFormat["height"])
        p = ProduceFoam(s, styrofoamFormat["amount"])
        cut_format = p.get_optimized_results(1)
        cut_formats.append(cut_format)
    json_data = json.loads(json.dumps([cut_format[0].__dict__ for cut_format in cut_formats]))
    return json_data, 200

app = connexion.FlaskApp(__name__, specification_dir='')
CORS(app.app)
app.app.config['CORS_HEADERS'] = 'Content-Type'
app.add_api("openapi.yaml")

if __name__ == "__main__":
    app.run(port=8080)