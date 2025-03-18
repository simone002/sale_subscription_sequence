from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    client_order_ref = fields.Char(string="Client Order Reference", copy=False, readonly=True, default=lambda self: self._generate_client_order_ref())

    @api.model
    def _generate_client_order_ref(self):
        return self.env['ir.sequence'].next_by_code('sale.order.client.order.ref') or '/'

    @api.model
    def _generate_client_order_ref(self):
        # Controlla se è un abbonamento usando il campo is_subscription
        if hasattr(self, 'is_subscription') and self.is_subscription:
            return self.env['ir.sequence'].next_by_code('sale.order.client.order.ref') or '/'
        # Per ordini normali, non generare un riferimento automatico
        return False