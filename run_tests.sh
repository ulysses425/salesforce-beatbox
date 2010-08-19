#!/bin/bash
PYTHON=~/jython2.5.1/bin/jython
export PYTHONPATH=.:./src

$PYTHON src/beatbox/tests/test_beatbox.py
$PYTHON src/beatbox/tests/test_pythonClient.py
