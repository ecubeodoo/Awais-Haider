# -*- coding: utf-8 -*-
###############################################################
########### Fields for WorkBook "Rebate" ##########
###############################################################

from openerp import models, fields, api

class income_rebate(models.Model):
	_name = 'income.rebate'

	description = fields.Char()
	amount      = fields.Float()
	rate        = fields.Float()
	tax         = fields.Float()

	@api.onchange('amount','rate')
	def _onchange_ftr_vals(self):
		self.tax = self.amount * self.rate

	income_rebate_id = fields.Many2one('tax.computation',ondelete='cascade', required=True)