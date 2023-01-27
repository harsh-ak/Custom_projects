from odoo.http import request
from odoo import http

class ChangeState(http.Controller):


    @http.route('/change_state',type='http', auth="public", website=True) 
    def change_state(self,**kw):
        request.website.sale_get_order().state='sent'
        return request.redirect('/contactus-thank-you')