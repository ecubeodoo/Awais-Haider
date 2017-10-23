# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# 
# 
# ---------------------------------------------------------------------
from openerp import models, fields, api
import datetime as dt
from openerp.exceptions import Warning

class comparative_wealth(models.Model):

	_name                             = 'comparative.wealth'
	_description                      = 'Comparative Wealth'
	_inherit                          = ['mail.thread', 'ir.needaction_mixin']
	name                              = fields.Many2one('res.partner','Client Name', required=True, track_visibility='always')
	# _defaults                         = { 'name': lambda self,cr,uid,context={}: self.pool.get('ir.sequence').get(cr, uid, 'comparative.wealth'), }
	# name                              = fields.Char(string="Name")
	all_years                         = fields.Boolean(string="All Years", default=True)
	group                             = fields.Many2one('res.partner')

	wealth_assets_id                  = fields.One2many('wealth.assets', 'assets_id')
	wealth_assets_ids                 = fields.One2many('wealth.assets', 'assets_id')
	wealth_liability_id               = fields.One2many('wealth.liability', 'liability_id')
	wealth_liability_ids              = fields.One2many('wealth.liability', 'liability_id')
	wealth_reconciliation_opening_id  = fields.One2many('wealth.reconciliation.open', 'wealth_open_id')
	wealth_reconciliation_opening_ids = fields.One2many('wealth.reconciliation.open', 'wealth_open_id')	
	wealth_reconciliation_income_id   = fields.One2many('wealth.reconciliation.income', 'wealth_income_id')
	wealth_reconciliation_income_ids  = fields.One2many('wealth.reconciliation.income', 'wealth_income_id')
	wealth_reconciliation_expense_id  = fields.One2many('wealth.reconciliation.expense', 'wealth_expense_id')
	wealth_reconciliation_expense_ids = fields.One2many('wealth.reconciliation.expense', 'wealth_expense_id')
	cash_opening_id                   = fields.One2many('opening', 'opening_id')
	cash_opening_ids                  = fields.One2many('opening', 'opening_id')
	cash_receipts_id                  = fields.One2many('receipts', 'receipts_id')
	cash_receipts_ids                 = fields.One2many('receipts', 'receipts_id')
	cash_payments_id                  = fields.One2many('payments', 'payments_id')
	cash_payments_ids                 = fields.One2many('payments', 'payments_id')
	cash_reconciliation_balance_id    = fields.One2many('reconciliation.balance', 'reconciliation_balance_id')
	cash_reconciliation_balance_ids   = fields.One2many('reconciliation.balance', 'reconciliation_balance_id')
	cash_closing_1_id                 = fields.One2many('closing_1.closing_1', 'closing_1_id')
	cash_closing_1_ids                = fields.One2many('closing_1.closing_1', 'closing_1_id')
	cash_closing_2_id                 = fields.One2many('closing_2.closing_2', 'closing_2_id')
	cash_closing_2_ids                = fields.One2many('closing_2.closing_2', 'closing_2_id')
	capital_working_workbook_id       = fields.One2many('capital_working.capital_working', 'capital_working_id')
	capital_working_workbook_ids      = fields.One2many('capital_working.capital_working', 'capital_working_id')
	balance_sheet_workbook_ids      = fields.One2many('balance_sheet.balance_sheet', 'balance_sheet_id')

	ttl_2011 = fields.Float(string="Total_2011 : " )
	ttl_2012 = fields.Float(string="Total_2012 : " )
	ttl_2013 = fields.Float(string="Total_2013 : " )
	ttl_2014 = fields.Float(string="Total_2014 : " )
	ttl_2015 = fields.Float(string="Total_2015 : " )
	ttl_2016 = fields.Float(string="Total_2016 : " )
	ttl_2017 = fields.Float(string="Total_2017 : " )
	ttl_2018 = fields.Float(string="Total_2018 : " )
	ttl_2019 = fields.Float(string="Total_2019 : " )
	ttl_2020 = fields.Float(string="Total_2020 : " )


	total_2005 = fields.Float(string="Total_2005 : ")
	total_2006 = fields.Float(string="Total_2006 : ")
	total_2007 = fields.Float(string="Total_2007 : ")
	total_2008 = fields.Float(string="Total_2008 : ")
	total_2009 = fields.Float(string="Total_2009 : ")
	total_2010 = fields.Float(string="Total_2010 : ")
	total_2011 = fields.Float(string="Total_2011 : ")
	total_2012 = fields.Float(string="Total_2012 : ")
	total_2013 = fields.Float(string="Total_2013 : ")
	total_2014 = fields.Float(string="Total_2014 : ")
	total_2015 = fields.Float(string="Total_2015 : ")
	total_2016 = fields.Float(string="Total_2016 : ")
	total_2017 = fields.Float(string="Total_2017 : ")
	total_2018 = fields.Float(string="Total_2018 : ")
	total_2019 = fields.Float(string="Total_2019 : ")
	total_2020 = fields.Float(string="Total_2020 : ")

	_sql_constraints = [
        ('name_uniq', 'UNIQUE (name)',  'You can not have two users with the same name !')
    ]
