import os
import http.client
from http import HTTPStatus
import json
from hashlib import sha256
import time
import struct
import random

temp_filename = 'temp_file.dat'

file = open(temp_filename, 'rb')
file_contents = file.read()

conn = http.client.HTTPSConnection("build-uploader.vircadia.com")

context = json.loads(os.environ['GITHUB_CONTEXT'])

owner_and_repository = context["repository"].split("/")
owner = owner_and_repository[0]
repository = owner_and_repository[1]

headers = {
    "owner": owner,
    "repo": repository,
    "commit_hash": context["event"]["pull_request"]["head"]["sha"],
    "pull_number": context["event"]["number"],
    "job_name": os.environ["JOB_NAME"],
    "run_id": context["run_id"]
}

conn.request("PUT", "/", body=file_contents, headers=headers)
response = conn.getresponse()

EXIT_CODE_OK = 0
EXIT_CODE_ERROR = 1

if (response.status == HTTPStatus.OK):
    print("response: ",  json.loads(response.read()))
    exit(EXIT_CODE_OK)
else:
    print(response.status, response.reason, response.read())
    exit(EXIT_CODE_ERROR)
