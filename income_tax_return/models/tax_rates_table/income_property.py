# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# 
# 
# ---------------------------------------------------------------------
from openerp import models, fields, api

class income_from_property(models.Model):
	_name       = 'income.from.property'

	amount_from      = fields.Float()
	amount_to        = fields.Float()
	fixed_tax_amount = fields.Float()
	rate_of_tax      = fields.Float()

	income_from_property_id = fields.Many2one('tax_rates_table.tax_rates_table',
        ondelete='cascade', string="Income From Property", required=True)