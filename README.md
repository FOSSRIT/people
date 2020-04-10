people
======

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/FOSSRIT/people.svg?branch=master)](https://travis-ci.org/FOSSRIT/people)

Interactive directory of FOSS@RIT community members generated from YAML profiles and built with Jekyll


## About

The **People** project [FOSS@MAGIC](https://fossrit.github.io "Free and Open Source Software at RIT") faculty and staff maintain a current roster of:

* Alums
* Faculty
* Mentors
* Students

The profiles are used for record-keeping and contact information.


## Installation

**People** uses a Ruby-based static site generator called [Jekyll](https://jekyllrb.com/).

1. Install a full [Ruby development environment](https://www.ruby-lang.org/en/documentation/installation/).
1. Install `bundler` and this project's `Gemfile`.

    ```bash
    gem install bundler
    bundle install
    ```

1. Build the site and make it available on a local server.

    ```bash
    bundle exec jekyll serve --watch
    ```

1. Browse to http://localhost:4000

Ta-da, the project should appear locally in your browser.


## Usage

```bash
bundle exec jekyll serve --watch
```


## Contributing

Want to contribute a profile?
See our [contributing guidelines](https://github.com/FOSSRIT/foss-profiles/blob/master/.github/CONTRIBUTING.md "How to contribute a new FOSS profile").

If you want to help with the actual project, awesome!
First, check the [open issues](https://github.com/FOSSRIT/people/issues) for things we are working on or need help with.
Please open an issue to discuss changes before submitting a pull request.

### Need help?

Join `#rit-foss` on the Freenode IRC network or join the bridged Telegram group.

* [IRC web chat](https://webchat.freenode.net/#rit-foss-admin "FOSS@RIT Tech Team on Freenode IRC")
* [Telegram](https://t.me/fossrit_techteam "FOSS@RIT Tech Team on Telegram")


## Legal

All work licensed under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html).
