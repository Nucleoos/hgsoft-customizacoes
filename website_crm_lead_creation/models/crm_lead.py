'''
Created on 06/08/2015

@author: danimar
'''
from openerp import models, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'
    
    @api.model
    def create(self, vals):
        return super(CrmLead, self).create(vals)
    
    @api.model
    def _lead_create_contact(self, lead, name, is_company, parent_id=False):
        partner_id = super(CrmLead, self)._lead_create_contact(lead, name,
                                                            is_company,
                                                            parent_id=parent_id)
        
        if not is_company:
            partner = self.env['res.partner'].browse(partner_id)
            self.env['res.users'].signup({'partner_id': partner.id , 'login': partner.email,
                                      'name': partner.name})            
            
        return partner_id