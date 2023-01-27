# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Clear Cart",
    "version": "16.0.1.0.0",
    "summary": "Clear Cart",
    "author": "Aktiv Software",
    "sequence": 10,
    "description": """
Clear Cart""",
    "depends": ["website_sale"],
    "data": [
    'views/cart_template_inherit.xml'
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
