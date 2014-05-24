# -*- coding: utf-8 -*-
##############################################################################
#
#    x_fiscal_printer
#    Copyright (C) 2014 No author.
#    No email
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{   'active': False,
    'author': 'No author.',
    'category': 'base.module_category_hidden',
    'demo_xml': [],
    'depends': [u'fiscal_printer'],
    'description': 'No documented',
    'init_xml': [],
    'installable': True,
    'license': 'AGPL-3',
    'name': 'fiscal_printer',
    'test': [ 'test/ev_info.yml' ],
    'data': [
        'data/fp_actions.xml',
        'data/fiscal_printer_view.xml',
        'data/journal_view.xml',
    ],
    'post_load': '',
    'js': [ 'static/src/js/fiscal_printer.js' ],
    'css': [],
    'qweb': ['static/src/xml/*.xml'],
    'version': 'No version',
    'website': ''}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
