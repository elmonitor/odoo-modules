# -*- coding: utf-8 -*-
##############################################################################
#
#    Globalteckz
#    Copyright (C) 2013-Today(www.globalteckz.com).
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

{
    'name' : 'Tax Disable',
    'version' : '1.0',
    'author' : 'Globalteckz',
    'description': """
        This module customizes default behaviour of tax configuration on 
        sale order's, purchase order's and Invoices. Specially designed for Saudi Arabia business to hide the tax details on
        invoices/Sales/Purchase order and from Sale Order's, Purchase Order's and Invoice as well as hiding the tax 
        menu from the Accounting configuration menu
    """,
    'category': 'Accounts and Tax Configuration',
    'website' : 'www.globalteckz.com',
    'depends' : ['sale','account','purchase'],
    'images': ['images/main_screenshot.png'],
    'demo' : [],
    'data' : [
            'views/sale_view.xml',
            'views/product_view.xml',
            'views/account_view.xml',
            'views/purchase_view.xml'
            ],
    'test' : [],
    'auto_install': False,
    'application': True,
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
