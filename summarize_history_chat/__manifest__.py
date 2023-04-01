# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    "name": "Summarize Chat history",
    "version": "16.0.1.0",
    "author": "Captivea LLC",
    "maintainer": "Captivea LLC",
    "website": "https://www.captivea.com",
    "category": "Inventory",
    "license": "AGPL-3",
    'summary': """Allow Connection to OpenAI API""",
    "depends": [
        "base",
        "product",
        "cap_chat_gpt",
        "sale",
        "base_setup", 
        "auth_signup",
        "sale_management"
    ],
    "data": [
        "views/res_users_form_inherit.xml",
        "views/sale_order.xml"
    ],
    "installable": True,
    "application": True,
}
