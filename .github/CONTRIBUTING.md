# Contributing to FOSSProfiles

Want to contribute to the FOSSProfiles project? Awesome! Here's some things to
help you make your contributiong.

## Adding a new profile

First, look at the [YAML example
profile](https://github.com/FOSSRIT/FOSSProfiles/blob/master/example_profile.yaml)
to see how the profiles are structured. You can also copy this file and use it
as a base for making your own profile.

### Required fields

All profiles are required to have these fields completed:

* `name`
* `website` (please include `http[s]://`)
* `email`
* `major`
* `graduation` (this means _graduation year from RIT_)
* `handle` (your IRC / Telegram username or your RIT computer account username)
* `bio` (**must be 140 characters or less**)

### Optional fields

These fields are optional. You can include them if they apply to you. please include `http[s]://` for URLs

* `blog`
* `forges.GitHub`
* `forges.BitBucket`
* `forges.Personal`
* `forges.Keybase`
* `forges.[others]`

## Running tests

All pull requests are tested for valid YAML syntax. To save time, you can test
everything out before you send your pull request. Run this script to make sure
everything still works.

```sh
./test.sh
```

## Get help

Something not covered in this guide? Do you have other questions? Jump into our
IRC channel or bridged Telegram group to say hello, get help, or ask questions.

* [IRC web chat](https://webchat.freenode.net/?channels=rit-foss "FOSS @ RIT
  community on Freenode IRC")
* [Telegram](https://t.me/fossrit "FOSS @ RIT community on Telegram")
