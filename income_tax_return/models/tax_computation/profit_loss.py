# -*- coding: utf-8 -*-
###############################################################
########### Fields for WorkBook "Profit-Loss" ##########
###############################################################

from openerp import models, fields, api

class profit_loss(models.Model):
	_name = 'profit_loss.profit_loss'
	description = fields.Char(required=True)
	types       = fields.Selection([
		('income', 'Income'),
        ('direct_expenses', 'Direct Expenses'),
        ('indirect_expenses', 'Indirect Expenses'),
        ], default='indirect_expenses')
	admissible = fields.Selection([
		('admissible', 'Admissible'),
        ('in_admissible', 'In Admissible'),
        ('depreciation', 'Depreciation')
        ],'Admissible/ In Admissible', default='admissible')

	ntr        = fields.Float(string="NTR")
	ftr_exempt = fields.Float(string="FTR / Exempt")
	total      = fields.Float()
	profit_loss_ids = fields.Many2one('pnl.computation',
        ondelete='cascade')