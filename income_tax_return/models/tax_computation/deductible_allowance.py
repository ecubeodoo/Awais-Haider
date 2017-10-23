# -*- coding: utf-8 -*-
###############################################################
########### Fields for WorkBook "Deductible Allowance" ##########
###############################################################

from openerp import models, fields, api

class deductible_allowance(models.Model):
	_name = 'deductible.allowance'

	description = fields.Char()
	deductible_allowance_ids = fields.Many2one('deductable.allowance','Deductible Allowance')
	amount      = fields.Float()
	ded_allowed        = fields.Float()

	deductible_allowance_id = fields.Many2one('tax.computation',ondelete='cascade', required=True)
	payment_id = fields.Many2one('payments',
		ondelete='cascade', string="Payments")
	income_under_ntr_id = fields.Many2one('income.under.ntr', string="Income UNTR ID")


	@api.onchange('amount')
	def _onchange_amount(self):
		if self.deductible_allowance_ids.name == 'Salary':
			self.ded_allowed = self.amount * 0.1