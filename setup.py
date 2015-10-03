#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# django-agpl -- tools to aid releasing Django projects under the AGPL
# Copyright (C) 2008, 2009 Chris Lamb <chris@chris-lamb.co.uk>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import glob

def get_files(dirs, prefix=None):
    oldpwd = os.path.abspath(os.curdir)
    if prefix:
        os.chdir(prefix)

    result = []
    for dir in dirs:
        for dirpath, dirnames, filenames in os.walk(dir):
            for filename in filenames:
                result.append(os.path.join(dirpath, filename))

    os.chdir(oldpwd)
    return result

setup_args = dict(
    name='django-agpl',
    version=1,
    packages=[
        'django_agpl',
    ],
    author='Chris Lamb',
    author_email='chris@chris-lamb.co.uk',
    package_data={
        'django_agpl': get_files(['templates'], 'django_agpl'),
    },
    data_files = (
        ('share/django_agpl', glob.glob('images/*')),
    ),
)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(**setup_args)
