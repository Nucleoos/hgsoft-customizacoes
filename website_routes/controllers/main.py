'''
Created on 2 de set de 2015

@author: danimar
'''

import werkzeug

from openerp import http
from openerp.http import request
from openerp.tools.translate import _
from openerp.addons.web import http
from openerp.addons.website.models.website import slug
from openerp.addons.web.controllers.main import login_redirect



class RoutesRedirect(http.Controller):

    @http.route(['/produto/<string:categoria>/<string:produto>'], type='http', auth="public", website=True)
    def redirect_product(self, categoria, produto):
        print 'chegou aqui'
        print categoria
        print produto
        return http.redirect_with_hash('http://www.google.com')  
        
    @http.route(['/categoria-produto/<string:categoria>'], type='http', auth="public",  website=True)
    def redirect_category(self, categoria):
        print 'passou na categoria:'
        print categoria
        return http.redirect_with_hash('http://www.google.com')
    
    @http.route(['/<string:pagina>/'], type='http', auth="public",  website=True)
    def redirect_paginas(self, pagina):
        print 'passou na pagina'
        print pagina
        return http.redirect_with_hash('/')
        
        
        