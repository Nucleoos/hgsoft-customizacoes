# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2015 TrustCode - www.trustcode.com.br                         #
#              Danimar Ribeiro <danimaribeiro@gmail.com>                      #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU Affero General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU General Public License for more details.                                #
#                                                                             #
# You should have received a copy of the GNU General Public License           #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#                                                                             #
###############################################################################


from openerp import models, api, fields
from openerp.models import NewId


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('order_line')
    def _onchange_order_line(self):
        for item in reversed(self.order_line):
            quantity = sum(
                1 for it in self.order_line if it.product_id.id == item.product_id.id)
            if quantity > 1:
                item.unlink()
                break
            print quantity

        return {}


class SaleOrdeLine(models.Model):
    _inherit = 'sale.order.line'

    def product_id_change_with_wh(self, cr, uid, ids, pricelist, product, qty=0,
                                  uom=False, qty_uos=0, uos=False, name='', partner_id=False,
                                  lang=False, update_tax=True, date_order=False, packaging=False,
                                  fiscal_position=False, flag=False, warehouse_id=False, context=None):

        product_obj = self.pool.get('product.product')
        product_info = product_obj.browse(cr, uid, product)
        warning = {
            'title': u'Atenção!',
            'message': 'Produto com estoque insuficiente!'}
        if product_info and product_info.type == 'product' and product_info.virtual_available < qty:
            return {'value': {'product_id': False}, 'warning': warning}

        result = super(SaleOrdeLine, self).product_id_change_with_wh(
            cr, uid, ids, pricelist, product, qty,
            uom, qty_uos, uos, name, partner_id,
            lang, update_tax, date_order, packaging, fiscal_position, flag, warehouse_id=warehouse_id, context=context)

        return result