#########################################################################################################
################################# New Refactor Code #####################################################

	@api.model
	def create(self, vals):
		result = super(comparative_wealth, self).create(vals)
		self.getReceiptsColumns()
		return result

	@api.multi
	def write(self, vals):
		result = super(comparative_wealth, self).write(vals)
		self.getReceiptsColumns()
		self.createReceiptIncome()
		self.createPaymentExpense()
		self.sendCashBankOpening()
		self.createLiabilityRecords()
		self.assetsMain()
		# self.createPaymentAssets()
		# self.createNCRAssets()
		# self.deductCapitalAmount()
		# self.getNCRRecieptValues()
		self.sendNCRIncome()
		self.sendNCRPayments()
		self.sendCapitalGainIncome()
		self.createCashBankAssets()
		# self.createPaymentOnCreateAssets()
		self.getCashDifference()
		self.createWealthStClosing()
		self.createOpeningReconcil()
		self.createReconcilClosing()
		self.getReconciliationDiff()
		self.delCapitalGain()
		# self.createNtrFromReciepts()
		self.update()
		return result

	def getReceiptsColumns(self):
		if self.cash_receipts_ids:
			for line in self.cash_receipts_ids:
				if line.capital_gain:
					for rec in line.capital_gain.capital_gain_ids: 
						year = 'y'+rec.year_sale.code
						if rec.year_sale.code:
							if 'y'+rec.year_sale.code == line.browse(year).id:
								self.env.cr.execute("update receipts set "+str(line.browse(year).id)+" =  "+str(rec.sale_value)+" WHERE id = "+str(line.id)+"")


	def getCashDifference(self):
		cw_fields = "total_20"
		op_fields = "y20"
		for x in xrange(10,25):
			cw_req_field = cw_fields+str(x)
			op_req_field = op_fields + str(x)
			total_opening = self.getValues("opening",op_req_field,"opening_id")
			total_receipts =  self.getValues("receipts",op_req_field,"receipts_id")
			total_payments =  self.getValues("payments",op_req_field,"payments_id")
			total_closing = self.getValues("reconciliation_balance",op_req_field,"reconciliation_balance_id")
			if total_opening != None and total_receipts != None and total_payments != None and total_closing != None:
				net = (total_opening + total_receipts) - (total_payments + total_closing)
				self.env.cr.execute("update comparative_wealth set "+str(cw_req_field)+" =  "+str(net)+" WHERE id = "+str(self.id)+"")

	def getReconciliationDiff(self):
		if self.cash_closing_2_ids or self.cash_closing_1_ids:
			cw_fields = "ttl_20"
			op_fields = "y20"
			for x in xrange(11,25):
				cw_req_field = cw_fields+str(x)
				op_req_field = op_fields + str(x)
				wealth_statement_closing =  self.getValues("closing_2_closing_2",op_req_field,"closing_2_id")
				wealth_recon_closing =  self.getValues("closing_1_closing_1",op_req_field,"closing_1_id")
				if wealth_statement_closing != None and wealth_recon_closing != None:
					net = (wealth_statement_closing - wealth_recon_closing)
					self.env.cr.execute("update comparative_wealth set "+str(cw_req_field)+" =  "+str(net)+" WHERE id = "+str(self.id)+"")

	def getValues(self, table_name, column_name, parent_id):
		result = 0
		self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = '"+table_name+"' AND COLUMN_NAME = '"+column_name+"'")
		check_column = self.env.cr.fetchone()
		if check_column != None:
			self.env.cr.execute("select SUM("+column_name+")  FROM "+table_name+" WHERE "+parent_id+" = "+str(self.id)+"")
			total = self.env.cr.fetchone()[0]
			if total != None:
				result = result + total
			return result

	def createReceiptIncome(self):
		income_record = self.wealth_reconciliation_income_ids.search([('wealth_income_id','=',self.id)])
		income_record.unlink()
		if self.cash_receipts_ids:
			income_ids = ['income','sal','bus','property','oth_sour','cgt','foreign_remit','arg_in']
			for line in self.cash_receipts_ids.search([('receipt_type','=','income'),('receipts_id.id','=',self.id)]):
				self.wealth_reconciliation_income_ids.create({
					'description' : line.description,
					'receipt_type': line.tax_type,
					'wealth_income_id' : self.id,
					'receipt_id': line.id
					})
				self.insertValues("receipts", "wealth_reconciliation_income", "receipt_id")

	def createPaymentExpense(self):
		expense_record = self.wealth_reconciliation_expense_ids.search([('wealth_expense_id','=',self.id)])
		expense_record.unlink()
		if self.cash_payments_ids:
			for line in self.cash_payments_ids.search([('receipt_type','in',['expense','ded_all']),('payments_id.id','=',self.id)]):
				self.wealth_reconciliation_expense_ids.create({
					'description' : line.description,
					'receipt_type': line.tax_type,
					'wealth_expense_id' : self.id,
					'payment_id': line.id
					})
				self.insertValues("payments", "wealth_reconciliation_expense", "payment_id")


	def assetsMain(self):
		for line in self.cash_payments_ids.search([('receipt_type','=','asset'),('payments_id.id','=',self.id)]):
			if not self.wealth_assets_ids.search([('payment_id','=',line.id)]):
				record = self.wealth_assets_ids.create({
					'description' : line.description,
					'assets_id' : self.id,
					'payment_id': line.id
					})
			record_fields = "y20"
			for x in xrange(10,25):
				record_field = record_fields+str(x)  # it starts with y2010 and ends at y2024
				self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = 'payments' AND COLUMN_NAME = '"+record_field+"'")
				check_column = self.env.cr.fetchone() ####2016
				emp_list = 0
				if check_column != None:
					for y in xrange(10,x+1):
						record_new = record_fields + str(y)
						self.env.cr.execute("select ("+record_new+")  FROM payments WHERE id = "+str(line.id)+" ")
						amount = self.env.cr.fetchone()[0]
						if amount != None:
							emp_list = emp_list + amount

					AssetsRecord = self.env['wealth.assets'].search([('payment_id','=',line.id)])
					ncr_records = self.env['non.cash.receipts'].search([('assets','=',AssetsRecord.id)])
					ncr_list = 0
					if ncr_records:
						for ncr in ncr_records.non_receipt_ids:
							if ncr.ncr_year.code <= "20"+str(x):
								ncr_list = ncr_list + ncr.ncr_addition
					CgtRecords = self.env['capital_gain.capital_gain'].search([('assets','=',AssetsRecord.id)])
					cgt_list = 0
					if CgtRecords:
						for cgt in CgtRecords.capital_gain_ids:
							if cgt.year_sale.code <= "20"+str(x):
								cgt_list = cgt_list + cgt.sold_value
					self.env.cr.execute("UPDATE wealth_assets SET    "+record_field+" = "+str(ncr_list + emp_list - cgt_list )+"  WHERE  payment_id = "+str(line.id)+"")

		for line in self.cash_receipts_ids.search([('receipt_type','=','ncr'),('receipts_id.id','=',self.id)]):
			if not self.wealth_assets_ids.search([('receipts_id','=',line.id)]):
				record = self.wealth_assets_ids.create({
					'description' : line.description,
					'assets_id' : self.id,
					'receipts_id': line.id
					})
				if line.non_cash_receipts:
					line.non_cash_receipts.assets = record.id
			record_fields = "y20"
			for x in xrange(10,25):
				record_field = record_fields+str(x)  # it starts with y2010 and ends at y2024
				self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = 'receipts' AND COLUMN_NAME = '"+record_field+"'")
				check_column = self.env.cr.fetchone() ####2016
				ncr_addition = 0
				ncr_cash_amount = 0
				total_ncr = 0 
				if check_column != None:
					for ncr in line.non_cash_receipts.non_receipt_ids:
						if ncr.ncr_year.code <= "20"+str(x):
							ncr_addition = ncr_addition + ncr.ncr_addition
							ncr_cash_amount = ncr_cash_amount + ncr.ncr_cash
							print ncr_cash_amount
							print "20"+str(x)
					total_ncr = ncr_addition + ncr_cash_amount
					AssetsRecord = self.env['wealth.assets'].search([('receipts_id','=',line.id)])
					CgtRecords = self.env['capital_gain.capital_gain'].search([('assets','=',AssetsRecord.id)])
					cgt_list = 0
					if CgtRecords:
						for cgt in CgtRecords.capital_gain_ids:
							if cgt.year_sale.code <= "20"+str(x):
								cgt_list = cgt_list + cgt.sold_value
					self.env.cr.execute("UPDATE wealth_assets SET    "+record_field+" = "+str(total_ncr - cgt_list )+"  WHERE  receipts_id = "+str(line.id)+"")


	def createPaymentAssets(self):
		for line in self.cash_payments_ids.search([('receipt_type','=','asset'),('payments_id.id','=',self.id)]):
			if not self.wealth_assets_ids.search([('payment_id','=',line.id)]):
				record = self.wealth_assets_ids.create({
					'description' : line.description,
					'assets_id' : self.id,
					'payment_id': line.id
					})
				record_fields = "y20"
				for x in xrange(10,25):
					record_field = record_fields+str(x)  # it starts with y2010 and ends at y2024
					self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = 'payments' AND COLUMN_NAME = '"+record_field+"'")
					check_column = self.env.cr.fetchone() ####2016
					if check_column != None:
						emp_list = 0
						for y in xrange(10,x+1):
							record_new = record_fields + str(y)
							self.env.cr.execute("select ("+record_new+")  FROM payments WHERE id = "+str(line.id)+" ")
							amount = self.env.cr.fetchone()[0]
							if amount != None:
								emp_list = emp_list + amount
						ncr_records = self.env['non.cash.receipts'].search([('assets','=',record.id)])
						if ncr_records:
							for ncr in ncr_records.non_receipt_ids:
								if ncr.ncr_year.code == "20"+str(x):
									ncr_list = 0
									for z in xrange(10,(int(ncr.ncr_year.code)+1) ):
										record_new = "20" + str(z)
										self.env.cr.execute("select ncr_addition  FROM non_cash_receipts_tree  WHERE ncr_year = "+record_new+" id = "+str(ncr.id)+" ")
										amount = self.env.cr.fetchone()[0]
										if amount != None:
											ncr_list = ncr_list + amount
									print ncr_list
									if ncr.ncr_addition:
										self.env.cr.execute("UPDATE wealth_assets SET    "+record_field+" = "+str(emp_list+ncr_list)+"  WHERE  payment_id = "+str(line.id)+"")
						else:
							self.env.cr.execute("UPDATE wealth_assets SET    "+record_field+" = "+str(emp_list)+"  WHERE  payment_id = "+str(line.id)+"")
			elif self.wealth_assets_ids.search([('payment_id','=',line.id)]):
				self.wealth_assets_ids.search([('payment_id','=',line.id)]).description = line.description
				record_fields = "y20"
				for x in xrange(10,25):
					record_field = record_fields+str(x)  # it starts with y2010 and ends at y2024
					self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = 'payments' AND COLUMN_NAME = '"+record_field+"'")
					check_column = self.env.cr.fetchone() ####2016
					if check_column != None:
						emp_list = 0
						for y in xrange(10,x+1):
							record_new = record_fields + str(y)
							self.env.cr.execute("select ("+record_new+")  FROM payments WHERE id = "+str(line.id)+" ")
							amount = self.env.cr.fetchone()[0]
							if amount != None:
								emp_list = emp_list + amount
						wealth_assets_record = self.env['wealth.assets'].search([('payment_id','=',line.id)])
						ncr_records = self.env['non.cash.receipts'].search([('assets','=',wealth_assets_record.id)])
						if ncr_records:
							for ncr in ncr_records.non_receipt_ids:
								if ncr.ncr_year.code == "20"+str(x):
									if ncr.ncr_addition:
										self.env.cr.execute("UPDATE wealth_assets SET    "+record_field+" = "+str(emp_list+ncr.ncr_addition)+"  WHERE  payment_id = "+str(line.id)+"")
						else:
							self.env.cr.execute("UPDATE wealth_assets SET    "+record_field+" = "+str(emp_list)+"  WHERE  payment_id = "+str(line.id)+"")
		if self.cash_receipts_ids:
			self.updateCapitalGainRecords()

	def addPreColumnsAssets(self, start_value, end_value,  table_name , line_id):
					previous = 0
					record_fields = "y20"
					for x in xrange(start_value,end_value):
						pre_field = record_fields+str(x)
						self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = '"+table_name+"' AND COLUMN_NAME = '"+pre_field+"'")
						pre_column = self.env.cr.fetchone()
						if pre_column != None:
							self.env.cr.execute("select SUM("+pre_field+")  FROM "+table_name+" WHERE id = "+str(line_id)+" ")
							pre_total = self.env.cr.fetchone()[0]
							if pre_total != None:
								previous = previous + pre_total
					return previous

	def insertValues(self, compared_table, update_table, update_table_id ):
		record_fields = "y20"
		for x in xrange(10,25):
			record_field = record_fields+str(x)
			self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = '"+compared_table+"' AND COLUMN_NAME = '"+record_field+"'")
			check_column = self.env.cr.fetchone()
			if check_column != None:
				self.env.cr.execute("UPDATE "+update_table+" b SET    "+record_field+" = a."+record_field+" FROM   "+compared_table+" a WHERE  b."+update_table_id+" = a.id")

	def sendCashBankOpening(self):
		expense_record = self.cash_opening_ids.search([('opening_id','=',self.id)])
		expense_record.unlink()
		if self.cash_reconciliation_balance_ids:
			for line in self.cash_reconciliation_balance_ids.search([('reconciliation_balance_id','=',self.id)]):
				self.cash_opening_ids.create({
					'description' : line.description,
					'receipt_type': line.receipt_type,
					'opening_id' : self.id,
					'reconciliation_id': line.id
					})
				self.InsertOpeningReconiliation("reconciliation_balance", "opening", "reconciliation_id")

	def InsertOpeningReconiliation(self, compared_table, update_table, update_table_id):
		record_fields = "y20"
		for x in xrange(10,25):
			record_field = record_fields+str(x)
			update_record_field = record_fields+str(x+1)
			self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = '"+update_table+"' AND COLUMN_NAME = '"+record_field+"'")
			column_record_field = self.env.cr.fetchone()			
			self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = '"+compared_table+"' AND COLUMN_NAME = '"+update_record_field+"'")
			column_update_record_field = self.env.cr.fetchone()
			if column_record_field != None and column_update_record_field != None:
				self.env.cr.execute("UPDATE "+update_table+" b SET    "+update_record_field+" = a."+record_field+" FROM   "+compared_table+" a WHERE  b."+update_table_id+" = a.id")
				
	def createLiabilityRecords(self):
		liability_records = self.wealth_liability_ids.search([('liability_id','=',self.id)])
		liability_records.unlink()
		if self.cash_receipts_ids:
			for line in self.cash_receipts_ids.search([('receipt_type','=','liability'),('receipts_id','=',self.id)]):
				if self.cash_payments_ids:
					for rec in self.cash_payments_ids.search([('receipt_type','=','loan_repayment'),('payments_id','=',self.id)]):
						if line.description == rec.description:
							if not self.wealth_liability_ids.search([('receipt_id','=',line.id)]):
								self.wealth_liability_ids.create({
									'description' : line.description,
									'liability_id' : self.id,
									'receipt_id': line.id
									})
								record_fields = "y20"
								for x in xrange(10,25):
									record_field = record_fields+str(x-1)
									self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = 'receipts' AND COLUMN_NAME = '"+record_field+"'")
									check_column = self.env.cr.fetchone()
									if check_column != None:
										recipts = self.addPreColumnsAssets(10, x, 'receipts', line.id)
										payments = self.addPreColumnsAssets(10, x, 'payments', rec.id)
										if recipts != None and payments != None:
											result = recipts - payments
											self.env.cr.execute("UPDATE wealth_liability SET "+record_field+" = "+str(result)+"  WHERE  receipt_id = "+str(line.id)+"")


		if self.cash_receipts_ids:
			for recipt in self.cash_receipts_ids.search([('receipt_type','=','liability'),('receipts_id','=',self.id)]):
				if len(self.cash_payments_ids.search([('receipt_type','=','loan_repayment'),('payments_id','=',self.id)])) == 0:
					self.wealth_liability_ids.create({
						'description' : recipt.description,
						'liability_id' : self.id,
						'receipt_id': recipt.id
						})
					record_fields = "y20"
					for x in xrange(10,25):
						record_field = record_fields+str(x-1)
						self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = 'receipts' AND COLUMN_NAME = '"+record_field+"'")
						check_column = self.env.cr.fetchone()
						if check_column != None:
							recipts = recipts = self.addPreColumnsAssets(10, x, 'receipts', recipt.id)
							if recipts != None:
								self.env.cr.execute("UPDATE wealth_liability SET "+record_field+" = "+str(recipts)+"  WHERE  receipt_id = "+str(recipt.id)+"")
				else:
					for record in self.cash_payments_ids.search([('receipt_type','=','loan_repayment'),('payments_id','=',self.id)]):
						if not self.wealth_liability_ids.search([('description','=',recipt.description)]):
							self.wealth_liability_ids.create({
								'description' : recipt.description,
								'liability_id' : self.id,
								'receipt_id': recipt.id
								})
							record_fields = "y20"
							for x in xrange(10,25):
								record_field = record_fields+str(x-1)
								self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = 'receipts' AND COLUMN_NAME = '"+record_field+"'")
								check_column = self.env.cr.fetchone()
								if check_column != None:
									recipts = recipts = self.addPreColumnsAssets(10, x, 'receipts', recipt.id)
									if recipts != None:
										self.env.cr.execute("UPDATE wealth_liability SET "+record_field+" = "+str(recipts)+"  WHERE  receipt_id = "+str(recipt.id)+"")

		if self.cash_payments_ids:
			for payments in self.cash_payments_ids.search([('receipt_type','=','loan_repayment'),('payments_id','=',self.id)]):
				loan_repayment_rec = self.cash_receipts_ids.search([('receipt_type','=','liability'),('receipts_id','=',self.id),('description','=',payments.description)])
				if not loan_repayment_rec:
					raise Warning("Description of Liability or Loan Payments records does not match.")


	def sendCapitalGainIncome(self):
		if self.cash_receipts_ids:
			for line in self.cash_receipts_ids:
				if line.capital_gain:
					for rec in line.capital_gain.capital_gain_ids:
						year = 'y'+rec.year_sale.code
						if rec.year_sale.code:
							if rec.capital_gain > 0:
								old_wealth_record = self.wealth_reconciliation_income_ids.search([('description','=',line.capital_gain.assets.description),('wealth_income_id','=',self.id)])
								if not old_wealth_record:
									record = self.wealth_reconciliation_income_ids.create({
										'description' : line.capital_gain.assets.description,
										'wealth_income_id':self.id,
										})
									if 'y'+rec.year_sale.code == line.browse(year).id:
										self.env.cr.execute("update wealth_reconciliation_income set "+str(line.browse(year).id)+" =  "+str(rec.capital_gain)+" WHERE id = "+str(record.id)+"")
								else:
									if 'y'+rec.year_sale.code == line.browse(year).id:
										# ncr_records = self.env['non.cash.receipts'].search([('assets','=',line.capital_gain.assets.id)])
										# for ncr in ncr_records.non_receipt_ids:
										# 	if ncr.ncr_year.code == rec.year_sale.code:
										# 		if ncr.ncr_addition:
										self.env.cr.execute("update wealth_reconciliation_income set "+str(line.browse(year).id)+" =  "+str(rec.capital_gain)+" WHERE id = "+str(old_wealth_record.id)+"")
							elif rec.capital_gain < 0:
								old_wealth_record = self.wealth_reconciliation_expense_ids.search([('description','=',line.capital_gain.assets.description),('wealth_expense_id','=',self.id)])
								if not old_wealth_record:
									record = self.wealth_reconciliation_expense_ids.create({
										'description' : line.capital_gain.assets.description,
										'wealth_expense_id':self.id,
										})
									if 'y'+rec.year_sale.code == line.browse(year).id:
										self.env.cr.execute("update wealth_reconciliation_expense set "+str(line.browse(year).id)+" =  "+str(rec.capital_gain * -1)+" WHERE id = "+str(record.id)+"")
								else:
									if 'y'+rec.year_sale.code == line.browse(year).id:
										self.env.cr.execute("update wealth_reconciliation_expense set "+str(line.browse(year).id)+" =  "+str(rec.capital_gain * -1)+" WHERE id = "+str(old_wealth_record.id)+"")

