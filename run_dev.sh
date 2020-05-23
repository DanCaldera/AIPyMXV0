#!/bin/bash

echo Setting Environment! 🛠
source .env/bin/activate

echo Checking Packages! 🛠
pip3 install -r requirements.txt

echo Setting Flask App variable and turning on debugger! 🛠
export FLASK_APP=main.py
export FLASK_DEBUG=1
export FLASK_ENV=development

echo Environment: $FLASK_ENV 🛠
echo Flask is running! 🌶
flask run
