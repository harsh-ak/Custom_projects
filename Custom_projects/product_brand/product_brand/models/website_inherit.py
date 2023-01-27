from odoo import fields, models


class WebsiteInherit(models.Model):
    _inherit = "website"



    def _search_with_fuzzy(self, search_type, search, limit, order, options):
        res=super(WebsiteInherit,self)._search_with_fuzzy(search_type, search, limit, order, options)
        # brand_id=request.params.get('brand')
        # print("=====================================",brand_id)
        return res