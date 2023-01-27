from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleInherit(WebsiteSale):

    @http.route(['/shop/cart/update_json'], type='json', auth="public", methods=['POST'], website=True, csrf=False)
    def cart_update_json(
        self, product_id, line_id=None, add_qty=None, set_qty=None, display=True,
        product_custom_attribute_values=None, no_variant_attribute_values=None, **kw
    ):
        res = super(WebsiteSaleInherit, self).cart_update_json(product_id=product_id, line_id=line_id, add_qty=add_qty, set_qty=set_qty, display=display,
                                                               product_custom_attribute_values=product_custom_attribute_values, no_variant_attribute_values=no_variant_attribute_values, **kw)

        request.session['website_sale_cart_quantity'] = len(
            request.website.sale_get_order().order_line)
        res['cart_quantity'] = len(
            request.website.sale_get_order().order_line)
        return res

    @http.route(['/shop/cart/update_option'], type='http', auth="public", methods=['POST'], website=True, multilang=False)
    def cart_options_update_json(self, product_and_options, goto_shop=None, lang=None, **kwargs):
        res = super(WebsiteSaleInherit, self).cart_options_update_json(product_and_options=product_and_options,goto_shop=goto_shop,lang=lang,**kwargs)
        return str(len(
            request.website.sale_get_order().order_line))    
    

