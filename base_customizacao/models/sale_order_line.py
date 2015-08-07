'''
Created on 06/08/2015

@author: danimar
'''

from openerp import models, api, fields

class SaleOrdeLine(models.Model):
    _inherit = 'sale.order.line'
    
    @api.multi
    def _get_line_numbers(self):
        index = 1
        for line in self[0].order_id.order_line:
            line.line_number = index
            index += 1
    
    line_number = fields.Integer(string="Item", compute='_get_line_numbers', store=True)
    
    @api.model
    def default_get(self, fields_list):
        vals = super(SaleOrdeLine, self).default_get(fields_list)
        if 'ref_ids' in self.env.context.keys():
            vals.update({'line_number': len(self.env.context['ref_ids']) + 1 })
        return vals

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    @api.multi
    def _count_quantity(self):        
        for order in self:
            total = 0.0
            for line in self[0].order_line:
                total += line.product_uom_qty
            order.total_items = total
        
    total_items = fields.Float(string="Qtde Total",
                               digits=(18,2),compute='_count_quantity')
    
    
