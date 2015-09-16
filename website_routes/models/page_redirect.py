'''
Created on 15 de set de 2015

@author: danimar
'''


from openerp import models, api, fields


class PageRedirect(models.Model):
    _name = 'page.redirect'
    
    rota = fields.Char(u'Url antiga', size=200)
    nova_rota = fields.Char(u'Nova Url', size=200)