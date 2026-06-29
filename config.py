# This Python file uses the following encoding: utf-8

import json

config = None

try:
    with open('Support/subscripts/ModMiiDownloader/downloader.json') as f:
        config = json.load(f)
except:
    with open('downloader.json') as f:
        config = json.load(f)