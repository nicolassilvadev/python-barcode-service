'''
    Just some tests with cerberus
'''

from cerberus import Validator

body = {
    "data": {
        "elemento1": 123.34,
        "elemento2": "",
        # "elemento3": 223
    }
}

body_validator = Validator({
    "data": {
        "type": "dict",
        "schema": {
            "elemento1": { "type": "float", "required": True, "empty": False },
            "elemento2": { "type": "string", "required": True, "empty": False },
            "elemento3": { "type": "string", "required": True, "empty": False },
        }
    }
})

response = body_validator.validate(body)

if response is False:
    print(body_validator.errors)
else:
    print("body ok")
