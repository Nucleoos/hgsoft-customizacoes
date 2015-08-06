'''
Created on 05/08/2015

@author: danimar
'''
from openerp import models, api

class product_product(models.Model):
    _inherit = 'product.product'
    
    @api.multi
    def name_get(self):
        return [(prod.id, 
                 u"[{0}] - {1}".format(prod.default_code,
                                      prod.name)) for prod in self]
