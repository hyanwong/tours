#!/usr/bin/env python3
import base64
import getpass
import json
import os.path
import urllib.request
import ssl
import sys

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Collect password
http_user = "admin"
http_password = getpass.getpass(prompt='Password for %s: ' % http_user, stream=None)

http_base = sys.argv[1]
if not http_base.startswith('http'):
    raise ValueError("Usage: upload.py http://localhost:8000/ *.json")
    sys.exit(1)

for file_path in sys.argv[2:]:
    url = "%s/tour/data.json/%s" % (
        http_base,
        os.path.splitext(os.path.basename(file_path))[0],
    )
    print("===== Uploading %s to %s" % (
        file_path,
        url
    ))

    with open(file_path, 'rb') as f:
        t = json.load(f)

    request = urllib.request.Request(url, method='PUT')
    request.add_header("Authorization", ("Basic %s" % base64.b64encode(':'.join((
        http_user,
        http_password
    )).encode('utf8')).decode('utf8')))
    request.add_header('Content-Type', 'application/json; charset=utf-8')
    bytes = json.dumps(t).encode('utf-8')
    request.add_header('Content-Length', len(bytes))

    with urllib.request.urlopen(request, bytes, context=ctx) as response:
        if response.status != 200:
            raise ValueError("Upload failed")
        out = json.load(response)
        print("Tour ID %d" % out['id'])

    request = urllib.request.Request("%s/tour/data.html/%s" % (
        http_base,
        os.path.splitext(os.path.basename(file_path))[0],
    ), method='GET')
    try:
        with urllib.request.urlopen(request, bytes, context=ctx) as response:
            if response.status != 200:
                print("Tour rendered as HTML")
    except urllib.error.HTTPError as e:
        print("Tour cannot be rendered by data.html, look at OneZoom error logs: %s" % e, file=sys.stderr)
        sys.exit(1)
