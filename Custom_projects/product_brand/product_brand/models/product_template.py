from odoo import fields, models,api


class Product(models.Model):
    _inherit = "product.template"

    brand_id = fields.Many2one(comodel_name="product.brand",string="Brand")


    
    def _search_get_detail(self, website, order, options):
        res=super(Product,self)._search_get_detail(website,order,options)
        print("=========================resssssssssssssssssss",res)
        if options.get('brand'):
            # brand_rec=self.env['product.brand'].browse(int((options.get('my_dict').get('brand'))))
            # product_recs=self.env['product.template'].search([])
            # product_recs.filtered_domain([('id','in',brand_rec.product_ids.ids)])
            res.get('base_domain').append([('brand_id','=',int(options.get('brand')))])
        return res