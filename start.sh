#! /usr/bin/sh
cd $(dirname "$0")/../../..
source Support/subscripts/ModMiiDownloader/.venv/bin/activate
python Support/subscripts/ModMiiDownloader/main.py
exit
