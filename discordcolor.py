#!/usr/bin/python3
import sys
import logging
import cssutils

cssutils.log.setLevel(logging.CRITICAL)
parser = cssutils.parseFile(sys.argv[1])

orig1 = '#7289da'
orig2 = '#5b6dae'

for rule in parser.cssRules:
    try:
        if orig1 in rule.cssText:
            print(rule.cssText.replace(orig1, sys.argv[2]))
        if orig2 in rule.cssText:
            print(rule.cssText.replace(orig2, sys.argv[3]))
    except TypeError:
        pass
