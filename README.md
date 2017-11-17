StudentProfiles [![Build Status](https://travis-ci.org/FOSSRIT/FOSSProfiles.svg?branch=master)](https://travis-ci.org/FOSSRIT/FOSSProfiles)
===============

HTML generator to create a page for FOSS@MAGIC profiles from YAML files


## About

StudentProfiles helps [FOSS@MAGIC](http://foss.rit.edu "Free and Open Source
Software at RIT") faculty and staff maintain a current roster of:

* Alums
* Faculty
* Mentors
* Students
* Student captains

The profiles are used for record-keeping or for other purposes, like alum or
student profiles on the [FOSS@MAGIC website](http://foss.rit.edu "Free and Open
Source Software at RIT").


## Requirements

To generate profiles, you need the following packages.

* `python3`
* `python3-jinja2`
* `python3-PyYAML`


## Usage

```sh
usage: generate_profiles.py [-h] [--template TEMPLATE]
                            [--roles ROLES [ROLES ...]] [--output OUTPUT]
                            directory

positional arguments:
  directory             Directory to read through

optional arguments:
  -h, --help            show this help message and exit
  --template TEMPLATE, -t TEMPLATE
                        Jinja template to use
  --roles ROLES [ROLES ...], -r ROLES [ROLES ...]
                        Ordered list of roles to use
  --output OUTPUT, -o OUTPUT
                        Output filename
```

## Contributing

If you want to contribute a profile, see our contributing guidelines.

If you want to help with the actual project, awesome! We'd love any help to make
the template prettier or anything that you think should be changed. Python 3.6
is recommended for your development environment, along with using
[Python virtual environments](https://stackoverflow.com/a/30233408/2497452). 

Need help? Join `#rit-foss` on the Freenode IRC network or join the bridged
Telegram group.

* [IRC web chat](https://webchat.freenode.net/?channels=rit-foss "FOSS @ RIT
  community on Freenode IRC")
* [Telegram](https://t.me/fossrit "FOSS @ RIT community on Telegram")


## Legal

All work in this repo is licensed under the
[GPLv3
license](https://github.com/FOSSRIT/FOSSProfiles/blob/master/LICENSE.txt).

