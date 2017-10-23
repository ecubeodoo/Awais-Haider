# -*- coding: utf-8 -*-
###############################################################
########### Fields for WorkBook "Income Under FTR" ##########
###############################################################

from openerp import models, fields, api

class income_under_ftr(models.Model):
	_name = 'income.under.ftr'

	description = fields.Char()
	amount      = fields.Float()
	rate        = fields.Many2one('final_tax.final_tax')
	tax         = fields.Float()
	receipt_type = fields.Selection([
		('ncr', 'Non Cash'),
		('income', 'Income'),
		('liability', 'Liability'),
		('capital_gain', 'Capital Gain'),
		('asset', 'Asset'),
		('sal', 'Salary'),
		('bus', 'Business'),
		('property', 'Property'),
		('oth_sour', 'Other Sources'),
		('cgt', 'CGT'),
		('foreign_remit', 'Foreign Remittance'),
		('arg_in', 'Agricultural Income'),
		])
	no_of_months   = fields.Integer()
	@api.onchange('amount','rate')
	def _onchange_ftr_vals(self):
		self.tax = self.amount * (self.rate.rate /100)

	income_under_ftr_id = fields.Many2one('tax.computation',ondelete='cascade')


	receipts_id = fields.Many2one('receipts',
        ondelete='cascade', string="Receipts")

	pnl_id = fields.Many2one('pnl.computation',
        ondelete='cascade', string="PNL Computation ID")