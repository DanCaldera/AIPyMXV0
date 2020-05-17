#!/bin/bash

echo Setting Environment! 🛠
source .env/bin/activate

echo Checking Packages! 🛠
pip install -r requirements.txt

export FLASK_APP=main.py

echo Testing 🧪
flask test
