#!/usr/bin/env bash
set -e

on_error_exit() {
    echo "ERROR: Command \"${BASH_COMMAND}\" at ${BASH_SOURCE} line ${BASH_LINENO} failed with exit code $?." >&2
}
trap on_error_exit ERR

cd "$(dirname "$0")"

echo ">>> Removing old environment"
if [ ! -d env ]; then
    rm -rf env
fi
echo ">>> Installing django into new virtualenv"
virtualenv env -p python3
env/bin/pip install -r requirements.txt
env/bin/pip install -e ../
