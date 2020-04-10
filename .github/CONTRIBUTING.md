# Contributing to People

Want to contribute to the **People** project?
Awesome!
Here's some things to help you make your contributiong.


## Add a new profile

First, look at the [YAML example profile](https://github.com/FOSSRIT/people/blob/master/example_profile.yaml) to see how the profiles are structured.
Copy this file and use it as a base to make your own profile.

### Required fields

All profiles must have these fields:

* `name`
* `website` (please include `http[s]://`)
* `email`
* `major`
* `graduation` (this means _expected graduation year from RIT_)
* `handle` (your IRC / Telegram username or your RIT computer account username)
* `bio` (**must be 140 characters or less**)

### Optional fields

These fields are optional.
You can include them if they apply to you.
Please include `http[s]://` for URLs:

* `blog`
* `forges.GitHub`
* `forges.GitLab`
* `forges.Personal`
* `forges.Keybase`
* `forges.[others]`


## Run tests

All pull requests are tested for three things:

1. If YAML syntax is valid
1. If Jekyll can build the site
1. If any URLs are broken

You can run the test suite locally before making a pull request.
After setting up a Ruby development environment and installing dependencies (see the `README.md` for instructions), run this command:

```bash
bundle exec rake test
```


## Get help

Something not covered in this guide?
Do you have other questions?
Join our IRC channel or Telegram group to say hello, get help, or ask questions.

* [IRC web chat](https://webchat.freenode.net/#rit-foss-admin "FOSS@RIT Tech Teamon Freenode IRC")
* [Telegram](https://t.me/fossrit_techteam "FOSS@RIT Tech Team on Telegram")
