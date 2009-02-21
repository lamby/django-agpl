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

from django.conf import settings

from django_agpl.http import DownloadHttpResponse
from django_agpl.utils import get_file_list, create_tarball, get_fileobj

__all__ = ('tar', 'tarbz', 'tarbz2', 'zip')

def tar(self):
    return DownloadHttpResponse(
        create_tarball(),
        extension='.tar',
        mimetype='application/x-gtar',
    )

def targz(self):
    return DownloadHttpResponse(
        create_tarball(mode='w|gz'),
        extension='.tar.gz',
        mimetype='application/x-gtar',
    )

def tarbz2(self):
    return DownloadHttpResponse(
        create_tarball(mode='w|bz2'),
        extension='.tar.bz2',
        mimetype='application/x-gtar',
    )

def zip(self):
    import zipfile

    fileobj = get_fileobj()
    f = zipfile.ZipFile(fileobj, mode='w')
    for location, name in get_file_list():
        f.write(location, name)
    f.close()

    return DownloadHttpResponse(
        fileobj,
        extension='.zip',
        mimetype='application/x-gtar',
    )
