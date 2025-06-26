from odoo import models, fields

class Manufactory(models.Model):  # Dùng TransientModel cho popup
    _name = 'manufactory.fish_weight'
    _description = 'Get fish weight'

    fish_id = fields.Integer('Cá số')
    weight = fields.Float('Trọng lượng')
    fish_type = fields.Char('Cá loại')
    user_name = fields.Char('Tên người dùng')
    

