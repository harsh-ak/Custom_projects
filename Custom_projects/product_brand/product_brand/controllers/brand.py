from odoo.http import request
from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale

class Brand(http.Controller):


    @http.route('/shop/brands',type='http', auth="public", website=True) 
    def brands(self,**kw):
        brands=request.env['product.brand'].search([('is_published','=',True),'|',('website_id','=',request.website.id),('website_id','=',False)])
        return request.render('product_brand.brand_page',{'brands':brands})



class WebsiteSaleInherit(WebsiteSale):

    def _get_search_options(
        self, category=None, attrib_values=None, pricelist=None, min_price=0.0, max_price=0.0, conversion_rate=1, **post
    ):
        res=super(WebsiteSaleInherit,self)._get_search_options(category=category, attrib_values=attrib_values, pricelist=pricelist, min_price=min_price, max_price=max_price, conversion_rate=conversion_rate, **post)
        if post.get('brand'):
            res['brand']=post.get('brand')
        return res
