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

    @http.route(['/produto/<string:categoria>/<string:produto>'],
                type='http', auth="public", website=True)
    def redirect_product(self, categoria, produto):
        prod_env = request.env['product.template'].sudo()        
        categ_env = request.env['product.public.category'].sudo()
        categ = categ_env.search([('rota', '=', categoria)])        
        item = prod_env.search([('rota', '=', produto),
                                ('public_categ_ids', 'in', categ.ids)])        
        if len(item) >= 1:
            url = "/shop/product/%s" % slug(item[0])
            return http.redirect_with_hash(url)
        else:
            return request.website.render("website_sale.404")

    @http.route(['/categoria-produto/<string:categoria>'],
                type='http', auth="public", website=True)
    def redirect_category(self, categoria):
        prod_env = request.env['product.public.category'].sudo()
        item = prod_env.search([('rota', '=', categoria)])
        if len(item) >= 1:
            url = "/shop/category/%s" % slug(item[0])
            return http.redirect_with_hash(url)
        else:
            return request.website.render("website_sale.404")

    @http.route(
        ['/<string:pagina>/'], type='http', auth="public", website=True)
    def redirect_paginas(self, pagina):
        prod_env = request.env['page.redirect'].sudo()
        item = prod_env.search([('rota', '=', pagina)])
        if item:            
            return http.redirect_with_hash(u'/%s' % item.nova_rota)
        else:
            return request.website.render("website.404")        

