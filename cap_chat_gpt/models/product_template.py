# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError,UserError
from odoo.tools import format_amount


class ProductTemplate(models.Model):
    _inherit = "product.template"

    ai_assisted_description = fields.Char('ChatGPT Description')

    def generate_description(self):
        if self.categ_id.chatgpt_sesion_id:
            chatgpt_session = self.categ_id.chatgpt_sesion_id
            promt = f'tell me a nice description for this product : \n - name={self.name}  \n - sales price = {self.list_price}  \n - number of variant = 4'

            description = chatgpt_session.send_pront(promt)
            self.ai_assisted_description = description.choices[0].message.content
        
        else:
            raise UserError("There is not ChatGPT session configured in the product category \n please fill that configuration and try again")