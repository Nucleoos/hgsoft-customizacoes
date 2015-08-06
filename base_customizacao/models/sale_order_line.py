'''
Created on 06/08/2015

@author: danimar
'''

from openerp import models, api

class sale_order_line(models.Model):
    _inherit = 'sale.order.line'
    
    @api.model
    def default_get(self, fields_list):
        vals = super(sale_order_line, self).default_get(fields_list)
        if 'ref_ids' in self.env.context.keys():
            vals.update({'sequence': len(self.env.context['ref_ids']) + 1 })
        return vals