# -*- coding: utf-8 -*-
###############################################################
########### Fields for WorkBook "Income Under NTR" ##########
###############################################################

from openerp import models, fields, api

class income_under_ntr(models.Model):
	_name = 'income.under.ntr'

	description = fields.Char()
	amount      = fields.Float()
	min_wh      = fields.Float('Min Tax WH')
	tax_type    = fields.Selection([
		('ntr', 'NTR'),
		('ftr', 'FTR'),
		('exempt', 'Exempt'),
		('minimum', 'Minimum'),
		('bahbood', 'Bahbood/PBA'),
		])

	receipt_type = fields.Selection([
		('sal', 'Salary'),
		('bus', 'Business'),
		('property', 'Property'),
		('oth_sour', 'Other Sources'),
		('cgt', 'CGT'),
		('foreign_remit', 'Foreign Remittance'),
		('arg_in', 'Agricultural Income'),
		('sh_aop', 'Share From AOP'),
		])
	sub_tax_type    = fields.Selection([
		('nor', 'NTR'),
		('min', 'Minimum'),
		])
	no_of_months   = fields.Integer()
	income_under_ntr_id = fields.Many2one('tax.computation',
		ondelete='cascade')

	receipts_id = fields.Many2one('receipts',
        ondelete='cascade', string="Receipts")

	pnl_id = fields.Many2one('pnl.computation',
        ondelete='cascade', string="PNL Computation ID")
	mintax_id = fields.Many2one('minimumtax.minimumtax',
        ondelete='cascade', string="Minimum Tax ID")