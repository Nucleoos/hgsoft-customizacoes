'''
Created on 2 de set de 2015

@author: danimar
'''

import werkzeug

from openerp import http
from openerp.http import request
from openerp.tools.translate import _
from openerp.addons.website.models.website import slug
from openerp.addons.web.controllers.main import login_redirect

from openerp.addons.website_sale.controllers.main import website_sale


class WebsiteSale(website_sale):

    @http.route(['/shop/payment_term/<int:term_id>'], type='json', auth="public", website=True)
    def payment_transaction(self, term_id):
        cr, uid, context = request.cr, request.uid, request.context
        payment_obj = request.registry.get('payment.acquirer')
        sale_order_obj = request.registry.get('sale.order')

        order = request.website.sale_get_order(context=context)
        sale_order_obj.write(cr, uid, order.id, { 'payment_term': term_id })
        return True

    @http.route()
    def payment(self, **post):
        cr, uid, context = request.cr, request.uid, request.context
        payment_obj = request.registry.get('payment.acquirer')
        sale_order_obj = request.registry.get('sale.order')

        order = request.website.sale_get_order(context=context)        
        redirection = self.checkout_redirection(order)
        if redirection:
            return redirection

        result = super(WebsiteSale, self).payment(**post)        
        result.qcontext['payment_terms'] = request.env['account.payment.term'].search([])
        result.qcontext['payment_term_id'] = order.payment_term.id if order.payment_term else 0
        
        return result
        
          
        