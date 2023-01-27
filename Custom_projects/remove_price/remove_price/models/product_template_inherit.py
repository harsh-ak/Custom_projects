from odoo import api, fields, models, _
from odoo.addons.http_routing.models.ir_http import slug, unslug


class ProductTemplateInherit(models.Model):
    _inherit = "product.template"

    def _search_render_results(self, fetch_fields, mapping, icon, limit):
        if 'detail' in mapping:
            mapping.pop('detail')
        res = super(ProductTemplateInherit, self)._search_render_results(
            fetch_fields=fetch_fields, mapping=mapping, icon=icon, limit=limit)
        return res

   