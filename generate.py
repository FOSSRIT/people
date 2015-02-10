from __future__ import print_function
import hashlib
from jinja2 import Environment, FileSystemLoader
import os
import yaml

with open("template.html") as f:
    env = Environment(loader=FileSystemLoader('.'))

env.filters['md5sum'] = lambda value: hashlib.md5(value).hexdigest()

template = env.get_template('template.html')

# TODO: Handle too-long bios (>140 characters)

with open("output.html", "w") as f:
    for yml in os.listdir("profiles"):
        with open(os.path.join("profiles", yml)) as inf:
            print(template.render(person=yaml.load(inf)), file=f)
