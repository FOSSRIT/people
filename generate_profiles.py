#!/bin/env python3
from __future__ import print_function
from __future__ import absolute_import
import argparse
import hashlib
from jinja2 import Environment, FileSystemLoader
import os
import yaml


def get_template(name):
    env = Environment(loader=FileSystemLoader('.'))

    def testbio(bio):
        assert len(bio) <= 140, "Biography is too long"
        return bio

    def md5sum(value):
        return hashlib.md5(value.encode('utf-8')).hexdigest()

    env.filters['md5sum'] = md5sum
    env.filters['testbio'] = testbio

    return env.get_template(name)


def rootedlistdir(pth):
    return [os.path.join(pth, name) for name in os.listdir(pth)]


def loadyaml(name):
    with open(name) as inf:
        return yaml.load(inf)


def parse_arguments():
    ROLES = ["captain", "faculty", "student", "alum", "mentor"]
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
    rendered = (template.render(person=loadyaml(name), role=role)
                for role in args.roles
                for name in rootedlistdir(os.path.join(args.directory, role))
                if os.path.splitext(name)[-1].lower() == ".yaml")

    print("\n".join(rendered), file=args.output)


if __name__ == '__main__':
    main()
