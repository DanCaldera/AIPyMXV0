#!/bin/bash

echo Setting Environment! 🛠
source .env/bin/activate

echo Setting Flask App variable and turning on debugger! 🛠
export FLASK_APP=main.py
export FLASK_DEBUG=1

echo Flask is running! 🌶
flask run