######################################### Sending Capital Gain Yearly amount in same year of wealth_reconciliation_income###############

	def deductCapitalAmount(self):
		if self.cash_receipts_ids:
			for line in self.cash_receipts_ids:
				if line.capital_gain:
					for rec in line.capital_gain.capital_gain_ids:
						year = 'y'+rec.year_sale.code
						if rec.year_sale.code:
							if 'y'+rec.year_sale.code == line.browse(year).id:
								if line.capital_gain.assets:
									assets_recd = line.capital_gain.assets.browse(year).id
									asset_updated_value = rec.remaining_value
									for x in xrange(int(rec.year_sale.code),int(rec.year_sale.code)+3):
										field = 'y'+str(x)
										self.env.cr.execute("update wealth_assets set "+field+" =  "+str(asset_updated_value)+" WHERE id = "+str(line.capital_gain.assets.id)+"")

########################## Update wealth assets and send remaining value of capital assets in same year of assets ###################################################################################################
	def updateCapitalGainRecords(self):
		if self.cash_receipts_ids:
			for line, record in ((cash,assets) for cash in self.cash_receipts_ids for assets in self.wealth_assets_ids):
				if line.description == record.description:
					if line.capital_gain.assets:
						line.capital_gain.assets = record.id
						sold_value = 0
						for rec in line.capital_gain.capital_gain_ids:
							assets_recd = line.capital_gain.assets.browse("y"+str(int(rec.year_sale.name))).id
							self.env.cr.execute("select "+assets_recd+"  FROM wealth_assets WHERE id = "+str(line.capital_gain.assets.id)+" ")
							asset_value = self.env.cr.fetchone()[0]
							if asset_value != None and asset_value > 0:
								sold_value = sold_value + rec.sold_value
								rec.purchase_value = asset_value
								rec.capital_gain = rec.sale_value - rec.sold_value
								rec.remaining_value = rec.purchase_value - sold_value

	def createCashBankAssets(self):
		if self.cash_reconciliation_balance_ids:
			for line in self.cash_reconciliation_balance_ids:
				assets_record = self.wealth_assets_ids.search([('cash_bank_id','=',line.id)])
				assets_record.unlink()
				self.wealth_assets_ids.create({
					'description' : line.description,
					'assets_id' : self.id,
					'cash_bank_id': line.id
					})
				self.insertValues("reconciliation_balance", "wealth_assets", "cash_bank_id")
	
	def createReconcilClosing(self):
		if self.cash_closing_1_ids:
			self.cash_closing_1_ids.unlink()
		if not self.cash_closing_1_ids:
			self.cash_closing_1_ids.create({
				'description' : "Closing",
				'closing_1_id' : self.id,
				})
			rec_fields = "y20"
			for x in xrange(11,25):
				rec_field = rec_fields + str(x)
				if self.wealth_reconciliation_opening_ids or self.wealth_reconciliation_income_ids or self.wealth_reconciliation_expense_ids:
					total_opening = self.getValues("wealth_reconciliation_open",rec_field,"wealth_open_id")
					total_income = self.getValues("wealth_reconciliation_income",rec_field,"wealth_income_id")
					total_expense = self.getValues("wealth_reconciliation_expense",rec_field,"wealth_expense_id")
					if total_opening != None and total_income != None and total_expense != None:
						net = (total_opening + total_income) - total_expense
						self.env.cr.execute("update closing_1_closing_1 set "+str(rec_field)+" =  "+str(net)+" WHERE id = "+str(self.id)+"")
		if self.cash_closing_1_ids:
			if len(self.cash_closing_1_ids) > 1:
				raise Warning("You have more than one Record in  Wealth Reconcilation Closing.")
			else:
				rec_fields = "y20"
				for x in xrange(11,25):
					rec_field = rec_fields + str(x)
					total_opening = self.getValues("wealth_reconciliation_open",rec_field,"wealth_open_id")
					total_income = self.getValues("wealth_reconciliation_income",rec_field,"wealth_income_id")
					total_expense = self.getValues("wealth_reconciliation_expense",rec_field,"wealth_expense_id")
					if total_opening != None and total_income != None and total_expense != None:
						net = (total_opening + total_income) - total_expense
						self.env.cr.execute("update closing_1_closing_1 set "+str(rec_field)+" =  "+str(net)+" WHERE id = "+str(self.cash_closing_1_ids[0].id)+"")

	def createWealthStClosing(self):
		if self.cash_closing_2_ids:
			self.cash_closing_2_ids.unlink()
		if not self.cash_closing_2_ids:
			self.cash_closing_2_ids.create({
				'description' : "Closing",
				'closing_2_id' : self.id,
				})
			rec_fields = "y20"
			for x in xrange(11,25):
				rec_field = rec_fields + str(x)
				if self.wealth_assets_ids or self.wealth_liability_ids:
					total_assets =  self.getValues("wealth_assets",rec_field,"assets_id")
					total_liability =  self.getValues("wealth_liability",rec_field,"liability_id")
					if total_assets != None and total_liability != None:
						net = total_assets - total_liability
						self.env.cr.execute("update closing_2_closing_2 set "+str(rec_field)+" =  "+str(net)+" WHERE closing_2_id = "+str(self.id)+"")

	def createOpeningReconcil(self):
		# if self.wealth_reconciliation_opening_ids:
		wealth_reconciliation_opening = self.wealth_reconciliation_opening_ids.search([('description', '=' ,"opening")])
		wealth_reconciliation_opening.unlink()
		if self.cash_closing_2_ids:
			self.wealth_reconciliation_opening_ids.create({
				'description' : "opening",
				'wealth_open_id' : self.id,
				'cash_closing_2_id' : self.cash_closing_2_ids[0].id,
				})
			record_fields = "y20"
			for x in xrange(10,25):
				update_field = record_fields+str(x+1)
				record_field = record_fields+str(x)
				self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = 'closing_2_closing_2' AND COLUMN_NAME = '"+record_field+"'")
				check_column = self.env.cr.fetchone()
				if check_column != None:
					self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = 'wealth_reconciliation_open' AND COLUMN_NAME = '"+update_field+"'")
					check_wro_column = self.env.cr.fetchone()
					if check_wro_column != None:
						self.env.cr.execute("UPDATE wealth_reconciliation_open b SET    "+update_field+" = a."+record_field+" FROM   closing_2_closing_2 a WHERE  b.cash_closing_2_id = a.id")



	def addPreNCRColAssets(self, start_value, end_value,  table_name , line_id):
					previous = 0
					record_fields = "y"
					for x in xrange(start_value,end_value):
						pre_field = record_fields+str(x)
						self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = '"+table_name+"' AND COLUMN_NAME = '"+pre_field+"'")
						pre_column = self.env.cr.fetchone()
						if pre_column != None:
							self.env.cr.execute("select SUM("+pre_field+")  FROM "+table_name+" WHERE receipts_id = "+str(line_id)+" ")
							pre_total = self.env.cr.fetchone()[0]
							if pre_total != None:
								previous = previous + pre_total
					return previous
