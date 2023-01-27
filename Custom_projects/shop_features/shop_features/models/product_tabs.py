from odoo import fields,models
from odoo.tools.translate import html_translate



class ProductTabs(models.Model):
    _name = "product.template.tabs"


    name=fields.Char(string="Tab Name")
    product_id=fields.Many2one(comodel_name="product.template")
    sequence = fields.Integer(default=1)
    is_active=fields.Boolean(string="Is Active?")
    snippet_content=fields.Html(string="Snippet Content", sanitize_overridable=True, sanitize_attributes=False, translate=html_translate, sanitize_form=False)