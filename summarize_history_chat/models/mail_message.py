# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from odoo.tools import format_amount


class MailMessage(models.Model):
    _inherit = "mail.message"
    
    ai_generated = fields.Boolean(string="AI generated", help="This field help to filter the messages generated for ChatGPT")
    