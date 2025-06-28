# models/fish_weight_popup.py
from odoo import models, fields

class FishWeightPopup(models.TransientModel):  # transient model dùng cho wizard/popup
    _name = 'fish.weight.popup'
    _description = 'Popup for Fish Weight'

    note = fields.Text('Ghi chú')  # trường ví dụ, bạn có thể thêm gì tùy ý

    def action_confirm(self):
        # Ví dụ xử lý, sau đó đóng popup
        return {'type': 'ir.actions.act_window_close'}
