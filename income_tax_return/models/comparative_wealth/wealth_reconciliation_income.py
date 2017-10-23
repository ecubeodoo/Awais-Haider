# -*- coding: utf-8 -*-
###########################################################################
###########  Fields for WorkBook "Wealth Reconciliation Income"###########
###########################################################################

from openerp import models, fields, api

class wealth_reconciliation_income(models.Model):
	_name = 'wealth.reconciliation.income'
	description = fields.Char(string = "Description")
	y2005 = fields.Float(string = "2005")
	y2006 = fields.Float(string = "2006")
	y2007 = fields.Float(string = "2007")
	y2008 = fields.Float(string = "2008")
	y2009 = fields.Float(string = "2009")
	y2010 = fields.Float(string = "2010")
	y2011 = fields.Float(string = "2011")
	y2012 = fields.Float(string = "2012")
	y2013 = fields.Float(string = "2013")
	y2014 = fields.Float(string = "2014")
	y2015 = fields.Float(string = "2015")
	y2016 = fields.Float(string = "2016")
	y2017 = fields.Float(string = "2017")
	y2018 = fields.Float(string = "2018")
	y2019 = fields.Float(string = "2019")
	y2020 = fields.Float(string = "2020")
	receipt_type = fields.Selection([
		('ntr', 'NTR'),
		('taxable', 'Taxable'),
        ('exempt', 'Exempt'),
        ('ftr', 'FTR'),
        ('minimum', 'Minimum'),
        ('salary', 'Salary'),
        ('sbi', 'SBI'),
        ])
	sequence = fields.Integer(string ='Sequence')
	_order   = 'sequence'

	wealth_income_id = fields.Many2one('comparative.wealth',
        ondelete='cascade', string="Wealth Reconciliation", required=True)
	receipt_id = fields.Many2one('receipts',
        ondelete='cascade', string="receipts")
	business_id = fields.Many2one('pnl.computation', 'Business ID')

	business_name_id = fields.Many2one('business.name',
        ondelete='cascade', string="Business Name ID")
