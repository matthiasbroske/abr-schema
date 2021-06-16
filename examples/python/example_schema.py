# example_schema.py
#
# Copyright (c) 2021, University of Minnesota
# Author: Bridger Herman <herma582@umn.edu>

import json
import requests
import jsonschema
from semver import VersionInfo

SCHEMA_URL = 'https://raw.githubusercontent.com/ivlab/abr-schema/master/ABRSchema_0-2-0.json'

def main():
    resp = requests.get(SCHEMA_URL)
    if resp.status_code != 200:
        print('Could not fetch schema')
        return

    schema = resp.json()

    example_state = {
        'version': '0.2.0-beta2',
        'scene': {
            'backgroundColor': '#FFFFFF'
        }
    }

    version = example_state['version']
    print('Schema version example state was created with:', VersionInfo.parse(version))

    try:
        jsonschema.validate(example_state, schema)
        print('Example state validates with schema!')
    except jsonschema.ValidationError as e:
        print('Schema validation failed:', e)


if __name__ == '__main__':
    main()