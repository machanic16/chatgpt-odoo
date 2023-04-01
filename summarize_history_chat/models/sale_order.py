# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from bs4 import BeautifulSoup


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    ai_assisted_summary = fields.Text('Summary Chat History')


    def summarize_chat_history(self):
        chatgpt_session = self.env.user.chatgpt_sesion_id
        
        messages = self.env['mail.message'].search([('model','=',self._name),('res_id','=',self.id),('ai_generated','=',False)])
        body_messages = messages.mapped('body')
        only_text_messages = []

        for html_string in body_messages:
            soup = BeautifulSoup(html_string, "html.parser")
            text = soup.get_text()
            only_text_messages.append(text)


        promt = 'Give a good summary of this conversation: '
        for message in only_text_messages:
                promt += "\n -" + message

        
        summary = chatgpt_session.send_pront(promt,150)
        self.ai_assisted_summary = summary.choices[0].message.content

    def post_summay_in_chatter(self):
        message = self.message_post(body=self.ai_assisted_summary)
        message.message_type = 'comment'
        message.ai_generated = True
        self.ai_assisted_summary = ""