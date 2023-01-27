# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Remove Price",
    "version": "16.0.1.0.0",
    "summary": "This module Will Remove All the price display",
    "author": "Aktiv Software",
    "sequence": 10,
    "description": """
This module Will Remove All the price display""",
    "depends": ["website_sale"],
    "data": [
        'views/compare_template_inherit.xml',
        'views/products_item_template_inherit.xml',
        'views/product_template_inherit.xml',
        'views/cart_template_inherit.xml',
        'views/extra_info_page_template_inherit.xml',
        'views/alternative_products_template_inherit.xml',
        'views/wishlist_template_inherit.xml',
        'views/dynamic_snippet_product_template_inherit.xml',
        'views/suggested_products_template_inherit.xml',
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
