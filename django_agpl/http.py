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
from django.http import HttpResponse
from django.core.exceptions import ImproperlyConfigured

from django_agpl.signals import project_downloaded

__all__ = ('DownloadHTTPResponse',)

class DownloadHttpResponse(HttpResponse):
    def __init__(self, fileobj, *args, **kwargs):
        extension = kwargs.pop('extension', '')
        super(DownloadHttpResponse, self).__init__(
            fileobj.getvalue(),
            *args,
            **kwargs
        )

        try:
            prefix = settings.AGPL_FILENAME_PREFIX
        except AttributeError:
            raise ImproperlyConfigured(
                "You must specify 'AGPL_FILENAME_PREFIX' in your "
                "project's settings"
            )

        self['Content-disposition'] = 'attachment; filename=%s%s' % \
            (prefix, extension)
        self.write(fileobj.getvalue())

        project_downloaded.send(sender=None)
