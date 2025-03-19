from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    client_order_ref = fields.Char(string="Client Order Reference", copy=False, readonly=True)
    
    @api.model
    def create(self, vals):
        record = super(SaleOrder, self).create(vals)
        # Check if this is a subscription order (has visible plan_id)
        if record.plan_id and record.plan_id.visible:
            record.client_order_ref = self.env['ir.sequence'].next_by_code('sale.order.subscription.ref') or '/'
        return record