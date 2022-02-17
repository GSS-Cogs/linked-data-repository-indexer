import json
from jsonschema import validate

schema = {
    "properties": {
        "item_one": {"type": "string"},
        "item_two": {"type": "number"}
    }
}


def validate_schema(message_payload):
    """
    Validate message queue payload against json schema
        - message_payload: queue item message
    """
    message_payload = json.dumps(message_payload)
    try:
        validate(instance=message_payload, schema=schema)
    except Exception as err:
        # make sure we log errors for debugging purposes
        # TO DO: replace with logging
        raise ValueError('error validating: %s' % (err))
