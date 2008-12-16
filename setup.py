#!/usr/bin/env python

from setuptools import setup,find_packages

setup(
    name           = 'tracSolr',
    version        = '0.1',
    packages       = find_packages(),
    author         = 'pphetra',
    description    = 'integrate trac with Solr',
    license        = 'GPL',
    entry_points   = {'trac.plugins':['tracSolr.pluginwrapper = tracSolr.pluginwrapper']})
