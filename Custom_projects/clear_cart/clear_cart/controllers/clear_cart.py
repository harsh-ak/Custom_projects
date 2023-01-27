from odoo.http import request
from odoo import http

class ClearCart(http.Controller):


    @http.route('/clear_cart',type='http', auth="public", website=True) 
    def clear_all_products(self,**kw):
        for rec in request.website.sale_get_order().order_line:
            rec.unlink()
        return request.redirect("/shop") 