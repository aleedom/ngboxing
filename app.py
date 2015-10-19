from flask import Flask, render_template, request
from flask_restful import Api, Resource


app = Flask(__name__, template_folder='./static')
api = Api(app)


def volume(item):
    return item['length']*item['width']*item['height']*item['amount']


class Box(Resource):
    def post(self):
        box = request.get_json(force=True)
        total_volume = 0
        for item in box:
            total_volume += volume(item)
        return total_volume

api.add_resource(Box, '/api/box_order')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
