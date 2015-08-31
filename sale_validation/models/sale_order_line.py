'''
Created on 06/08/2015

@author: danimar
'''

from openerp import models, api, fields

class SaleOrdeLine(models.Model):
    _inherit = 'sale.order.line'

    def product_id_change_with_wh(self, cr, uid, ids, pricelist, product, qty=0,
            uom=False, qty_uos=0, uos=False, name='', partner_id=False,
            lang=False, update_tax=True, date_order=False, packaging=False,
            fiscal_position=False, flag=False, warehouse_id=False, context=None):
        
        result =  super(sale_order_line, self).product_id_change_with_wh( cr, uid, ids, pricelist, product, qty,
            uom, qty_uos, uos, name, partner_id,
            lang, update_tax, date_order, packaging, fiscal_position, flag, warehouse_id=warehouse_id, context=context)
        
        return result    
