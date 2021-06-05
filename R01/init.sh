#!/bin/bash

VENE_DIR=".venv"
PYTHON_PATH="/usr/bin/python3"

# setup venv
$PYTHON_PATH -m venv $VENE_DIR
source $VENE_DIR/bin/activate

# pip version
pip --version

# pip install
pip install --force-reinstall -r requirements.txt
