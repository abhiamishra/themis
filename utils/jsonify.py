import json

from bson import json_util


def jsonify(data):
    return json.loads(json_util.dumps(data))
