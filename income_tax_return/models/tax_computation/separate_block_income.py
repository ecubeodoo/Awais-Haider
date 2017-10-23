# -*- coding: utf-8 -*-
###############################################################
########### Fields for WorkBook "Income Under NTR" ##########
###############################################################

from openerp import models, fields, api

class separate_block_income(models.Model):
	_name = 'separate.block.income'

	description = fields.Char()
	amount      = fields.Float()

	receipt_type = fields.Selection([
		('sal', 'Salary'),
		('bus', 'Business'),
		('property', 'Property'),
		('oth_sour', 'Other Sources'),
		('cgt', 'CGT'),
		('foreign_remit', 'Foreign Remittance'),
		('arg_in', 'Agricultural Income'),
		])
	no_of_months   = fields.Integer()
	details = fields.Selection([
		('aca', 'Accquired After 1.7.2012'),
		('acb', 'Accquired Before 1.7.2012'),
        ('pme', 'Pakistan Mercantile Exchange'),
        ], string="Details")

	im_sec_type = fields.Selection([
		('imp', 'Immoveable Property'),
		('sec', 'Securites'),
        ], string="Type")
	separate_block_income_id = fields.Many2one('tax.computation',
		ondelete='cascade')
	tax = fields.Float()

	receipts_id = fields.Many2one('receipts',
        ondelete='cascade', string="Receipts")
