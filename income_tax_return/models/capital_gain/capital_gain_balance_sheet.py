# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# 
# 
# ---------------------------------------------------------------------
from openerp import models, fields, api

class capital_gain_balance_sheet(models.Model):

	_name      = 'capital_gain_balance_sheet.capital_gain_balance_sheet'
	_description = "Capital Gain Balance Sheet"
	_inherit   = ['mail.thread', 'ir.needaction_mixin']

	_rec_name = 'assets'



	name           = fields.Many2one('res.partner','Client Name', required=True)
	description    = fields.Char()
	year_purchase  = fields.Many2one('account.fiscalyear')
	year_sale      = fields.Many2one('account.fiscalyear')
	assets         = fields.Many2one('balance_sheet_sub_sub.balance_sheet_sub_sub')
	sale_value     = fields.Float()
	purchase_value = fields.Float()
	capital_gain   = fields.Float()
	sold_value   = fields.Float()
	remaining_value   = fields.Float()



