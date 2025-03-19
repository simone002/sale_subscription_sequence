from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    client_order_ref = fields.Char(string="Client Order Reference", copy=False, readonly=True)
    
    @api.model_create_multi
    def _create(self, vals_list):
        records = super(SaleOrder, self)._create(vals_list)
        for record in records:
            # Check if this is a subscription order (has visible plan_id)
            if record.plan_id and record.plan_id.visible:
                record.client_order_ref = self.env['ir.sequence'].next_by_code('sale.order.subscription.ref') or '/'
        return records