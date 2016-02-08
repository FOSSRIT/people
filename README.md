StudentProfiles
===============

A simple Jinja-powered template system for creating lists of student profiles. Running this script will output HTML with all of the YAML files passed as an argument. In the case of this repository, you can pass the `profiles/` directory as an argument.


## Usage

```sh
./generate profiles
```


## Requirements

Profiles need only a bit of information, and are organized such that they can be sorted in the output. In order for Jinja to build the template, all profile biographies must be under 140 characters.