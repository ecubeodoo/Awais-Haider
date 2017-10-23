# -*- coding: utf-8 -*-
###############################################################
########### Fields for WorkBook "Tax Credits" ##########
###############################################################

from openerp import models, fields, api

class tax_credits(models.Model):
	_name = 'tax.credits'

	description 		= fields.Char()
	amount      		= fields.Float()
	rate        		= fields.Float()
	tax         		= fields.Float()
	remarks     		= fields.Char()
	check_min_tax     	= fields.Boolean('Min Tax')

	@api.onchange('amount','rate')
	def _onchange_ftr_vals(self):
		self.tax = self.amount * (self.rate / 100)

	tax_credits_id = fields.Many2one('tax.computation',ondelete='cascade', required=True)

