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

PREFIX = ''

EXCLUDE_FILES = [
    r'^site_settings.py$',
    r'^local_settings.py$',
    r'^\.gitignore$',
    r'\.pyc$',
    r'\.sql$',
    r'\.sqlite$',
]

EXCLUDE_DIRS = [
    r'^CVS$',
    r'^site_media$',
    r'^uploads$',
    r'\.git$',
    r'\.svn$',
]
