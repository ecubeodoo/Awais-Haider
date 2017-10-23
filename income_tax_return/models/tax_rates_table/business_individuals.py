# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# 
# 
# ---------------------------------------------------------------------
from openerp import models, fields, api

class business_individuals(models.Model):
	_name       = 'business_individuals.business_individuals'

	amount_from      = fields.Float()
	amount_to        = fields.Float()
	fixed_tax_amount = fields.Float()
	rate_of_tax      = fields.Float()

	business_individuals_id = fields.Many2one('tax_rates_table.tax_rates_table',
        ondelete='cascade', string="Business Individuals", required=True)