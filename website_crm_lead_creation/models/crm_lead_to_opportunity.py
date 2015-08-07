#coding=utf-8
'''
Created on 06/08/2015

@author: danimar
'''
from openerp import models, fields

class crm_lead2opportunity_partner(models.TransientModel):
    _inherit = 'crm.lead2opportunity.partner'
    
    create_user = fields.Boolean(string="Criar usuário", default=True)
    send_mail = fields.Boolean(string="Enviar e-mail", default=True)