################################################## Create Assets of NON CASH RECIEPTS from RECEIPTS#################################################
	def createNCRAssets(self):
		for line in self.cash_receipts_ids.search([('receipt_type','=','ncr'),('receipts_id.id','=',self.id)]):
			for ncr in line.non_cash_receipts:
				if not ncr.assets:
					if not self.wealth_assets_ids.search([('receipts_id','=',line.id)]):
						record = self.wealth_assets_ids.create({
							'description' : line.description,
							'assets_id' : self.id,
							'receipts_id': line.id
							})
						emp_list = 0
						ncr.assets = record.id
						for rec in line.non_cash_receipts.non_receipt_ids:
							year = int(rec.ncr_year.code)
							record_fields = "y"
							emp_list += rec.remaining_value
							for x in xrange(year,2025):
								record_field = record_fields + str(x)
								self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = 'wealth_assets' AND COLUMN_NAME = '"+record_field+"'")
								check_column = self.env.cr.fetchone() ####2016
								if check_column != None:
									for y in xrange(2010,x+1):
										record_new = 'y' + str(y)
										self.env.cr.execute("UPDATE wealth_assets SET    "+record_field+" = "+str(rec.remaining_value)+"  WHERE  receipts_id = "+str(line.id)+"")
									# if len(line.non_cash_receipts.non_receipt_ids) > 1:
									# 	break

			result = 0
			for rec in line.non_cash_receipts.non_receipt_ids:
				year = int(rec.ncr_year.code)
				record_fields = "y"
				result += rec.remaining_value
				for x in xrange(year,2025):
					record_field = record_fields + str(x)
					self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = 'wealth_assets' AND COLUMN_NAME = '"+record_field+"'")
					check_column = self.env.cr.fetchone() ####2016
					if check_column != None:
						self.env.cr.execute("UPDATE wealth_assets SET    "+record_field+" = "+str(result)+"  WHERE  receipts_id = "+str(line.id)+"")




