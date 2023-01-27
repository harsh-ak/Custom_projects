from odoo import api, fields, models



class Brand(models.Model):
    _name = "product.brand"
    _description="This Model Will store all the details related to the product Brand."



    

    name=fields.Char(string="Brand Name")
    website_id=fields.Many2one(comodel_name="website")
    logo=fields.Image(string='Logo',required=True)
    product_ids=fields.One2many(comodel_name="product.template",inverse_name="brand_id")
    is_published=fields.Boolean(string="Published")
    