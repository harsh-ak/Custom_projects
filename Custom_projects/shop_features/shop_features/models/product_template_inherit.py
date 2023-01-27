from odoo import fields, models


class Product(models.Model):
    _inherit = "product.template"


    tab_ids=fields.One2many(comodel_name="product.template.tabs",inverse_name="product_id")
    






