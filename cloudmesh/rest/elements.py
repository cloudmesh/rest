from __future__ import print_function

import glob

import simplejson
from  ruamel import yaml


class Elements(object):
    def __init__(self, directory, filename):


        import os.path

        settings = {}
        try:
            os.remove(filename)
        except Exception as e:
            pass
        if ".yaml" in filename:
            for file in glob.glob(os.path.join(directory, '*.yml')):
                print("... reading", file)
                with open(file) as fd:
                    d = yaml.load(fd)
                    settings.update(d)
        elif "json" in filename:
            for file in glob.glob(os.path.join(directory, '*.json')):
                print ("... reading", file)
                with open(file) as fd:
                    d = simplejson.load(fd)
                    settings.update(d)
        else:
            print ("converrsion not supported")
            return None

        with open(filename, 'w') as fd:
            simplejson.dump(settings, fd, indent=4)


'''            
y2j.py:
import ruamel.yaml
import json

import sys

yfile = sys.argv[1]
y = open(yfile).read().strip()
d = yaml.load(y)
print json.dumps(d)
'''
