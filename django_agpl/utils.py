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
import re
import django_agpl

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

__all__ = ('get_file_list', 'create_tarball', 'get_fileobj')

def create_tarball(mode='w'):
    import tarfile
    fileobj = get_fileobj()
    f = tarfile.open('download', mode, fileobj)
    for location, name in get_file_list():
        f.add(location, name)
    f.close()
    return fileobj

def get_fileobj():
    return StringIO()

def matches_any(name, candidates):
    for pat in candidates:
        if re.search(pat, name):
            return True
    return False

def get_file_list():
    try:
        app_root = settings.AGPL_ROOT
    except AttributeError:
        raise ImproperlyConfigured(
            "You must specify 'AGPL_ROOT' in your project's settings"
        )

    try:
        prefix = settings.AGPL_PREFIX
    except AttributeError:
        # No prefix
        prefix = ''

    try:
        MY_EXCLUDE_FILES = settings.AGPL_EXCLUDE_FILES
    except AttributeError:
        # Fallback to default exclude list for files
        MY_EXCLUDE_FILES = django_agpl.EXCLUDE_FILES

    try:
        MY_EXCLUDE_DIRS = settings.AGPL_EXCLUDE_DIRS
    except AttributeError:
        # Fallback to default exclude list for directories
        MY_EXCLUDE_DIRS = django_agpl.EXCLUDE_DIRS

    for root, dirs, files in os.walk(app_root):
        for filename in files:
            if matches_any(filename, MY_EXCLUDE_FILES):
                continue

            yield (
                os.path.join(root, filename),
                os.path.join(
                    prefix,
                    root[len(app_root) + 1:],
                    filename,
                ),
            )

        for subdir in dirs:
            if matches_any(subdir, MY_EXCLUDE_DIRS):
                try:
                    dirs.remove(subdir)
                except ValueError:
                    pass
