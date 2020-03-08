foss-profiles
=============

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/FOSSRIT/foss-profiles.svg?branch=master)](https://travis-ci.org/FOSSRIT/foss-profiles)

HTML page generator for FOSS@MAGIC student, faculty, and alum profiles from YAML files


## About

foss-profiles helps [FOSS@MAGIC](http://foss.rit.edu "Free and Open Source Software at RIT") faculty and staff maintain a current roster of:

* Alums
* Faculty
* Mentors
* Students

The profiles are used for record-keeping and contact information.
They are also planned to eventually appear on the reworked [FOSS@MAGIC website](http://foss.rit.edu "Free and Open Source Software at RIT").


## Installation

foss-profiles uses [pipenv](https://pipenv.readthedocs.io/en/latest/) to manage dependencies.
Read their docs for installation help.

Once pipenv is installed, run these commands to initialize your development environment:

```bash
pipenv sync --dev
pipenv shell
```


## Usage

```bash
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

Want to contribute a profile?
See our [contributing guidelines](https://github.com/FOSSRIT/foss-profiles/blob/master/.github/CONTRIBUTING.md "How to contribute a new FOSS profile").

If you want to help with the actual project, awesome!
Help is welcome to make the template prettier or anything you think could be improved.
Note foss-profiles is a **Python 3.6** project.

Need help?
Join `#rit-foss` on the Freenode IRC network or join the bridged Telegram group.

* [IRC web chat](https://webchat.freenode.net/?channels=rit-foss "FOSS @ RIT community on Freenode IRC")
* [Telegram](https://t.me/fossrit "FOSS @ RIT community on Telegram")


## Legal

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

All work licensed under the [GPLv3 license](https://github.com/FOSSRIT/foss-profiles/blob/master/LICENSE.txt).
