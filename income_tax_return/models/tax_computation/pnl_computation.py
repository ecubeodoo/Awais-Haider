from openerp import models, fields, api
from openerp.exceptions import Warning
import time

class business_name(models.Model):
	_name = 'business.name'
	name  = fields.Char('Name')
	customer = fields.Many2one('res.partner', 'Customer')
	business_type = fields.Selection([
            ('aop', 'AOP'),
            ('sp', 'Sole Proprietor'),
            ], string="Business Type")

	@api.model
	def create(self, vals):
		recs = self.env['business.name'].search([('name','=',vals['name']),('customer','=',vals['customer'])])
		if recs:
			raise Warning("Multiple businesses for same client cant be created..!")
		return super(business_name, self).create(vals)

class pnl_computation(models.Model):
	_name = 'pnl.computation'



	name                    = fields.Many2one('business.name','Name')
	client_name 			= fields.Many2one('res.partner')
	tax_year 				= fields.Many2one('account.fiscalyear')
	comparative_wealth 		= fields.Many2one('comparative.wealth')
	pnl_computation 		= fields.Many2one('pnl.computation')

	total_sale              = fields.Float(string="Total Sales")
	sale_under_ntr          = fields.Float(string="NTR Sales")
	sale_under_ftr          = fields.Float(string="FTR/Exempt Sales")
	other_sale_under_ntr    = fields.Float(string="Other NTR Revenue")
	other_sale_under_ftr    = fields.Float(string="Other FTR/Exempt Revenue")
	ntr_income              = fields.Float(string="NTR Revenue")
	purchases               = fields.Float(string="Purchases")
	direct_expenses         = fields.Float(string="Direct Expenses")
	opening                 = fields.Float(string="Add: Opening")
	closing                 = fields.Float(string="Less: Closing")
	cost_of_sales			= fields.Float(string="Cost of Sales")
	ntr_cost_of_sales	    = fields.Float(string="Cost of Sales")
	gross_profit			= fields.Float(string="Gross Profit")
	ntr_expense             = fields.Float(string="NTR Expense")
	ntr_profit_Loss         = fields.Float(string="NTR Acc. Profit/Loss")
	accounting_depreciation = fields.Float(string="Acc Depreciation")
	inadmissible_expenses   = fields.Float(string="In admissible Expenses")
	tax_depreciation	    = fields.Float(string="Tax Depreciation")
	tax_profit              = fields.Float(string="Tax Profit (NTR)")
	tax_profit_min          = fields.Float(string="Tax Profit (Minimum)")
	income_under_ftr        = fields.Float(string="Income under FTR")
	tax_deduct              = fields.Float(string="Tax deducted")
	description             = fields.Text()
	amount                  = fields.Float()
	capital_opening			= fields.Float(string="Opening")
	profit_for_period       = fields.Float(string="Profit")
	capital_closing			= fields.Float(string="Closing")
	capital_drawing			= fields.Float(string="Drawing")
	capital_intro			= fields.Float(string="Capital Introduction")

	ftr_income              	= fields.Float(string="FTR Revenue")
	ftr_gross_profit			= fields.Float(string="Gross Profit")
	ftr_expense             	= fields.Float(string="FTR Expense")
	ftr_profit_Loss         	= fields.Float(string="FTR Acc. Profit/Loss")
	ftr_accounting_depreciation = fields.Float(string="Acc Depreciation")
	ftr_inadmissible_expenses   = fields.Float(string="In admissible Expenses")
	ftr_tax_depreciation	    = fields.Float(string="Tax Depreciation")
	ftr_tax_profit              = fields.Float(string="Tax Profit")
	ftr_cost_of_sales			= fields.Float(string="Cost of Sales")
	rateoftaxes					= fields.Float(string="Rate of Minimum Tax")
	ntr_min_sales				= fields.Float(string="Minimum Sales")


	profit_loss_link_id     	= fields.One2many('profit_loss.profit_loss', 'profit_loss_ids')
	accounting_depreciation_ids = fields.One2many('pnl.accounting.depreciation', 'accounting_depreciation_id')
	accounting_tax_ids    		= fields.One2many('pnl.tax.depreciation', 'accounting_tax_id')
	pnl_acc_dep_sum_ids     	= fields.One2many('pnl.accounting.depreciation.summary', 'pnl_acc_dep_sum_id')
	pnl_tax_dep_sum_ids    		= fields.One2many('pnl.tax.depreciation.summary', 'pnl_tax_dep_sum_id')
	minimum_tax_ids    			= fields.One2many('minimumtax.minimumtax', 'minimum_tax_id')
	final_tax_ids    			= fields.One2many('finaltax.finaltax', 'final_tax_id')


	@api.onchange('accounting_depreciation_ids')
	def onchange_append_summary(self):
		for x in self.accounting_depreciation_ids:
			ids = []
			for a in self.pnl_acc_dep_sum_ids:
				ids.append(a.selection_type.id)
			if x.selection_type.id not in ids and x.selection_type:
				self.pnl_acc_dep_sum_ids |= self.pnl_acc_dep_sum_ids.new({
					'rate':x.rate,
					'wdv_bf':sum(item.wdv_bf for item in self.accounting_depreciation_ids if item.selection_type.id==x.selection_type.id),
					'code': x.code,
					'pnl_acc_dep_sum_id': self.id,
					'selection_type' : x.selection_type.id,
					})
			for x in self.accounting_depreciation_ids:
				for y in self.pnl_acc_dep_sum_ids:
					if y.selection_type.id == x.selection_type.id:
						y.wdv_bf = sum(item.wdv_bf for item in self.accounting_depreciation_ids if item.selection_type.id==x.selection_type.id)

	@api.onchange('accounting_tax_ids')
	def onchange_append_tax_summary(self):
		for x in self.accounting_tax_ids:
			ids = []
			for a in self.pnl_tax_dep_sum_ids:
				ids.append(a.selection_type.id)
			if x.selection_type.id not in ids and x.selection_type:
				self.pnl_tax_dep_sum_ids |= self.pnl_tax_dep_sum_ids.new({
					'rate':x.rate,
					'wdv_bf':sum(item.wdv_bf for item in self.accounting_tax_ids if item.selection_type.id==x.selection_type.id),
					'code': x.code,
					'pnl_tax_dep_sum_id': self.id,
					'selection_type' : x.selection_type.id,
					})
			for x in self.accounting_tax_ids:
				for y in self.pnl_tax_dep_sum_ids:
					if y.selection_type.id == x.selection_type.id:
						y.wdv_bf = sum(item.wdv_bf for item in self.accounting_tax_ids if item.selection_type.id==x.selection_type.id)

	@api.multi
	def update(self):
		if self.total_sale != 0:
			ntr_ratio = self.sale_under_ntr / self.total_sale
			ftr_ratio = self.sale_under_ftr / self.total_sale

			for x in self.profit_loss_link_id:
				x.ntr =  x.total * ntr_ratio
				x.ftr_exempt =  x.total * ftr_ratio
			self.ntr_income =  self.sale_under_ntr + self.other_sale_under_ntr
			
			self.direct_expenses =  sum(line.total for line in self.profit_loss_link_id if line.types =='direct_expenses' and line.admissible == 'admissible')
			self.cost_of_sales =  self.purchases + self.direct_expenses +  self.opening - self.closing
			self.gross_profit = self.ntr_income - self.ntr_cost_of_sales
			# self.accounting_depreciation =  sum(line.ntr for line in self.profit_loss_link_id if line.admissible =='depreciation')
			self.ntr_cost_of_sales = self.cost_of_sales * (self.sale_under_ntr/self.total_sale)
			self.ntr_expense =  sum(line.ntr for line in self.profit_loss_link_id if line.types =='indirect_expenses' and line.admissible == 'admissible') 
			self.inadmissible_expenses =  sum(line.ntr for line in self.profit_loss_link_id if line.types !='income' and line.admissible == 'in_admissible')
			self.ntr_profit_Loss = self.gross_profit - self.ntr_expense
			self.tax_profit = self.ntr_profit_Loss + self.accounting_depreciation  + self.inadmissible_expenses - self.tax_depreciation
			self.tax_profit_min = (self.tax_profit / (self.sale_under_ntr + self.ntr_min_sales)) * self.ntr_min_sales



			self.ftr_income =  self.sale_under_ftr + self.other_sale_under_ftr
			self.ftr_cost_of_sales = self.cost_of_sales * (self.sale_under_ftr/self.total_sale) 
			self.ftr_expense =  sum(line.ftr_exempt for line in self.profit_loss_link_id if line.types =='indirect_expenses' and line.admissible == 'admissible')
			self.ftr_gross_profit = self.ftr_income - self.ftr_cost_of_sales
			self.ftr_profit_Loss = self.ftr_gross_profit - self.ftr_expense
			# self.ftr_accounting_depreciation =  sum(line.ftr_exempt for line in self.profit_loss_link_id if line.admissible =='depreciation')
			self.ftr_inadmissible_expenses =  sum(line.ftr_exempt for line in self.profit_loss_link_id if line.types !='income' and line.admissible == 'in_admissible')
			self.ftr_tax_profit = self.ftr_profit_Loss + self.ftr_accounting_depreciation  + self.ftr_inadmissible_expenses - self.ftr_tax_depreciation
			
			self.accounting_depreciation = (sum(line.depreciation for line in self.accounting_depreciation_ids)) * (self.sale_under_ntr / self.total_sale)
			self.tax_depreciation = (sum(line.depreciation for line in self.accounting_tax_ids)) * (self.sale_under_ntr / self.total_sale)
			self.ftr_tax_depreciation = (sum(line.depreciation for line in self.accounting_tax_ids)) * (self.sale_under_ftr / self.total_sale)
			self.ftr_accounting_depreciation = (sum(line.depreciation for line in self.accounting_depreciation_ids)) * (self.sale_under_ftr / self.total_sale)

			self.other_sale_under_ntr = sum(line.capital_gain for line in self.accounting_tax_ids)

		self.update_opening()
		self.update_tax_depriciation()
		self.update_capital_amount()
		self.getFinalTax()
		self.getMinTax()


	def getFinalTax(self):
		if self.final_tax_ids:
			for line in self.final_tax_ids:
				line.profit = (self.tax_profit / (self.sale_under_ntr + sum(rec.sales for rec in self.final_tax_ids))) * line.sales

	def getMinTax(self):
		if self.minimum_tax_ids:
			for line in self.minimum_tax_ids:
				# line.profit = (self.tax_profit / (self.sale_under_ntr + self.ntr_min_sales)) * line.sales
				line.profit = ((line.sales / self.ntr_income) * self.tax_profit) - line.adjustment

	@api.multi
	def update_opening(self):
		if self.name:
			tax_computation = self.env['pnl.computation.workbook'].search([('business_name','=',self.id)])
			tax_profited = self.env['tax.computation'].search([('client_name.id','=',self.name.customer.id)])
			for line in tax_profited:
				for record in tax_computation:
					if line.tax_year.name == str(int(record.tax_computation_id.tax_year.name) - 1):
						for item in line.pnl_computation:
							if item.business_name.name == self.name:
								self.capital_opening = item.business_name.capital_closing
		# if self.tax_profit or self.ftr_tax_profit:
		self.profit_for_period = self.tax_profit + self.ftr_tax_profit

		# if self.capital_opening or self.profit_for_period or self.capital_drawing:
		self.capital_closing = (self.capital_opening + self.profit_for_period + self.capital_intro) - self.capital_drawing

