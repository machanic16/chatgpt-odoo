# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    "name": "Cap ChatGPT Sesions",
    "version": "16.0.1.0",
    "author": "Captivea LLC",
    "maintainer": "Captivea LLC",
    "website": "https://www.captivea.com",
    "category": "Inventory",
    "license": "AGPL-3",
    'summary': """Allow Connection to OpenAI API""",
    "depends": [
        "base",
        "product"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/chatgpt_config_view.xml",
        "views/menu.xml",
        "views/product_category_form_view.xml",
        "views/product_views.xml"
    ],
    "installable": True,
    "application": True,
}
