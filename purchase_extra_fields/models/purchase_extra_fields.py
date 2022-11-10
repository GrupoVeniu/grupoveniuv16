from odoo import fields, models

class purchaseExtra(models.Model):
    _inherit = 'purchase.order'
    
    motivo_de_uso = fields.Selection([('c','Consumo'), ('v','Venta'), ('r','Reposicion')], string="Motivo de Uso", required=True)
    # desarrollo = fields.Selection([('I','Iarará'), ('OS','OmnivitaliaSur'), ('OC','Omnivitalia Chapalita')], string="Desarrollo de interés", required=True)
    # interes = fields.Selection([('D','Renta'), ('I','Venta'), ('OS','Inversión')], string="Interés", required=True)
