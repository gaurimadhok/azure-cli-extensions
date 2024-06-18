#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from codecs import open
from setuptools import setup, find_packages

# HISTORY.rst entry.
VERSION = '1.0.0b1'
try:
    from azext_providerhub.manual.version import VERSION
except ImportError:
    pass

# The full list of classifiers is available at
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
]

DEPENDENCIES = []

try:
    from azext_providerhub.manual.dependency import DEPENDENCIES
except ImportError:
    pass

with open('README.md', 'r', encoding='utf-8') as f:
    README = f.read()
with open('HISTORY.rst', 'r', encoding='utf-8') as f:
    HISTORY = f.read()

setup(
    name='providerhub',
    version=VERSION,
    description='Microsoft Azure Command-Line Tools ProviderHub Extension',
    author='Microsoft Corporation',
    author_email='azpycli@microsoft.com',
    url='https://github.com/Azure/azure-cli-extensions/tree/main/src/providerhub',
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    package_data={'azext_providerhub': ['azext_metadata.json']},
)
