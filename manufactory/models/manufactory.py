from odoo import models, fields

class Manufactory(models.Model):  # Dùng TransientModel cho popup
    _name = 'manufactory.fish_weight'
    _description = 'Get fish weight'

    fish_id = fields.Integer('Cá số')
    weight = fields.Float('Trọng lượng')
    fish_type = fields.Char('Cá loại')
    user_name = fields.Char('Tên người dùng')

    image_1920 = fields.Binary('Hình ảnh', attachment=True, help="This is the image of the fish.")
    
    def open_popup(self):

        self.ensure_one()  # sẽ fail nếu self là int

        return {
            'type': 'ir.actions.act_window',
            'name': 'Fish Popup',
            'res_model': 'fish.weight.popup',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_fish_id': self.fish_id,
                'default_note': 'Auto-filled from main form'
            }
        }
