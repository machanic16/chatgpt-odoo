# Odoo-ChatGPT Integration

This repository contains two modules that integrate Odoo ERP System with OpenAI's ChatGPT using the OpenAI API. The purpose of these modules is to enhance the Odoo user experience by automating specific tasks such as generating product descriptions and summarizing customer communication threads. These modules leverage the power of OpenAI's ChatGPT language model to ensure the output is coherent, meaningful, and relevant.

## Modules

    1.Product Description Generator (cap_chat_gpt)
    2.Customer Communication Summary (summarize_history_chat)

## Installation

Before installing the modules, ensure that you have Odoo ERP System installed on your machine or server. You will also need to sign up for an OpenAI API key.

    Clone the repository to your local machine or server:

`git clone https://github.com/machanic16/chatgpt-odoo.git`

    Move the cap_chat_gpt and summarize_history_chat folders to your Odoo addons directory.

    Update the odoo.conf file with the following line to include the path to the addons directory

`addons_path = /path/to/your/addons`

    1.Restart your Odoo server.

    2.Log in to your Odoo instance and navigate to Apps.

    3.Search for ChatGPT and install the Product Description Generator and Customer Communication Summary modules.

    4.In the settings of each module, input your OpenAI API key to enable the integration.

## Usage
### Product Description Generator

This module generates product descriptions automatically for selected products in the Odoo ERP System using OpenAI's ChatGPT.

    1. Navigate to the Products menu under the Inventory app.

    2. Select the product you wish to generate descriptions for.

    3. Go to the tab "AI asisted description" 
    
    4. Click the buttom "Generate Description"

    5. The descriptions will be generated and automatically added to the selected product.

### Customer Communication Summary

This module generates a summary of a customer communication thread in one or two paragraphs, providing a quick overview of the conversation.

    1. Go to a sales order
    
    2. Click the tab "AI assisted summary"
    
    3. clic the buttom "Generate Summary"

    4. The summary will be generated and added to the communication thread as a new message.

## Contributing

Feel free to fork the repository and submit pull requests for any enhancements or bug fixes. For major changes, please open an issue first to discuss the proposed change.
License

This project is licensed under the MIT License - see the LICENSE.md file for details.
