from odoo.http import request
from odoo import http

class OrdeNote(http.Controller):


    @http.route('/get_order_note',type='http', auth="public", website=True) 
    def get_note(self,**kw):
        request.website.sale_get_order().write({
            'note':kw['note']
            })
        print("==============",request.website.sale_get_order())
            # return request.render('website.contactus_thanks',{}) 