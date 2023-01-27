from odoo import fields, models, api


class AddProduct(models.TransientModel):
    _name = "add.product.wizard"

    product_id = fields.Many2one(
        comodel_name="product.template", string="Product")

    def add_product(self):
        current_brand_object = self.env["product.brand"].browse(
            self.env.context.get("active_id")
        )
        current_brand_object.write({
            'product_ids': current_brand_object.product_ids+self.product_id

        })
