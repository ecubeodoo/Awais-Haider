# -*- coding: utf-8 -*-
#####################################################
###########  Fields for WorkBook 'Payments'##########
#####################################################

from openerp import models, fields, api

class payments(models.Model):
	_name = 'payments'
	description = fields.Char(string = "Description", required=True)
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
	hidden_id = fields.Boolean(string="Hidden Id", default=False,)
	sequence = fields.Integer(string ='Sequence')
	_order   = 'sequence'
	
	receipt_type = fields.Selection([
			('ded_all', 'Deductible Allowance'),
            ('expense', 'Expense'),
            ('asset', 'Asset'),
            ('loan_repayment', 'Loan Repayment'),
            ])
	
	deductible_allowance_ids = fields.Many2one('deductable.allowance','Dedutable Allowance')

	tax_type    = fields.Selection([
        ('adjustable', 'Adjustable'),
        ('minimum', 'Minimum'),
		('tax_ftr', 'Tax FTR'),
		('deductible_allowance', 'Deductible Allowance'),
		('sbi','SBI (IMM)'),
		('sbi_sec','SBI (SEC)')
        ])

	sub_type = fields.Selection([
            ('sal', 'Salary'),
            ('bus', 'Business'),
            ('property', 'Property'),
            ('oth_sour', 'Other Sources'),
            ('cgt', 'CGT'),
            ])

	payments_id = fields.Many2one('comparative.wealth',
        ondelete='cascade', string="Wealth Reconciliation")

	receipts_id = fields.Many2one('receipts',
        ondelete='cascade', string="Receipts")

	business_name_id = fields.Many2one('business.name',
        ondelete='cascade', string="Business Name ID")