################################################### Send Capital Value To Compartive Wealth Blance Sheet ########################

	@api.multi
	def update_capital_amount(self):
		if self.comparative_wealth:
			for line in self.comparative_wealth.balance_sheet_workbook_ids:
				line.business.getCashDifference()
				if line.business.balance_sheet_cap_id:
					line.business.balance_sheet_cap_id.unlink()
				if not line.business.balance_sheet_cap_id:
					new_line = line.business.balance_sheet_cap_id.create({
						'description' : "Closing",
						'pnl_id' : self.id,
						'balance_sheet_sub_cap_id' : line.id
						})
					if self.tax_year:
						year = 'y'+self.tax_year.name
						if 'y'+self.tax_year.name == line.browse(year).id:
							self.env.cr.execute("update balance_sheet_sub_sub_cap_balance_sheet_sub_sub_cap set "+str(line.browse(year).id)+" =  "+str(self.capital_closing)+" WHERE id = "+str(new_line.id)+"")
		 			




	# def update_tax_depriciation(self):
	# 	if self.name:
	# 		tax_computation = self.env['pnl.computation.workbook'].search([('business_name','=',self.id)])
	# 		tax_profited = self.env['tax.computation'].search([('client_name.id','=',self.name.customer.id)])
	# 		for item in tax_profited:
	# 			for record in tax_computation:
	# 				if item.tax_year.name == str(int(record.tax_computation_id.tax_year.name) - 1):
	# 					for line in item.pnl_computation:
	# 						for sheet in item.comparative_id.balance_sheet_workbook_ids:
	# 							for asset in sheet.business.balance_sheet_id:
	# 								if asset.selection_type == "noncurrent":
	# 									if line.business_name.id == sheet.business.tax_comp_bus.id:
	# 										balance_sheet_rec =  line.business_name.accounting_tax_ids.search([('bal_sheet_asset_id','=',asset.id)])
	# 										balance_sheet_rec.unlink()
	# 										line.business_name.accounting_tax_ids.create({
	# 												'desc' : asset.description,
	# 												'bal_sheet_asset_id' : asset.id,
	# 												'accounting_tax_id' : line.business_name.id
	# 												})
	# 										year = 'y'+str(int(item.tax_year.name)-1)
	# 										self.env.cr.execute("UPDATE pnl_tax_depreciation b SET    depreciation = a."+str(year)+" FROM   balance_sheet_sub_sub_balance_sheet_sub_sub a WHERE  b.bal_sheet_asset_id = a.id")

	@api.multi
	def update_tax_depriciation(self):
		if self.client_name and self.tax_year:
			comparative_wealth = self.env['comparative.wealth'].search([('name','=',self.client_name.id)])
			# comparative_wealth.update()   #### Commented Due to Some Issue
			for sheet in self.comparative_wealth.balance_sheet_workbook_ids:
				for asset in sheet.business.balance_sheet_id:
					if asset.selection_type == "noncurrent":
						if self.name.id == sheet.business.tax_comp_bus.name.id:
							balance_sheet_rec =  self.accounting_tax_ids.search([('bal_sheet_asset_id','=',asset.id),('desc','=',asset.description),('accounting_tax_id','=', self.id)])
							print balance_sheet_rec
							# balance_sheet_rec.unlink()
							if not balance_sheet_rec:
								self.accounting_tax_ids.create({
										'desc' : asset.description,
										'bal_sheet_asset_id' : asset.id,
										'accounting_tax_id' : self.id
										})
								if self.tax_year:
									year = 'y'+str(int(self.tax_year.name)-1)
									self.env.cr.execute("UPDATE pnl_tax_depreciation b SET    wdv_bf = a."+str(year)+" FROM   balance_sheet_sub_sub_balance_sheet_sub_sub a WHERE  b.bal_sheet_asset_id = a.id")
							else:
								if self.tax_year:
									year = 'y'+str(int(self.tax_year.name)-1)
									self.env.cr.execute("UPDATE pnl_tax_depreciation b SET    wdv_bf = a."+str(year)+" FROM   balance_sheet_sub_sub_balance_sheet_sub_sub a WHERE  b.bal_sheet_asset_id = a.id")


			# Setting Current Year Value as wdv_cf (closing) of previous Year
			if self.tax_year:
				year = 'y'+str(self.tax_year.name)
				for td in self.accounting_tax_ids:
					for bls in comparative_wealth.balance_sheet_workbook_ids:
						for ast in bls.business.balance_sheet_id:
							if td.desc == ast.description:
								self.env.cr.execute("UPDATE balance_sheet_sub_sub_balance_sheet_sub_sub b SET    "+str(year)+" = a.wdv_cf FROM   pnl_tax_depreciation a WHERE  b.id = a.bal_sheet_asset_id")


		# Getting Accounting Depriciation Records from previous year
		# Previous Year WDV(CF)(Closing) is = Current Year WDV(BF)(Opening)
		year = str(int(self.tax_year.name)-1)
		tax_comp_recs = self.env['tax.computation'].search([('client_name.id','=',self.client_name.id),('tax_year.name','=',year)])
		if tax_comp_recs:
			for tcr in tax_comp_recs.pnl_computation:
				for ad in tcr.business_name.accounting_depreciation_ids:
					act_dep_recs = self.accounting_depreciation_ids.search([('desc','=',ad.desc),('accounting_depreciation_id','=',self.id)])
					if not act_dep_recs:
						self.accounting_depreciation_ids.create({
														'desc' : ad.desc,
														'rate' : ad.rate,
														'wdv_bf' : ad.wdv_cf,
														'depreciation' : ad.wdv_cf * (ad.rate / 100),
														'wdv_cf' : ad.wdv_cf - (ad.wdv_cf * (ad.rate / 100)),
														'accounting_depreciation_id' : self.id
														})
					else:
						act_dep_recs.wdv_bf = ad.wdv_cf
						act_dep_recs.depreciation = (act_dep_recs.wdv_bf + (act_dep_recs.addition_new * (act_dep_recs.month_use / 12)) - (act_dep_recs.deletion * (act_dep_recs.month_use / 12))) * (act_dep_recs.rate / 100)
												

	@api.onchange('tax_profit', 'ftr_tax_profit')
	def onchange_tax_ftr_profit(self):
		if self.tax_profit or self.ftr_tax_profit:
			self.profit_for_period = self.tax_profit + self.ftr_tax_profit

	@api.onchange('capital_opening','profit_for_period','capital_drawing', 'capital_intro')
	def onchange_opn_cl_dr(self):
		if self.capital_opening or self.profit_for_period or self.capital_drawing or self.capital_intro:
			self.capital_closing = (self.capital_opening + self.profit_for_period + self.capital_intro) - self.capital_drawing

