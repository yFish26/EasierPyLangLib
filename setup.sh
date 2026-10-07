#!/bin/bash
# setup bash shell

echo "-----welcome to run setup shell! -----"

# install modules
echo "installing modules..."
pip install requirements.txt

# run init code
echo "running..."
python EasierPyLangLib/__init__.py

echo "ok"
