# -*- coding: utf-8 -*-
#
# django-agpl -- tools to aid releasing Django projects under the AGPL
# Copyright (C) 2008, 2009, 2016 Chris Lamb <chris@chris-lamb.co.uk>
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
import re
import six
import tarfile
import zipfile

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from . import app_settings


def create_tarball(mode='w'):
    fileobj = six.BytesIO()
    f = tarfile.open('download', mode, fileobj)
    for location, name in get_file_list():
        f.add(location, name)
    f.close()
    return fileobj

def create_zip():
    fileobj = six.BytesIO()
    f = zipfile.ZipFile(fileobj, mode='w')
    for location, name in get_file_list():
        f.write(location, name)
    f.close()
    return fileobj

def matches_any(name, candidates):
    return any(re.search(x, name) for x in candidates)

def get_setting(val):
    return getattr(settings, 'AGPL_{}'.format(val), getattr(app_settings, val))

def get_file_list():
    try:
        app_root = settings.AGPL_ROOT
    except AttributeError:
        raise ImproperlyConfigured(
            "You must specify 'AGPL_ROOT' in your project's settings"
        )

    prefix = get_setting('PREFIX')
    exclude_dirs = get_setting('EXCLUDE_DIRS')
    exclude_files = get_setting('EXCLUDE_FILES')

    for root, dirs, files in os.walk(app_root, topdown=True):
        for filename in files:
            if matches_any(filename, exclude_files):
                continue

            yield (
                os.path.join(root, filename),
                os.path.join(
                    prefix,
                    root[len(app_root) + 1:],
                    filename,
                ),
            )

        dirs[:] = [x for x in dirs if not matches_any(x, exclude_dirs)]
