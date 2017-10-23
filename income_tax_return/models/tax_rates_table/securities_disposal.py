# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# 
# 
# ---------------------------------------------------------------------
from openerp import models, fields, api

class securities_disposal(models.Model):
	_name       = 'securities.disposal'

	period_from     = fields.Integer()
	period_to       = fields.Integer()
	rate        	= fields.Float()

	securities_disposal_id = fields.Many2one('tax_rates_table.tax_rates_table',
        ondelete='cascade', string="Securities Disposal", required=True)