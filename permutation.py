#! /usr/bin/python

import sys

def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                #nb str[0:1] works in both string and list contexts
                yield perm[:i] + str[0:1] + perm[i:]


listT='abcdefghijklmnopqrstuvwxyz'
for p in all_perms(listT):
    print p
