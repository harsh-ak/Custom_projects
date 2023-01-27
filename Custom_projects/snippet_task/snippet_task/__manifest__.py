# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Snippet Task",
    "version": "16.0.1.0.0",
    "author": "Aktiv Software",
    "summary": "Snippet Task",
    "sequence": 10,
    "description": """
Snippet Task""",
    "depends": ["website_sale"],
    "data": [
    'views/snippets/snippet_template.xml',
    'views/snippets/snippet_register.xml',
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
