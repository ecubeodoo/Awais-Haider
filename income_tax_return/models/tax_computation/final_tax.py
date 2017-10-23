# -*- coding: utf-8 -*-
###############################################################
########### Fields for WorkBook "Profit-Loss" ##########
###############################################################

from openerp import models, fields, api

class FinalTax(models.Model):
	_name = 'finaltax.finaltax'
	description = fields.Char()
	sales       = fields.Float(string="Sales")
	rate 		= fields.Float(string="Rate")
	profit      = fields.Float(string="Profit")
	tax 		= fields.Float(string="Tax")
	final_tax_id = fields.Many2one('pnl.computation',
        ondelete='cascade')


	@api.onchange('sales','rate')
	def calculate_tax(self):
		if self.sales and self.rate:
			self.tax = self.sales * (self.rate/100)