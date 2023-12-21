#!/bin/sh

set -e

BASE_DIR="$( cd "$( dirname "$0" )" && pwd )"
VENV_DIR="${BASE_DIR}/.venv"

rm -rf "${BASE_DIR}/.pytest_cache"
rm -rf "${VENV_DIR}"
rm -rf "${BASE_DIR}/build"
rm -rf "${BASE_DIR}/dist"
rm -rf "${BASE_DIR}/src/wortsalat.egg-info"
rm -rf "${BASE_DIR}/test/__pycache__"
 

echo "##############################"
echo "### 1. Create a new venv   ###"
echo "##############################"

if python3 -m venv "${VENV_DIR}"; 
then
    echo "Venv Created"
else
    echo "Could not create venv"
    exit 1
fi

. $VENV_DIR/bin/activate

echo "##############################"
echo "### 2. Build the library   ###"
echo "##############################"
python3 -m pip install build
python3 -m build --wheel 

echo "##############################"
echo "### 3. Install the Library ###"
echo "##############################"
python3 -m pip install "${BASE_DIR}/dist/wortsalat-0.0.1-py3-none-any.whl"

echo "##############################"
echo "### 4. Start the tests     ###"
echo "##############################"
python3 -m pip install pytest
python3 -m pytest "${BASE_DIR}/tests/"