# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Product Brand",
    "version": "16.0.1.0.0",
    "author": "Aktiv Software",
    "summary": "Product Brand",
    "sequence": 10,
    "description": """
Product Brand""",
    "depends": ["website_sale"],
    "data": [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/shop_template_inherit.xml',
        'views/product_brand.xml',
        'views/product_view_inherit.xml',
        'views/brands_template.xml',
        'wizard/add_product_wizard_view.xml'

    ],
    "demo": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
