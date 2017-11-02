StudentProfiles [![Build Status](https://travis-ci.org/FOSSRIT/FOSSProfiles.svg?branch=master)](https://travis-ci.org/FOSSRIT/FOSSProfiles)
===============

Jinja-powered template system for creating lists of student profiles. Running
this script outputs HTML with all YAML files passed as an argument. In the case
of this repository, you can pass the `profiles/` directory as an argument.


## Usage

```sh
./generate profiles
```


## Requirements

Profiles need only a bit of information and are organized to be sorted in the
output. In order for Jinja to build the template, all profile biographies must
be under 140 characters.