class pnl_computation_workbook(models.Model):
	_name = 'pnl.computation.workbook'

	business_name = fields.Many2one('pnl.computation', string = "Business Name", )
	profit = fields.Float()
	tax_computation_id = fields.Many2one('tax.computation')


class pnl_computation_prototype(models.Model):
	_name = 'pnl.computation.prototype'
	code = fields.Float('Code')
	wdv_bf = fields.Float('WDV(BF)')
	deletion = fields.Float('Deletion')
	addition_in_pak = fields.Float('Addition (Used in Pakistan)')
	extent_use = fields.Float('Extent of Use')
	addition_new = fields.Float('Addition (New)')
	initial_allowance = fields.Float('Initial Allowance')
	depreciation = fields.Float('Depreciation')
	wdv_cf = fields.Float('WDV(CF)')
	desc = fields.Char()
	selection_type = fields.Many2one('pnl.computation.selection', 'Type')
	rate = fields.Float('Rate')
	month_use = fields.Float('Month')
	d_month_use = fields.Float('D Month')
	capital_gain = fields.Float( 'Capital Gain')
	capital_sale_value = fields.Float( 'Sale Value')

class pnl_computation_selection(models.Model):
	_name = 'pnl.computation.selection'
	name = fields.Char()
	rate = fields.Selection([
			('0.10', '10%'),
			('0.15', '15%'),
			('0.20', '20%'),
            ('0.30', '30%'),
            ('1', '100%'),
            ], string="Depreciation Rate")
	initial_allowance = fields.Selection([
            ('15', '15%'),
            ('25', '25%'),
            ], string="Initial Allowance")