################################################### Get value of Non Cash Receipt In Receipt Year ######################################

	# def getNCRRecieptValues(self):
	# 	if self.cash_receipts_ids:
	# 		for line in self.cash_receipts_ids:
	# 			if line.non_cash_receipts:
	# 				for rec in line.non_cash_receipts.non_receipt_ids: 
	# 					year = 'y'+str(rec.ncr_year.code)
	# 					if rec.ncr_year.code:
	# 						if 'y'+rec.ncr_year.code == line.browse(year).id:
	# 							self.env.cr.execute("update receipts set "+str(line.browse(year).id)+" =  "+str(rec.sale_value)+" WHERE id = "+str(line.id)+"")

######################################### Send Non Cash Receipt to INCOME in Wealth Reconciliation TAB #############################
	def sendNCRIncome(self):
		if self.cash_receipts_ids:
			for line in self.cash_receipts_ids:
				if line.non_cash_receipts:
					old_wealth_record = self.wealth_reconciliation_income_ids.search([('receipt_id','=',line.id)])
					if not old_wealth_record:
						record = self.wealth_reconciliation_income_ids.create({
							'description' : line.description,
							'wealth_income_id':self.id,
							'receipt_id' : line.id,
							})
					for rec in line.non_cash_receipts.non_receipt_ids:
						year = 'y'+str(rec.ncr_year.code)
						if rec.ncr_year.code:
							if not old_wealth_record:
								if 'y'+rec.ncr_year.code == line.browse(year).id:
									self.env.cr.execute("update wealth_reconciliation_income set "+str(line.browse(year).id)+" =  "+str(rec.ncr_addition)+" WHERE id = "+str(record.id)+"")
							else:
								if 'y'+rec.ncr_year.code == line.browse(year).id:
									self.env.cr.execute("update wealth_reconciliation_income set "+str(line.browse(year).id)+" =  "+str(rec.ncr_addition)+" WHERE id = "+str(old_wealth_record.id)+"")

