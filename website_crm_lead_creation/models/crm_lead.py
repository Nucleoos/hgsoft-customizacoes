# coding=utf-8
'''
Created on 06/08/2015

@author: danimar
'''
from openerp import models, api
from openerp.exceptions import Warning
from psycopg2 import IntegrityError
from openerp.addons.auth_signup.res_users import SignupError


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def create(self, vals):
        return super(CrmLead, self).create(vals)

    @api.multi
    def handle_partner_assignation(self, action='create',
                                   partner_id=False, context=None):
        partner_ids = super(CrmLead, self).handle_partner_assignation(
            action=action, partner_id=partner_id, context=context)

        for lead in self:
            if lead.contact_name and lead.email_from and action == 'exist':
                partner_id = partner_ids[lead.id]
                partners = self.env['res.partner'].search([('parent_id', '=', partner_id),
                                                           ('email', '=', lead.email_from)])
                if len(partners) == 0:
                    self._lead_create_contact(
                        lead, lead.contact_name, False, partner_id)

        return partner_ids

    @api.model
    def _lead_create_contact(self, lead, name, is_company, parent_id=False):
        partner_id = super(CrmLead, self)._lead_create_contact(
            lead, name, is_company, parent_id=parent_id)

        if not is_company:
            try:
                partner = self.env['res.partner'].browse(partner_id)
                # if self.env.context.get('create_user', False):
                user = self.env['res.users'].signup({'partner_id': partner.id,
                                                     'login': partner.email,
                                                     'name': partner.name})
                # if self.env.context.get('send_email', False):
                users = self.env['res.users'].with_context(
                    {'create_user': True}).search([('login', '=', user[1])])
                users[0].action_reset_password()
            except SignupError:
                raise Warning(
                    'Um usuário já existe com o endereço de e-mail cadastrado')
            except Exception as ex:
                raise Warning(
                    u'Erro ao converter oportunidade:\n{0}'.format(
                        ex.message or ex.value))
        return partner_id
