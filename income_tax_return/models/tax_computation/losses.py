# -*- coding: utf-8 -*-
###############################################################
########### Fields for WorkBook "Deductible Allowance" ##########
###############################################################

from openerp import models, fields, api

class Losses(models.Model):
	_name = 'losses.losses'

	business_loss       = fields.Float(string="Business Losses")
	property_loss       = fields.Float(string="Property Losses")
	other_src_loss      = fields.Float(string="Losses From Other Sources")
	cg_loss      		= fields.Float(string="Captital Gain Losses")
	fr_remit_loss       = fields.Float(string="Foreign Losses")
	loss_type       	= fields.Selection([('loss', 'Loss'),('adj', 'Adjustment')],string="Type")
	tax_year            = fields.Many2one('account.fiscalyear',string="Tax Year")

	losses_id = fields.Many2one('tax.computation',ondelete='cascade', required=True)