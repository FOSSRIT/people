#!/bin/bash
#
# Script:       test.sh
# Authored by:  Justin W. Flory
# License:      GPLv3
#
# Test script to verify and successfully validate changes to existing code
#

# yamllint required for tests
command -v yamllint
if [ $? -eq 1 ]; then
    logger -s -p user.err 'fossprofiles: yamllint not found. Install yamllint via Pipenv or pip.'
    exit 127
fi

# check YAML files for correct syntax
yamllint -c .yamllintrc -s _data/
if [ $? -eq 1 ]; then
    logger -p user.err 'fossprofiles: yamllint tests failed. Run yamllint for detailed info.'
    exit 1
fi

# build actual profiles
python3 generate_profiles.py -t _ignore/template.html -o index.html _data/
logger -p user.info 'fossprofiles: HTML successfully generated.'
