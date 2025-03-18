from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    is_subscription = fields.Boolean(string="Is Subscription", default=False)
    client_order_ref = fields.Char(
        string="Client Order Reference",
        copy=False,
        readonly=True,
        default=False
    )

    @api.model_create_multi
    def create(self, vals_list):
        """Gestisce la creazione in batch e assegna la sequenza solo agli ordini di abbonamento"""
        sequence = self.env.ref("sale_subscription_sequence.sequence_subscription_order")

        for vals in vals_list:
            if vals.get("is_subscription") and not vals.get("client_order_ref"):
                vals["client_order_ref"] = sequence.next_by_id()

        return super().create(vals_list)

    def renew_subscription(self):
        """Duplica l'ordine mantenendo il client_order_ref"""
        self.ensure_one()
        new_order = self.copy(default={"client_order_ref": self.client_order_ref})
        return new_order