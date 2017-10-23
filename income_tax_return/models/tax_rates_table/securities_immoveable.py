# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# 
# 
# ---------------------------------------------------------------------
from openerp import models, fields, api

class securities_immoveable(models.Model):
	_name       = 'securities.immoveable'

	period_from     = fields.Integer()
	period_to       = fields.Integer()
	rate        	= fields.Float()

	sec_immoveable_id = fields.Many2one('tax_rates_table.tax_rates_table',
        ondelete='cascade', string="Securities Immoveable", required=True)