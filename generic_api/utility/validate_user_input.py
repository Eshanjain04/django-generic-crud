import cerberus


def validate_data(data_schema, data):
    validation_schema = cerberus.Validator(data_schema)
    is_valid = validation_schema.validate(data)
    if is_valid:
        return True, []
    else:
        validation_errors = validation_schema.errors
        return False, validation_errors
