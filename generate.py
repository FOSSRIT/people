#!/bin/env python
from __future__ import print_function
import hashlib
from itertools import ifilter
from jinja2 import Environment, FileSystemLoader
import os
import yaml


def get_template(name):
    env = Environment(loader=FileSystemLoader('.'))

    def testbio(bio):
        assert len(bio) <= 140, "Biography is too long"
        return bio

    env.filters['md5sum'] = lambda value: hashlib.md5(value).hexdigest()
    env.filters['testbio'] = testbio

    return env.get_template(name)


def rootedlistdir(pth):
    return [os.path.join(pth, name) for name in os.listdir(pth)]


def loadyaml(name):
    with open(name) as inf:
        return yaml.load(inf)


def yaml_filter(role):
    return lambda yml: yml.get('role', 'student') == role

template = get_template('template.html')
names = rootedlistdir("profiles")
yamls = [loadyaml(name) for name in names]
ROLES = ["captain", "faculty", "student", "alumni"]
sortedyamls = (yml for role in ROLES
               for yml in filter(yaml_filter(role), yamls))
rendered = (template.render(person=yml) for yml in sortedyamls)

with open("output.html", "w") as f:
    print("\n".join(rendered), file=f)
