#!/bin/env python
from __future__ import print_function
import argparse
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


def parse_arguments():
    ROLES = ["captain", "faculty", "student", "alumni"]
    parser = argparse.ArgumentParser()
    parser.add_argument('--template', '-t', default='template.html',
                        help='Jinja template to use')
    parser.add_argument('--roles', '-r', nargs='+',
                        default=ROLES, help='Ordered list of roles to use')
    parser.add_argument('--output', '-o', default='-',
                        type=argparse.FileType('w'),
                        help='Output filename')
    parser.add_argument('directory', help='Directory to read through')
    return parser.parse_args()


def main():
    args = parse_arguments()
    template = get_template(args.template)
    names = rootedlistdir(args.directory)
    yamls = [loadyaml(name) for name in names]
    sortedyamls = (yml for role in args.roles
                   for yml in filter(yaml_filter(role), yamls))
    rendered = (template.render(person=yml) for yml in sortedyamls)

    print("\n".join(rendered), file=args.output)

if __name__ == '__main__':
    main()
