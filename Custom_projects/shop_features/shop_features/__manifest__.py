# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Shop Features",
    "version": "16.0.1.0.0",
    "summary": "Added Features to Shop Page",
    "sequence": 20,
    "description": """
Added Features to Shop Page""",
    "depends": ["website_sale"],
    "data": [
    'security/ir.model.access.csv',
    'views/shop_template_inherit.xml',
    'views/product_view_inherit.xml',
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
    'assets': {
        'web.assets_frontend': [
            'shop_features/static/src/css/my_custom_css.css',
        ]
    }
}