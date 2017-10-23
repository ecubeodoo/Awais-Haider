# -*- coding: utf-8 -*-
###############################################################
########### Fields for WorkBook "Income Under Exempt" ##########
###############################################################

from openerp import models, fields, api

class income_under_exempt(models.Model):
	_name = 'income.under.exempt'

	description = fields.Char()
	amount      = fields.Float()
	sub_type = fields.Selection([
			('sal', 'Salary'),
			('bus', 'Business'),
			('property', 'Property'),
			('oth_sour', 'Other Sources'),
			('cgt', 'CGT'),
			('foreign_remit', 'Foreign Remittance'),
			('arg_in', 'Agricultural Income'),
			])
	
	income_under_exempt_id = fields.Many2one('tax.computation',ondelete='cascade')


	receipts_id = fields.Many2one('receipts',
		ondelete='cascade', string="Receipts")
	pnl_id = fields.Many2one('pnl.computation', ondelete='cascade', string="PNL Computation ID")