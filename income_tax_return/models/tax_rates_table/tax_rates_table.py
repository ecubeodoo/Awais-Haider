# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# 
# 
# ---------------------------------------------------------------------
from openerp import models, fields, api

class tax_rates_table(models.Model):
	_name       = 'tax_rates_table.tax_rates_table'
	_inherit    = ['mail.thread', 'ir.needaction_mixin']

	tax_year    = fields.Many2one('account.fiscalyear', required=True)
	description = fields.Char()

	business_rates_table_ids = fields.One2many('business_individuals.business_individuals', 'business_individuals_id')
	salaried_rates_table_ids = fields.One2many('salaried_individuals.salaried_individuals', 'salaried_individuals_id')

	income_from_property_ids = fields.One2many('income.from.property', 'income_from_property_id')
	securities_disposal_ids = fields.One2many('securities.disposal', 'securities_disposal_id')
	securities_immoveable_ids = fields.One2many('securities.immoveable', 'sec_immoveable_id')