######################################### Send Non Cash Receipt to Payemtns in Wealth Reconciliation TAB #############################
	def sendNCRPayments(self):
		if self.cash_receipts_ids:
			for line in self.cash_receipts_ids:
				if line.non_cash_receipts:
					old_wealth_record = self.cash_payments_ids.search([('receipts_id','=',line.id)])
					if not old_wealth_record and sum(item.ncr_cash for item in line.non_cash_receipts.non_receipt_ids ) != 0:
						record = self.cash_payments_ids.create({
							'description' : line.description,
							'payments_id':self.id,
							'receipts_id':line.id
							})
						for rec in line.non_cash_receipts.non_receipt_ids:
							year = 'y'+str(rec.ncr_year.code)
							if rec.ncr_year.code:
								if not old_wealth_record:
									if 'y'+rec.ncr_year.code == line.browse(year).id:
										self.env.cr.execute("update payments set "+str(line.browse(year).id)+" =  "+str(rec.ncr_cash)+" WHERE id = "+str(record.id)+"")
					else:
						for rec in line.non_cash_receipts.non_receipt_ids:
							year = 'y'+str(rec.ncr_year.code)
							if rec.ncr_year.code:
								if old_wealth_record:
									if 'y'+rec.ncr_year.code == line.browse(year).id:
										self.env.cr.execute("update payments set "+str(line.browse(year).id)+" =  "+str(rec.ncr_cash)+" WHERE id = "+str(old_wealth_record.id)+"")

