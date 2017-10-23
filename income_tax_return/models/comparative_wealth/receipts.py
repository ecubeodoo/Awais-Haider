# -*- coding: utf-8 -*-
#####################################################
###########  Fields for WorkBook 'Receipts'##########
#####################################################

from openerp import models, fields, api

class receipts(models.Model):
	_name = 'receipts'
	description = fields.Char(string = "Description", required=True)
	capital_gain = fields.Many2one('capital_gain.capital_gain', domain="[('name','=',parent.name)]", string = 'Capital Gain', ondelete='cascade')

	non_cash_receipts = fields.Many2one('non.cash.receipts', domain="[('name','=',parent.name)]", string = 'Non Cash Receipts', ondelete='cascade')

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
	sequence = fields.Integer(string ='Sequence')
	_order   = 'sequence'

	receipt_type = fields.Selection([
			('ncr', 'Non Cash'),
            ('income', 'Income'),
            ('liability', 'Liability'),
            ('capital_gain', 'Capital Gain'),
            ('asset', 'Asset'),
            ])
	sub_type = fields.Selection([
            ('sal', 'Salary'),
            ('bus', 'Business'),
            ('property', 'Property'),
            ('oth_sour', 'Other Sources'),
            ('cgt', 'CGT'),
            ('foreign_remit', 'Foreign Remittance'),
            ('arg_in', 'Agricultural Income'),
            ])
	tax_type = fields.Selection([
		('ntr', 'NTR'),
		('sbi', 'SBI'),
        ('exempt', 'Exempt'),
        ('ftr', 'FTR'),
        ('minimum', 'Minimum'),
        # ('salary', 'Salary'),
        ])

	receipts_id = fields.Many2one('comparative.wealth',
        ondelete='cascade', string="Wealth Reconciliation", required=True)
	business_name_id = fields.Many2one('business.name',
        ondelete='cascade', string="Business Name ID")
	@api.multi
	def unlink(self):
		ncr_rcd = self.env['non.cash.receipts'].search([('id','=',self.non_cash_receipts.id)])
		cgt_rec = self.env['capital_gain.capital_gain'].search([('id','=',self.capital_gain.id)])
		cgt_rec.unlink()
		ncr_rcd.unlink()
		return super(receipts, self).unlink()
	# @api.model
	# def create(self, vals):
		
	# 	new_record = super(receipts, self).create(vals)
	# 	idd = str(new_record.id)
	# 	capital_gain_id = str(new_record.capital_gain.id)
	# 	print idd
	# 	print "xxxxxxxxxxxxxxxxxxxxx"
	# 	a_n_l_recs  = self.env.cr.execute('SELECT capital_gain,year_sale FROM capital_gain_capital_gain WHERE id =('+capital_gain_id+')')
	# 	a_n_l_recs_info = self.env.cr.fetchall()
	# 	print a_n_l_recs_info
	# 	amount  = str(a_n_l_recs_info[0][0])
	# 	year_id = str(a_n_l_recs_info[0][1])
	# 	years  = self.env.cr.execute('SELECT code FROM account_fiscalyear WHERE id =('+year_id+')')
	# 	a_n_l_years_info = self.env.cr.fetchall()
	# 	print a_n_l_years_info
	# 	year_code =  "y" + str(a_n_l_years_info[0][0])
	# 	# print year
	# 	self.env.cr.execute("update receipts set "+year_code+" =  "+amount+" WHERE id = "+idd+"")
	# 	return new_record    

