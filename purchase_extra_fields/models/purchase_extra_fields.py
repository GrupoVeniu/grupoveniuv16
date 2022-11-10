from odoo import fields, models

class purchaseExtra(models.Model):
    _inherit = 'purchase.order'

    motivo_de_uso = fields.Selection ([('C', 'Consumo), ('O', 'Otros), ('V', 'Venta')], string="Motivos de uso")

