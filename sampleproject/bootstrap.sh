#!/usr/bin/env bash

echo ">>> Removing old environment"
if [ ! -d env ]; then
    rm -rf env
fi
echo ">>> Installing django into new virtualenv"
virtualenv env -p python3
env/bin/pip install -r requirements.txt
env/bin/pip install -e ../
