from flask import Flask, request
from flask_expects_json import expects_json

from exceptions import InvalidRuleNameError
from services import RuleDataHandler


app = Flask(__name__)

schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "array",
            "minItems": 1,
            "items": {"type": "number"}
        },
        "rule": {
            "type": "string",
            "minLength": 1
        },
    },
    "required": ["data", "rule"]
}


@app.route('/start', methods=['POST'])
@expects_json(schema)
def start():
    request_data = request.get_json()
    try:
        return {"result": RuleDataHandler(request_data).apply()}, 200
    except InvalidRuleNameError as exc:
        return {
            "result": [],
            "message": str(exc)
        }, 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