######################################### Delete Capital Gain Whose Assest Is False #############################
	def delCapitalGain(self):
		capital_gain = self.env['capital_gain.capital_gain'].search([('assets','=',False)])
		capital_gain.unlink()
################################### Create Income Under NTR from Reciepts #########################################

	def createNtrFromReciepts(self):
		tax_profited = self.env['tax.computation'].search([('client_name.id','=',self.name.id)])
		if tax_profited:
			for taxcomp in tax_profited:
				if taxcomp.comparative_id.id == self.id:
					if self.cash_receipts_ids:
						for line in self.cash_receipts_ids:
							if line.tax_type == 'ntr':
								taxcomp.tax_computation_ntr_id.create({
									'description' : line.description,
									'receipt_type' : line.receipt_type,
									'receipts_id': line.id,
									'sub_tax_type' : 'nor',
									'income_under_ntr_id': taxcomp.id
									})
							elif line.tax_type == 'minimum':
								taxcomp.tax_computation_ntr_id.create({
									'description' : line.description,
									'receipt_type' : line.receipt_type,
									'receipts_id': line.id,
									'sub_tax_type' : 'min',
									'income_under_ntr_id' : taxcomp.id
									})
		else:
			raise Warning("You have No Record for this client In Tax Computation Or You havent saved that.")

	@api.multi
	def update(self):
		tax_profited = self.env['tax.computation'].search([('client_name.id','=',self.name.id)])
		if tax_profited:
			self.getReceiptsColumns()
			self.createReceiptIncome()
			self.createPaymentExpense()
			# self.createPaymentAssets()
			self.sendCashBankOpening()
			self.createLiabilityRecords()
			# self.createNCRAssets()
			# self.getNCRRecieptValues()
			self.sendNCRIncome()
			self.sendNCRPayments()
			self.sendCapitalGainIncome()
			# self.deductCapitalAmount()
			self.createCashBankAssets()
			# self.createPaymentOnCreateAssets()
			self.delCapitalGain()
			# self.createNtrFromReciepts()

		 	for line in tax_profited:
		 		if line.pnl_computation:
			 		for rec in line.pnl_computation:
		############################## Sending Capital profit_for_period To wealth_reconciliation_income in Comparitive Wealth ######################################
			 			if not self.wealth_reconciliation_income_ids.search([('description','=',"Profit "+rec.business_name.name.name),('business_name_id','=',rec.business_name.name.id)]):
							new_line = self.wealth_reconciliation_income_ids.create({
								'description' : "Profit "+rec.business_name.name.name,
								'receipt_type' : 'taxable',
								'wealth_income_id' : self.id,
								'business_name_id': rec.business_name.name.id,
								})
							if line.tax_year:
								year = 'y'+line.tax_year.name
								# if 'y'+line.tax_year.name == line.browse(year).id:
								self.env.cr.execute("update wealth_reconciliation_income set "+str(year)+" =  "+str(rec.business_name.profit_for_period)+" WHERE id = "+str(new_line.id)+"")
			 			
			 			for record in self.wealth_reconciliation_income_ids:
			 				if record.description == "Profit "+rec.business_name.name.name and record.business_name_id.id == rec.business_name.name.id:
								if line.tax_year:
									year = 'y'+line.tax_year.name
									# if 'y'+line.tax_year.name == line.browse(year).id:
									self.env.cr.execute("update wealth_reconciliation_income set "+str(year)+" =  "+str(rec.business_name.profit_for_period)+" WHERE id = "+str(record.id)+"") 			
		############################## Sending Capital Closing To wealth_assets in Comparitive Wealth ######################################
			 			if not self.wealth_assets_ids.search([('description','=',rec.business_name.name.name),('business_name_id','=',rec.business_name.name.id)]):
							wealth_assets_line = self.wealth_assets_ids.create({
								'description' : rec.business_name.name.name,
								'assets_id' : self.id,
								'business_name_id': rec.business_name.name.id,
								})
							if line.tax_year:
								year = 'y'+line.tax_year.name
								# if 'y'+line.tax_year.name == line.browse(year).id:
								self.env.cr.execute("update wealth_assets set "+str(year)+" =  "+str(rec.business_name.capital_closing)+" WHERE id = "+str(wealth_assets_line.id)+"")
			 			for assets in self.wealth_assets_ids:
			 				if assets.description == rec.business_name.name.name and assets.business_name_id.id == rec.business_name.name.id:
								if line.tax_year:
									year = 'y'+line.tax_year.name
									# if 'y'+line.tax_year.name == line.browse(year).id:
									self.env.cr.execute("update wealth_assets set "+str(year)+" =  "+str(rec.business_name.capital_closing)+" WHERE id = "+str(assets.id)+"")
		############################## Sending Capital Drawing To Receipts in Comparitive Wealth ######################################
			 			if not self.cash_receipts_ids.search([('description','=','Drawing '+rec.business_name.name.name),('business_name_id','=',rec.business_name.name.id)]):
							new_reciept = self.cash_receipts_ids.create({
								'description' : 'Drawing '+rec.business_name.name.name,
								'receipts_id' : self.id,
								'business_name_id': rec.business_name.name.id,
								})
							if line.tax_year:
								year = 'y'+line.tax_year.name
								# if 'y'+line.tax_year.name == line.browse(year).id:
								self.env.cr.execute("update receipts set "+str(year)+" =  "+str(rec.business_name.capital_drawing)+" WHERE id = "+str(new_reciept.id)+"")

			 			for drawing in self.cash_receipts_ids:
			 				if drawing.description == 'Drawing '+rec.business_name.name.name and drawing.business_name_id.id == rec.business_name.name.id:
								if line.tax_year:
									year = 'y'+line.tax_year.name
									# if 'y'+line.tax_year.name == line.browse(year).id:
									self.env.cr.execute("update receipts set "+str(year)+" =  "+str(rec.business_name.capital_drawing)+" WHERE id = "+str(drawing.id)+"")
		############################## Sending Capital Introduction To Payments in Comparitive Wealth ######################################
			 			if not self.cash_payments_ids.search([('description','=','Capital Introduction '+rec.business_name.name.name),('business_name_id','=',rec.business_name.name.id)]):
							new_payment = self.cash_payments_ids.create({
								'description' : 'Capital Introduction '+rec.business_name.name.name,
								'payments_id' : self.id,
								'business_name_id': rec.business_name.name.id,
								})
							if line.tax_year:
								year = 'y'+line.tax_year.name
								# if 'y'+line.tax_year.name == line.browse(year).id:
								self.env.cr.execute("update payments set "+str(year)+" =  "+str(rec.business_name.capital_intro)+" WHERE id = "+str(new_payment.id)+"") 			

			 			for payment in self.cash_payments_ids:
			 				if payment.description == 'Capital Introduction '+rec.business_name.name.name and payment.business_name_id.id == rec.business_name.name.id:
								if line.tax_year:
									year = 'y'+line.tax_year.name
									# if 'y'+line.tax_year.name == line.browse(year).id:
									self.env.cr.execute("update payments set "+str(year)+" =  "+str(rec.business_name.capital_intro)+" WHERE id = "+str(payment.id)+"")
				
			

			self.getCashDifference()
			self.createWealthStClosing()
			self.createOpeningReconcil()
			self.createReconcilClosing()
			self.getReconciliationDiff()
		else:
			raise Warning("You have No Record for this client In Tax Computation Or You havent saved that.")

	def createPaymentOnCreateAssets(self):
		msg="Record has been Modified for : "+str(self.name.name)+" "
		self.message_post(body=msg)

#########################################################################################################

	@api.multi
	def upload_assets(self):
		self.createPaymentAssets()

	@api.multi
	def button_open_wizard_method(self):
		return {
		'type': 'ir.actions.act_window',
		'name': 'wizarddd',
		'res_model': 'dedy.yuristiawan.wizard',
		'view_type': 'form',
		'view_mode': 'form',
		'target' : 'new',
		}