#!/bin/bash
#
# Development testing script to verify that current changes to the code still
# validate and work successfully.
#

AUTHOR="Justin W. Flory (jflory7)"

test_valid_yaml_syntax () {
    if [ ! -f $(which yamllint) ]; then
        echo -e "yamllint not installed, exiting…"
        exit
    fi

    yamllint -s profiles/
}

test_build_html () {
    python3 generate_profiles.py -t template.html -o index.html profiles/
    echo -e "HTML successfully generated."
}

test_valid_yaml_syntax
test_build_html

