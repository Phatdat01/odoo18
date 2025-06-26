from odoo import models, fields

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    production_note = fields.Text(string='Production Note')
