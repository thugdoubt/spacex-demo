import pymongo

from flask import (
    abort,
    Flask,
    jsonify,
    render_template,
    request
)


app = Flask(__name__)


def get_db():
    return pymongo.MongoClient('mongo').demo


def get_collection():
    return get_db().launches


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/v1/launches', methods=['GET'])
def get_launches():
    # process the query, generate the filter
    query = request.args.get('q')
    launch_filter = {}
    if query:
        launch_filter = { '$or': [
            { 'launch_year': { '$regex': query } },
            { 'rocket.rocket_name': { '$regex': query, '$options': 'i' } },
            { 'rocket.rocket_type': { '$regex': query, '$options': 'i' } },
            { 'launch_site.site_name': { '$regex': query, '$options': 'i' } },
        ] }

    # search!
    coll = get_collection()
    launches = []
    for launch in coll.find(launch_filter).sort('flight_number'):
        # ObjectId is not serializable. normally one would create a
        # serializer for it, but for this demo it's not needed
        del launch['_id']
        launches.append(launch)

    return jsonify({'count': len(launches), 'launches': launches})


@app.route('/api/v1/launch/<int:flight_number>', methods=['GET'])
def get_launch(flight_number):
    coll = get_collection()
    launch = coll.find_one({'flight_number': flight_number})
    if launch:
        del launch['_id']
        return jsonify(launch)
    abort(404)
