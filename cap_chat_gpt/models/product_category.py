# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from odoo.tools import format_amount


class ProductCategory(models.Model):
    _inherit = "product.category"
    
    chatgpt_sesion_id = fields.Many2one(string="ChatGPT Session", comodel_name='chatgpt.config', help="Select a sesion to use a specific API Key")
