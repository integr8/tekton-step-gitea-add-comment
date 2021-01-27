import requests
import os
from urllib.parse import ParseResultBytes, urlparse

from requests import api

"""
GITEA_HOST_URL:
GITEA_API_PATH_PREFIX:
IGNORE_SELFSIGNED_CERT:
REQUEST_URL:
GITEA_TOKEN:
COMMENT_FILE_NAME
COMMENT:
"""

gitea_host_url = os.environ.get('GITEA_HOST_URL')
gitea_api_path_prefix = os.environ.get('GITEA_API_PATH_PREFIX')
gitea_token = os.environ.get('GITEA_TOKEN')

ignore_selfsigned_cert = os.environ.get('IGNORE_SELFSIGNED_CERT')
request_url = os.environ.get('REQUEST_URL')
api_path_prefix = os.environ.get('GITEA_API_PATH_PREFIX')
comment = os.environ.get('COMMENT')

request_url_parse = urlparse(request_url)

if not gitea_host_url or not gitea_api_path_prefix:
    api_root_path = f"{request_url_parse.scheme}://{request_url_parse.netloc}{api_path_prefix}"
else:
    api_root_path = f"{gitea_host_url}{gitea_api_path_prefix}"

comment_api_url = f"{api_root_path}/repos{request_url_parse.path.replace('pulls','issues')}/comments"

headers = {
    "User-Agent": "TektonCD, the peaceful cat",
    "Authorization": f"Bearer {gitea_token}",
}

data = {
    "body": """{0}""".format(comment),
}

try:
    request = requests.post(comment_api_url, json=data, headers=headers)
    request.raise_for_status()
except requests.exceptions.RequestException as e:
    print(e)