class pnl_accounting_depreciation(models.Model):
	_name = 'pnl.accounting.depreciation'
	_inherit = 'pnl.computation.prototype'
	accounting_depreciation_id = fields.Many2one('pnl.computation', 'Pnl ID')


	@api.onchange('rate','addition_new','deletion', 'month_use','d_month_use','wdv_bf')
	def onchange_get_deprication_values(self):
		actual = (self.wdv_bf - self.deletion) * (self.rate / 100)
		deletion = (self.deletion) * (self.rate / 100) * (self.d_month_use / 12)
		addition = (self.addition_new) * (self.rate / 100) * (self.month_use / 12)
		self.depreciation = actual + deletion + addition
		self.wdv_cf = self.wdv_bf  - self.deletion + self.addition_new - self.depreciation



class pnl_tax_depreciation(models.Model):
	_name = 'pnl.tax.depreciation'
	_inherit = 'pnl.computation.prototype'
	accounting_tax_id = fields.Many2one('pnl.computation', 'Pnl ID')
	bal_sheet_asset_id = fields.Many2one('balance_sheet_sub_sub.balance_sheet_sub_sub', 'Asset ID')

	@api.onchange('selection_type','addition_new','deletion','wdv_bf')
	def onchange_get_deprication(self):
		if self.selection_type or self.addition_new or self.deletion or self.wdv_bf:
			if self.selection_type.initial_allowance == '15':
				self.initial_allowance = self.addition_new * 0.15
				self.depreciation = (self.wdv_bf + self.addition_new + self.addition_in_pak - self.deletion - self.initial_allowance) * (float(self.selection_type.rate))
			elif self.selection_type.initial_allowance == '25':
				self.initial_allowance = self.addition_new * 0.25
				self.depreciation = (self.wdv_bf + self.addition_new + self.addition_in_pak - self.deletion - self.initial_allowance) * (float(self.selection_type.rate))
			else:
				self.depreciation = (self.wdv_bf + self.addition_new + self.addition_in_pak - self.deletion) * (float(self.selection_type.rate))

			self.wdv_cf = self.wdv_bf + self.addition_new + self.addition_in_pak - self.deletion - self.initial_allowance - self.depreciation


	@api.onchange('capital_sale_value','deletion')
	def onchange_capital_sale_value(self):
		if self.capital_sale_value:
			self.capital_gain = self.capital_sale_value - self.deletion

class pnl_accounting_depreciation_summary(models.Model):
	_name = 'pnl.accounting.depreciation.summary'
	_inherit = 'pnl.computation.prototype'
	pnl_acc_dep_sum_id = fields.Many2one('pnl.computation', 'Pnl ID')
	accounting_depreciation_id = fields.Many2one('pnl.accounting.depreciation', 'Acc Dep ID')



class pnl_tax_depreciation_summary(models.Model):
	_name = 'pnl.tax.depreciation.summary'
	_inherit = 'pnl.computation.prototype'
	pnl_tax_dep_sum_id = fields.Many2one('pnl.computation', 'Pnl ID')