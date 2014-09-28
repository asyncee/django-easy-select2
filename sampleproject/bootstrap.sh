#!/bin/bash

echo ">>> Removing old environment"
if [ ! -d env ]; then
    rm -rf env
fi
echo ">>> Installing django into new virtualenv"
virtualenv env &&
source ./env/bin/activate &&
pip install -r requirements.txt
pip install -e ../
