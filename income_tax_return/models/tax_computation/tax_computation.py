#--------------------------------------------------------------------------------
#
#
#--------------------------------------------------------------------------------

from openerp import models, fields, api
from openerp.exceptions import Warning
class tax_computation(models.Model):
	_name = 'tax.computation'

	client_name             = fields.Many2one('res.partner','Client Name', required=True)
	tax_year                = fields.Many2one('account.fiscalyear', 'Tax Year', required=True)
	group                   = fields.Many2one('res.partner')
	tax_computation 		= fields.Many2one('tax.computation')
	_rec_name 			    = 'custom_seq'
	custom_seq      		= fields.Char(string="Name")
	comparative_id 			= fields.Many2one('comparative.wealth', string = 'Comparative Wealth')
	last_year_computation   = fields.Many2one('tax.computation')
	income_under_ntr        = fields.Float(string="Income under NTR")
	exempt_income           = fields.Float(string="Exempt Income ")
	deductible_allowance    = fields.Float(string="Deductible Allowance")
	taxable_income          = fields.Float(string="Taxable Income")
	tax_rate                = fields.Float(string="Rate of Tax")
	fixed_tax               = fields.Float(string="Fixed Tax")
	tax_liability           = fields.Float(string="Tax Liability")
	portion_of_minimum_tax  = fields.Float(string="Portion of Minimum Tax")
	payable_tax             = fields.Float(string="Total Tax Payable")
	tax_adjust              = fields.Float(string="Tax deducted Adjustable")
	tax_deduct_min          = fields.Float(string="Tax deducted Minimum")
	total_tax               = fields.Float(string="Total Tax")
	tax_credits             = fields.Float(string="Tax Credits")
	refund_adjust           = fields.Float(string="Refund Adjustment")
	tax_ratio               = fields.Float(string="Tax Payable/ (Refundable)")
	rebate                  = fields.Float()
	admitted_tax            = fields.Float(string="Admitted Tax")
	income_under_ftr        = fields.Float(string="Income under FTR")
	tax_deduct              = fields.Float(string="Tax deducted")
	tax_computation_ntr_id        = fields.One2many('income.under.ntr', 'income_under_ntr_id')
	tax_computation_sbi_id        = fields.One2many('separate.block.income', 'separate_block_income_id')
	tax_computation_deductible_id = fields.One2many('deductible.allowance', 'deductible_allowance_id')
	tax_credits_id                = fields.One2many('tax.credits', 'tax_credits_id')
	tax_rebate_id                 = fields.One2many('income.rebate', 'income_rebate_id')
	tax_computation_ftr_id        = fields.One2many('income.under.ftr', 'income_under_ftr_id')
	tax_deduct_link_id            = fields.One2many('tax.deduct', 'tax_deduct_id')
	tax_computation_exempt_id     = fields.One2many('income.under.exempt', 'income_under_exempt_id')
	pnl_computation           = fields.One2many('pnl.computation.workbook', 'tax_computation_id')
	

	tc_salary           = fields.Float(string="1 Salary")
	tc_business         = fields.Float(string="2 Business")
	tc_property         = fields.Float(string="3 Property")
	tc_other_sources    = fields.Float(string="4 Other Sources")
	tc_cgt           	= fields.Float(string="5 CGT")
	tc_for_remit        = fields.Float(string="6 Foreign Remittance")
	tc_arg_in           = fields.Float(string="7 Agricultural Income")
	tc_share_aop        = fields.Float(string="7.5 Share From AOP")
	tc_total_income     = fields.Float(string="8 Total Income")
	tc_less_exempt		= fields.Float(string="9 Less Exempt")
	tc_less_sbi			= fields.Float(string="9.5 Less SBI")
	tc_less_ftr			= fields.Float(string="10 Less FTR")
	tc_ftr_exempt_diff	= fields.Float(string="11 Total")
	tc_less_ded_allowed	= fields.Float(string="12 Less Deductable Allowance ")
	tc_fe_ded_diff		= fields.Float(string="13 Total")
	tc_less_cap_gain    = fields.Float(string="14 Less Capital Gain")
	tc_less_property    = fields.Float(string="15 Less Property")
	tc_ntr 				= fields.Float(string="16 NTR")
	tc_tax_liabilty		= fields.Float(string="17 Tax Liability Under NTR")
	tax_lib_diff		= fields.Float(string="17.5 Diff of Min Tax Chargable")
	tc_tax_already_ded	= fields.Float(string="18 Tax Already Deducted Under NTR")
	tc_tax_credits		= fields.Float(string="18.5 Tax Credits")
	tc_tax_pay_refund	= fields.Float(string="19 Net Tax Payable / (Refundable)")
	tc_income_charg_uftr= fields.Float(string="20 Income Chargable to Tax under FTR")
	tc_tax_charge_ftr	= fields.Float(string="21 Tax Chargable under FTR ")
	tc_tax_deduct_ftr	= fields.Float(string="22 Tax Deducted under FTR ")
	tc_pay_refund_uftr	= fields.Float(string="23 Tax Payable / (Refundable) U FTR")
	tc_income_from_prp	= fields.Float(string="24 Income From Property ")
	tc_taxable_ifd		= fields.Float(string="25 Deductions Allowed From Property Income")
	tc_taxable_ifp		= fields.Float(string="26 Taxable Income From Property")
	tc_tax_liability_ifd= fields.Float(string="27 Tax Liability From Property")
	tc_capital_gain	    = fields.Float(string="28 CG Immoveable Property")
	tc_exmt_cg			= fields.Float(string="29 Exempt Capital Gain ")
	tc_cgt_ded			= fields.Float(string="30 CGT Deductions Allowed Immoveable Property")
	tc_balnc_taxable	= fields.Float(string="31 Balance Taxable Immoveable Property")
	tc_tax_pay_cg		= fields.Float(string="32 Tax Payable on CG Immoveable Property")
	tc_tax_paid_cg		= fields.Float(string="33 Tax Paid on CG Immoveable Property")
	tc_ttl_ntr			= fields.Float(string="34 NTR")
	tc_ttl_ftr			= fields.Float(string="35 FTR")
	tc_ttl_sbi			= fields.Float(string="36 Separate Block Income")
	tc_total_tax_lib	= fields.Float(string="37 Total Tax Liability")
	tc_ttd_ntr			= fields.Float(string="38 NTR")
	tc_ttd_ntr_tc		= fields.Float(string="38.5 Tax Credits")
	tc_ttd_ftr			= fields.Float(string="39 FTR")
	tc_ttd_sbi			= fields.Float(string="40 Separate Block Income")
	tc_total_tax_ded	= fields.Float(string="41 Total Tax Deducted")
	tc_final_pay_refund	= fields.Float(string="42 Net Tax Payable / (Refundable)")
	tc_ifp_ded			= fields.Float(string="43 Tax Deducted")
	tc_ifp_pay_refund	= fields.Float(string="44 Tax Payable / (Refundable)")
	tc_cgt_pay_refund	= fields.Float(string="45 CGT Payable / (Refundable) Immoveable Property")

	tc_capital_gain_s	= fields.Float(string="46 CG Securities")
	tc_cgt_ded_s		= fields.Float(string="47 CGT Deductions Allowed Securities")
	tc_balnc_taxable_s	= fields.Float(string="48 Balance Taxable Securities")
	tc_tax_pay_cg_s		= fields.Float(string="49 Tax Payable on CG Securities" )
	tc_tax_paid_cg_s	= fields.Float(string="50 Tax Paid on CG Securities")
	tc_cgt_pay_refund_s	= fields.Float(string="51 CGT Payable / (Refundable) Securities")
	tc_bahbood			= fields.Float(string="52 Bahbood")
	tc_minimum			= fields.Float(string="53 Minimum")
	tc_turnover			= fields.Float(string="54 Turnover")


	cc_profit_los_min_tax	= fields.Float('Profit Loss Minimum Tax')
	cc_tax_deducted_min	= fields.Float('Tax Deducted Minimum')
	cc_lib_bahbood	= fields.Float('Bahbood')
	cc_actual_liabilty	= fields.Float('Actual Liability')
	cc_lib_amount	= fields.Float('Liability Amount')
	cc_avg_rate_tax	= fields.Float('Average Rate', digits=(12,6))

	aop_indv_type = fields.Selection([
		('aop', 'AOP'),
		('ind', 'Indiviual'),
		])

	# tc_sca 				= fields.Boolean(string="Senior Citizen Allowance")
	# tc_fta 				= fields.Boolean(string="Full time Teacher Allowance")
	# tc_ftc 				= fields.Boolean(string="Foreign Tax Credit")
	# tc_donations		= fields.Boolean(string="Donations")
	# tc_inv_shares		= fields.Boolean(string="Investment in Shares")
	# tc_inv_hi			= fields.Boolean(string="Investment on Health Insurance")
	# tc_capf				= fields.Boolean(string="Contribution to approved pension fund")
	# tc_rusta			= fields.Boolean(string="Registration under Sales Tax Act ")
	# tc_emp_gen			= fields.Boolean(string="Employment Generation")
	# tc_inv_plnmach		= fields.Boolean(string="Investment in Plant and Machinery")
	# tc_enlistment		= fields.Boolean(string="Enlistment")
	# tc_ind_eqtinv		= fields.Boolean(string="Industrial underetakings [Equity Investment]")
	# tc_ind_plnmach		= fields.Boolean(string="Industrial underetakings [Plant and Machinery]")

	tax_cr_tree_ids		= fields.Many2many('tax.credits.tree')
	losses_ids			= fields.One2many('losses.losses','losses_id')




	@api.model
	def create(self, vals):
		recs = self.env['tax.computation'].search([('client_name','=',vals['client_name']),('tax_year','=',vals['tax_year'])])
		if recs:
			raise Warning("Multiple years for same client cant be done..!")
		return super(tax_computation, self).create(vals)

	@api.onchange('tax_computation_ntr_id')
	def _onchange_ntr_id(self):
		self.income_under_ntr = sum(line.amount for line in self.tax_computation_ntr_id if line.tax_type!='exempt')

	@api.onchange('tax_computation_deductible_id')
	def _onchange_deductible_id(self):
		self.deductible_allowance = sum(line.ded_allowed for line in self.tax_computation_deductible_id)

	@api.onchange('tax_rebate_id')
	def _onchange_rebate_id(self):
		self.rebate = sum(line.tax for line in self.tax_rebate_id)

	@api.onchange('tax_credits_id')
	def _onchange_credits_id(self):
		self.tax_credits = sum(line.tax for line in self.tax_credits_id)

	@api.onchange('tax_computation_ftr_id')
	def _onchange_ftr_id(self):
		self.income_under_ftr = sum(line.amount for line in self.tax_computation_ftr_id)
		self.tax_deduct = sum(line.tax for line in self.tax_computation_ftr_id)

	@api.onchange('tax_deduct_link_id')
	def _onchange_tax_deduct(self):
		self.tax_adjust = sum(line.amount for line in self.tax_deduct_link_id if line.tax_type=='adjustable')
		self.tax_deduct_min = sum(line.amount for line in self.tax_deduct_link_id if line.tax_type=='minimum')

		@api.onchange('tc_salary','tc_business','tc_property','tc_other_sources','tc_cgt','tc_for_remit','tc_arg_in')
		def _onchange_sub_types(self):
			self.tc_total_income=self.tc_salary+self.tc_business+self.tc_property+self.tc_other_sources+self.tc_cgt+self.tc_for_remit+self.tc_arg_in
			
		@api.onchange('tc_total_income','tc_less_exempt','tc_less_ftr')
		def _onchange_tc_total_income(self):
			self.tc_ntr = self.tc_total_income - (self.tc_less_exempt + self.tc_less_ftr)


	@api.onchange('income_under_ntr','rebate','tax_rate','deductible_allowance','tax_credits','fixed_tax','portion_of_minimum_tax','tax_adjust','tax_deduct_min','refund_adjust')
	def onchange_assesment_form_field(self):
		self.taxable_income = self.income_under_ntr - self.deductible_allowance
		self.tax_liability  = (self.taxable_income * self.tax_rate) + self.fixed_tax
		self.total_tax      = self.payable_tax - self.tax_adjust
		self.total_tax      = self.total_tax - self.tax_deduct_min
		self.tax_ratio      = self.total_tax - self.refund_adjust - self.tax_credits
		self.admitted_tax   = self.tax_ratio - self.rebate
		if self.portion_of_minimum_tax < self.tax_deduct_min:
			self.payable_tax    = self.tax_liability - self.portion_of_minimum_tax + self.tax_deduct_min
		elif self.portion_of_minimum_tax > self.tax_deduct_min:
			self.payable_tax = self.tax_liability

	@api.multi
	def update_computation(self):
		# self.tax_computation_ntr_id.unlink()
		# self.tax_deduct_link_id.unlink()
		# required_class = self.env['comparative.wealth'].search([('name','=',self.client_name.id)])

		# self.income_under_ntr = sum(line.amount for line in self.tax_computation_ntr_id if line.tax_type != 'exempt')
		# self.exempt_income = sum(line.amount for line in self.tax_computation_ntr_id if line.tax_type == 'exempt')
		# self.tax_deduct = sum(line.amount for line in self.tax_deduct_link_id if line.tax_type == 'tax_ftr')
		# self.income_under_ftr = sum(line.amount for line in self.tax_computation_ftr_id)
		# self.tax_adjust = sum(line.amount for line in self.tax_deduct_link_id if line.tax_type == 'adjustable')
		# self.tax_deduct_min = sum(line.amount for line in self.tax_deduct_link_id if line.tax_type == 'minimum')
		# self.taxable_income = self.income_under_ntr - self.deductible_allowance
		# self.payable_tax = self.tax_liability + self.portion_of_minimum_tax
		self.createIncomeUNTR()
		self.createIncomeUFTR()
		self.createTaxDeducted()
		self.createIncomeUExempt()
		self.createDedAllowance()
		self.createSBI()
		self.createDedAllSalary()
		self.updateCGTAmount()
		self.calculateTaxSBI()
		self.getBusinessProfit()
		self.computeTaxCredit()
		self.getTaxCompDetails()
		self.get_tax_rate()


	def getTaxCompDetails(self):
		self.tc_salary =  sum(line.amount for line in self.tax_computation_ntr_id if line.receipt_type =='sal') + sum(line.amount for line in self.tax_computation_ftr_id if line.receipt_type =='sal') + sum(line.amount for line in self.tax_computation_exempt_id if line.sub_type =='sal')
		self.tc_business =  sum(line.amount for line in self.tax_computation_ntr_id if line.receipt_type =='bus') + sum(line.amount for line in self.tax_computation_ftr_id if line.receipt_type =='bus') + sum(line.amount for line in self.tax_computation_exempt_id if line.sub_type =='bus')
		self.tc_property =  sum(line.amount for line in self.tax_computation_ntr_id if line.receipt_type =='property') + sum(line.amount for line in self.tax_computation_ftr_id if line.receipt_type =='property') + sum(line.amount for line in self.tax_computation_exempt_id if line.sub_type =='property')
		# self.tc_less_property =  sum(line.amount for line in self.tax_computation_ntr_id if line.receipt_type =='property') + sum(line.amount for line in self.tax_computation_ftr_id if line.receipt_type =='property') + sum(line.amount for line in self.tax_computation_exempt_id if line.sub_type =='property')
		self.tc_less_property =  0
		self.tc_other_sources =  sum(line.amount for line in self.tax_computation_ntr_id if line.receipt_type =='oth_sour') + sum(line.amount for line in self.tax_computation_ftr_id if line.receipt_type =='oth_sour') + sum(line.amount for line in self.tax_computation_exempt_id if line.sub_type =='oth_sour')
		self.tc_cgt =  sum(line.amount for line in self.tax_computation_ntr_id if line.receipt_type =='cgt') + sum(line.amount for line in self.tax_computation_ftr_id if line.receipt_type =='cgt') + sum(line.amount for line in self.tax_computation_exempt_id if line.sub_type =='cgt') + sum(line.amount for line in self.tax_computation_sbi_id if line.receipt_type =='cgt')
		self.tc_for_remit =  sum(line.amount for line in self.tax_computation_ntr_id if line.receipt_type =='foreign_remit') + sum(line.amount for line in self.tax_computation_ftr_id if line.receipt_type =='foreign_remit') + sum(line.amount for line in self.tax_computation_exempt_id if line.sub_type =='foreign_remit')
		self.tc_arg_in =  sum(line.amount for line in self.tax_computation_ntr_id if line.receipt_type =='arg_in') + sum(line.amount for line in self.tax_computation_ftr_id if line.receipt_type =='arg_in') + sum(line.amount for line in self.tax_computation_exempt_id if line.sub_type =='arg_in')
		self.tc_share_aop =  sum(line.amount for line in self.tax_computation_ntr_id if line.receipt_type =='sh_aop')
		self.tc_total_income=self.tc_salary+self.tc_business+self.tc_property+self.tc_other_sources+self.tc_cgt+self.tc_for_remit+self.tc_arg_in+self.tc_share_aop
		self.tc_less_exempt =   sum(line.amount for line in self.tax_computation_exempt_id)
		self.tc_less_ftr =  sum(line.amount for line in self.tax_computation_ftr_id)
		# self.tc_tax_already_ded =  sum(line.amount for line in self.tax_deduct_link_id if line.tax_type =='adjustable' and line.sub_type in ['sal','bus','oth_sour']) change_commentd--
		self.tc_tax_already_ded =  sum(line.amount for line in self.tax_deduct_link_id if line.tax_type =='adjustable' or line.tax_type == 'minimum')
		self.tc_tax_credits = sum(line.tax for line in self.tax_credits_id)
		self.tc_tax_pay_refund = self.tc_tax_liabilty + self.tax_lib_diff- self.tc_tax_already_ded - self.tc_tax_credits - self.tc_bahbood
		self.tc_less_ded_allowed =  sum(line.ded_allowed for line in self.tax_computation_deductible_id if line.deductible_allowance_ids.name == 'NTR' or line.deductible_allowance_ids.name == 'Salary')
		self.tc_taxable_ifd =  sum(line.ded_allowed for line in self.tax_computation_deductible_id if line.deductible_allowance_ids.name == 'Property')
		self.tc_cgt_ded =  sum(line.ded_allowed for line in self.tax_computation_deductible_id if line.deductible_allowance_ids.name == 'CGT (IMV)')
		self.tc_cgt_ded_s = sum(line.ded_allowed for line in self.tax_computation_deductible_id if line.deductible_allowance_ids.name == 'CGT (SEC)')
		self.tc_less_sbi = sum(line.amount for line in self.tax_computation_sbi_id)
		self.tc_ftr_exempt_diff =  self.tc_total_income - self.tc_less_exempt - self.tc_less_sbi - self.tc_less_ftr
		self.tc_fe_ded_diff =  self.tc_ftr_exempt_diff - self.tc_less_ded_allowed
		self.tc_less_cap_gain = 0
		# self.tc_less_cap_gain = self.tc_cgt
		self.tc_ntr = self.tc_fe_ded_diff - self.tc_less_cap_gain - self.tc_less_property
		self.tc_income_charg_uftr = self.tc_less_ftr
		self.tc_tax_deduct_ftr =  sum(line.amount for line in self.tax_deduct_link_id if line.tax_type =='tax_ftr')
		self.tc_tax_charge_ftr =  sum(line.tax for line in self.tax_computation_ftr_id)
		self.tc_pay_refund_uftr =  self.tc_tax_charge_ftr - self.tc_tax_deduct_ftr
		self.tc_income_from_prp =  sum(line.amount for line in self.tax_computation_sbi_id if line.receipt_type =='property')
		self.tc_taxable_ifp =  self.tc_income_from_prp - self.tc_taxable_ifd
		self.tc_tax_paid_cg =  sum(line.amount for line in self.tax_deduct_link_id if line.tax_type =='sbi' )
		self.tc_ifp_ded =  sum(line.amount for line in self.tax_deduct_link_id if line.tax_type =='sbi' and line.sub_type == 'property')
		self.tc_ifp_pay_refund = self.tc_tax_liability_ifd - self.tc_ifp_ded
		self.tc_capital_gain = sum(line.amount for line in self.tax_computation_sbi_id if line.receipt_type =='cgt' and line.im_sec_type == 'imp' )
		self.tc_capital_gain_s = sum(line.amount for line in self.tax_computation_sbi_id if line.receipt_type =='cgt' and line.im_sec_type == 'sec' )
		self.tc_balnc_taxable = self.tc_capital_gain - self.tc_cgt_ded
		self.tc_cgt_pay_refund = self.tc_tax_pay_cg - self.tc_tax_paid_cg
		self.tc_ttl_ntr = self.tc_tax_liabilty
		self.tc_ttl_ftr = self.tc_tax_charge_ftr
		self.tc_tax_pay_cg_s = sum(line.tax for line in self.tax_computation_sbi_id if line.receipt_type =='cgt' and line.im_sec_type == 'sec')
		self.tc_ttl_sbi = self.tc_tax_liability_ifd + self.tc_tax_pay_cg + self.tc_tax_pay_cg_s
		self.tc_total_tax_lib = self.tc_ttl_ntr + self.tc_ttl_ftr + self.tc_ttl_sbi
		self.tc_ttd_ntr = self.tc_tax_already_ded
		self.tc_ttd_ftr = self.tc_tax_deduct_ftr
		self.tc_ttd_sbi = self.tc_tax_paid_cg + self.tc_ifp_ded + self.tc_tax_paid_cg_s
		self.tc_total_tax_ded = self.tc_ttd_ntr + self.tc_ttd_ftr + self.tc_ttd_sbi + self.tc_ttd_ntr_tc
		self.tc_final_pay_refund = self.tc_total_tax_lib - self.tc_total_tax_ded

		self.tc_balnc_taxable_s = self.tc_capital_gain_s - self.tc_cgt_ded_s
		self.tc_tax_paid_cg_s = sum(line.amount for line in self.tax_deduct_link_id if line.tax_type =='sbi_sec')
		self.tc_cgt_pay_refund_s = self.tc_tax_pay_cg_s - self.tc_tax_paid_cg_s
		self.tc_ttd_ntr_tc = self.tc_tax_credits
		self.cc_avg_rate_tax = (self.tc_tax_liabilty - sum(line.tax for line in self.tax_credits_id if line.check_min_tax == True))/self.tc_ntr


	@api.onchange('tc_tax_credits','tc_capital_gain_s','tc_cgt_ded_s','tc_total_tax_lib','tc_total_tax_ded',
		'tc_ttd_ntr','tc_ttd_ftr','tc_ttd_sbi','tc_ttd_ntr_tc','tc_tax_paid_cg','tc_ifp_ded','tc_tax_paid_cg_s',
		'tc_tax_liability_ifd','tc_tax_pay_cg','tc_tax_pay_cg_s','tc_tax_deduct_ftr','tc_tax_already_ded','tc_ttl_ntr',
		'tc_ttl_ftr','tc_ttl_sbi','tc_capital_gain','tc_cgt_ded','tc_tax_liabilty','tc_tax_charge_ftr','tc_income_from_prp',
		'tc_taxable_ifd','tc_total_income','tc_less_exempt','tc_less_sbi','tc_less_ftr','tc_ftr_exempt_diff','tc_less_ded_allowed',
		'tc_fe_ded_diff','tc_less_cap_gain','tc_less_property')
	def _onchange_manyfields(self):
		self.tc_ttd_ntr_tc = self.tc_tax_credits
		self.tc_cgt_pay_refund_s = self.tc_tax_pay_cg_s - self.tc_tax_paid_cg_s
		self.tc_balnc_taxable_s = self.tc_capital_gain_s - self.tc_cgt_ded_s
		self.tc_final_pay_refund = self.tc_total_tax_lib - self.tc_total_tax_ded
		self.tc_total_tax_ded = self.tc_ttd_ntr + self.tc_ttd_ftr + self.tc_ttd_sbi + self.tc_ttd_ntr_tc
		self.tc_ttd_sbi = self.tc_tax_paid_cg + self.tc_ifp_ded + self.tc_tax_paid_cg_s
		self.tc_ttl_sbi = self.tc_tax_liability_ifd + self.tc_tax_pay_cg + self.tc_tax_pay_cg_s
		self.tc_total_tax_lib = self.tc_ttl_ntr + self.tc_ttl_ftr + self.tc_ttl_sbi
		self.tc_ttd_ntr = self.tc_tax_already_ded
		self.tc_ttd_ftr = self.tc_tax_deduct_ftr
		self.tc_balnc_taxable = self.tc_capital_gain - self.tc_cgt_ded
		self.tc_cgt_pay_refund = self.tc_tax_pay_cg - self.tc_tax_paid_cg
		self.tc_ttl_ntr = self.tc_tax_liabilty
		self.tc_ttl_ftr = self.tc_tax_charge_ftr
		self.tc_taxable_ifp =  self.tc_income_from_prp - self.tc_taxable_ifd
		self.tc_ftr_exempt_diff =  self.tc_total_income - self.tc_less_exempt - self.tc_less_sbi - self.tc_less_ftr
		self.tc_fe_ded_diff =  self.tc_ftr_exempt_diff - self.tc_less_ded_allowed
		self.tc_ntr = self.tc_fe_ded_diff - self.tc_less_cap_gain - self.tc_less_property
		self.tc_income_charg_uftr = self.tc_less_ftr
		self.tc_pay_refund_uftr =  self.tc_tax_charge_ftr - self.tc_tax_deduct_ftr



	def computeTaxCredit(self):
		if self.tax_cr_tree_ids:
			for line in self.tax_cr_tree_ids:
				tc_record = self.tax_credits_id.search([('description','=',line.name)])
				if not tc_record:

					# if line.rate != 0:
					# 	tc_record.amount = self.tc_tax_liabilty * line.rate
				# else:
					self.tax_credits_id.create({
						'description' : line.name,
						# 'amount' : self.tc_tax_liabilty * line.rate,
						'tax_credits_id' : self.id,
						})
			# for x in self.tax_credits_ids:
			# 	if x.


	def getBusinessProfit(self):
		if self.pnl_computation:
			for line in self.pnl_computation:
				################### Records Creation For Income Under NTR #################
				if line.business_name.name.business_type == 'sp':
					ntr_id = self.tax_computation_ntr_id.search([('pnl_id','=',line.id)])
					self.createMinitaxUNTR(line.business_name.minimum_tax_ids, self.tax_computation_ntr_id, line.id, self.id)
					if not ntr_id:
						self.tax_computation_ntr_id.create({
							'description' : "Profit for "+line.business_name.name.name,
							'receipt_type' : "bus",
							'sub_tax_type' : 'nor',
							'tax_type' : 'ntr',
							'income_under_ntr_id': self.id,
							'amount' : line.business_name.tax_profit - sum(mintax.profit for mintax in line.business_name.minimum_tax_ids),
							'pnl_id' : line.id
							})
					else:
						ntr_id.description = "Profit for "+line.business_name.name.name
						ntr_id.amount = line.business_name.tax_profit - sum(mintax.profit for mintax in line.business_name.minimum_tax_ids)
					
					################### Records Creation For Income Under FTR #################
					ftr_id = self.tax_computation_ftr_id.search([('pnl_id','=',line.id)])
					if not ftr_id:
						self.tax_computation_ftr_id.create({
							'description' : "Profit for "+line.business_name.name.name,
							'receipt_type' : "bus",
							'income_under_ftr_id': self.id,
							'amount' : line.business_name.ftr_tax_profit,
							'pnl_id' : line.id
							})
					else:
						ftr_id.description = "Profit for "+line.business_name.name.name
						ftr_id.amount = line.business_name.ftr_tax_profit
				################### Records Creation For Exempt  Income #################
				elif line.business_name.name.business_type == 'aop':
					ntr_id = self.tax_computation_ntr_id.search([('pnl_id','=',line.id)])
					self.createMinitaxUNTR(line.business_name.minimum_tax_ids, self.tax_computation_ntr_id, line.id, self.id)
					if not ntr_id:
						self.tax_computation_ntr_id.create({
							'description' : "Profit for "+line.business_name.name.name,
							'receipt_type' : "sh_aop",
							'sub_tax_type' : 'nor',
							'tax_type' : 'ntr',
							'income_under_ntr_id': self.id,
							'amount' : line.business_name.tax_profit,
							'pnl_id' : line.id,
							})
					else:
						ntr_id.description = "Profit for "+line.business_name.name.name
						ntr_id.amount = line.business_name.tax_profit


					# exempt_id = self.tax_computation_exempt_id.search([('pnl_id','=',line.id)])
					# if not exempt_id:
					# 	self.tax_computation_exempt_id.create({
					# 		'description' : "Profit for "+line.business_name.name.name,
					# 		'sub_type' : "bus",
					# 		'income_under_exempt_id': self.id,
					# 		'amount' : line.business_name.tax_profit,
					# 		'pnl_id' : line.id
					# 		})
					# else:
					# 	exempt_id.description = "Profit for "+line.business_name.name.name
					# 	exempt_id.amount = line.business_name.tax_profit

	def createMinitaxUNTR(self, minTaxRecs, model_UNTR, pnl_id, tax_comp_id):
		for line in minTaxRecs:
			old_rec = model_UNTR.search([('pnl_id','=',pnl_id), ('mintax_id','=',line.id)])
			if not old_rec:
				model_UNTR.create({
							'description' : "Profit for "+line.description,
							'receipt_type' : "bus",
							'sub_tax_type' : 'min',
							'tax_type' : 'minimum',
							'income_under_ntr_id': tax_comp_id,
							'amount' : line.profit,
							'pnl_id' : pnl_id,
							'mintax_id': line.id,				
							'min_wh': line.tax,				
					})
			else:
				old_rec.description = "Profit for "+line.description
				old_rec.amount =  line.profit
				old_rec.min_wh =  line.tax



	def createIncomeUNTR(self):
		required_class = self.env['comparative.wealth'].search([('name','=',self.client_name.id)])

		self.tax_computation_ntr_id.unlink()
		year = 'y'+str(self.tax_year.code)
		for line in required_class.cash_receipts_ids:
			if line.tax_type == 'ntr':
				new_ntr_id = self.tax_computation_ntr_id.create({
					'description' : line.description,
					'receipt_type' : line.sub_type,
					'receipts_id': line.id,
					'sub_tax_type' : 'nor',
					'income_under_ntr_id': self.id
					})
				self.env.cr.execute("UPDATE income_under_ntr b SET    amount = a."+year+" FROM   receipts a WHERE  b.receipts_id = a.id and b.id = "+str(new_ntr_id.id)+"")
			elif line.tax_type == 'minimum':
				new_min_id = self.tax_computation_ntr_id.create({
					'description' : line.description,
					'receipt_type' : line.sub_type,
					'receipts_id': line.id,
					'sub_tax_type' : 'min',
					'income_under_ntr_id' : self.id,
					})
				self.env.cr.execute("UPDATE income_under_ntr b SET    amount = a."+year+" FROM   receipts a WHERE  b.receipts_id = a.id and b.id = "+str(new_min_id.id)+"")

	def createIncomeUFTR(self):
		required_class = self.env['comparative.wealth'].search([('name','=',self.client_name.id)])

		# self.tax_computation_ftr_id.unlink()
		year = 'y'+str(self.tax_year.code)
		for line in required_class.cash_receipts_ids:
			old_rec =  self.tax_computation_ftr_id.search([('receipts_id','=',line.id),('income_under_ftr_id','=',self.id)])
			if not old_rec:
				if line.tax_type == 'ftr':
					new_ftr_id = self.tax_computation_ftr_id.create({
						'description' : line.description,
						'receipts_id': line.id,
						'receipt_type' : line.sub_type,
						'income_under_ftr_id': self.id,
						})
					self.env.cr.execute("UPDATE income_under_ftr b SET    amount = a."+year+" FROM   receipts a WHERE  b.receipts_id = a.id and b.id = "+str(new_ftr_id.id)+"")



	def createSBI(self):
		required_class = self.env['comparative.wealth'].search([('name','=',self.client_name.id)])

		self.tax_computation_sbi_id.unlink()
		year = 'y'+str(self.tax_year.code)
		for line in required_class.cash_receipts_ids:
			if line.tax_type == 'sbi':
				new_sbi_id = self.tax_computation_sbi_id.create({
					'description' : line.description,
					'receipts_id': line.id,
					'receipt_type' : line.sub_type,
					'separate_block_income_id': self.id,
					})
				self.env.cr.execute("UPDATE separate_block_income b SET    amount = a."+year+" FROM   receipts a WHERE  b.receipts_id = a.id and b.id = "+str(new_sbi_id.id)+"")


	def createIncomeUExempt(self):
		required_class = self.env['comparative.wealth'].search([('name','=',self.client_name.id)])

		self.tax_computation_exempt_id.unlink()
		year = 'y'+str(self.tax_year.code)
		for line in required_class.cash_receipts_ids:
			if line.tax_type == 'exempt':
				new_exempt_id = self.tax_computation_exempt_id.create({
					'description' : line.description,
					'receipts_id': line.id,
					'sub_type': line.sub_type,
					'income_under_exempt_id': self.id,
					})
				self.env.cr.execute("UPDATE income_under_exempt b SET    amount = a."+year+" FROM   receipts a WHERE  b.receipts_id = a.id and b.id = "+str(new_exempt_id.id)+"")


	def createTaxDeducted(self):
		required_class = self.env['comparative.wealth'].search([('name','=',self.client_name.id)])

		self.tax_deduct_link_id.unlink()
		year = 'y'+str(self.tax_year.code)
		for line in required_class.cash_payments_ids:
			if line.tax_type:
				new_taxded_id = self.tax_deduct_link_id.create({
					'description' : line.description,
					'payments_id': line.id,
					'tax_deduct_id': self.id,
					'tax_type':line.tax_type,
					'sub_type':line.sub_type,
					})
				self.env.cr.execute("UPDATE tax_deduct b SET    amount = a."+year+" FROM   payments a WHERE  b.payments_id = a.id and b.id = "+str(new_taxded_id.id)+"")


	def createDedAllowance(self):
		if self.comparative_id:
			year = 'y'+str(self.tax_year.code)
			if self.comparative_id.cash_payments_ids:
				for line in self.comparative_id.cash_payments_ids:
					old_recs = self.tax_computation_deductible_id.search([('payment_id','=',line.id)])
					old_recs.unlink()
					if line.receipt_type == 'ded_all':
						print line
						self.tax_computation_deductible_id.create({
							'description' : line.description,
							'deductible_allowance_id': self.id,
							'deductible_allowance_ids': line.deductible_allowance_ids.id,
							'payment_id': line.id,
							})
						self.env.cr.execute("UPDATE deductible_allowance b SET    amount = a."+year+" , ded_allowed= a."+year+"  FROM   payments a WHERE  b.payment_id = a.id")
		else:
			raise Warning("Please select Comparative Wealth for :",self.client_name.name)

	def createDedAllSalary(self):
		if self.tax_computation_ntr_id:
			old_recs = self.tax_computation_deductible_id.search([('description','=',"Medical Allowance"),('deductible_allowance_id','=',self.id,)])
			deductible_allowance_ids = self.env['deductable.allowance'].search([('name','=','Salary')]).id
			for line in self.tax_computation_ntr_id:
				if line.receipt_type == 'sal':
					if not old_recs:
						self.tax_computation_deductible_id.create({
							'description' : "Medical Allowance",
							'deductible_allowance_id': self.id,
							'deductible_allowance_ids': deductible_allowance_ids,
							'income_under_ntr_id': line.id,
							})
	def updateCGTAmount(self):
		if self.comparative_id:

			##########Capital Gain Amount For Income Under NTR######################## 
			for ntr in self.tax_computation_ntr_id:
				if ntr.receipt_type == 'cgt':
					receipts_record = self.comparative_id.cash_receipts_ids.search([('id','=',ntr.receipts_id.id)])
					for rec in receipts_record.capital_gain.capital_gain_ids:
						if rec.year_sale.code == self.tax_year.code:
							ntr.amount = rec.capital_gain
							ntr.no_of_months = rec.no_of_months

			##########Capital Gain Amount For Income Under SBI######################## 
			for sbi in self.tax_computation_sbi_id:
				if sbi.receipt_type == 'cgt':
					receipts_record = self.comparative_id.cash_receipts_ids.search([('id','=',sbi.receipts_id.id)])
					for rec in receipts_record.capital_gain.capital_gain_ids:
						if rec.year_sale.code == self.tax_year.code:
							sbi.amount = rec.capital_gain
							sbi.no_of_months = rec.no_of_months
							sbi.details = rec.details
							sbi.im_sec_type = rec.im_sec_type

			##########Capital Gain Amount For Income Under FTR######################## 
			for ftr in self.tax_computation_ftr_id:
				if ftr.receipt_type == 'cgt':
					receipts_record = self.comparative_id.cash_receipts_ids.search([('id','=',ftr.receipts_id.id)])
					for rec in receipts_record.capital_gain.capital_gain_ids:
						if rec.year_sale.code == self.tax_year.code:
							ftr.amount = rec.capital_gain
							ftr.no_of_months = rec.no_of_months

		else:
			raise Warning("Please select Comparative Wealth for :",self.client_name.name)

	def calculateTaxSBI(self):
		# if self.tax_computation_sbi_id:
		for line in self.tax_computation_sbi_id:
			if line.receipt_type == 'cgt':
				if line.im_sec_type == 'sec':
					if line.details == 'aca':
						required_class = self.env['tax_rates_table.tax_rates_table'].search([('tax_year','=',self.tax_year.id)])
						for rate in required_class.securities_disposal_ids:
							if rate.period_from <= line.no_of_months <= rate.period_to:
								line.tax = line.amount * (rate.rate / 100)
					elif line.details == 'acb':
						line.tax = line.amount * 0.0
					elif line.details == 'pme':
						line.tax = line.amount * 0.05
					






	@api.multi
	def get_tax_rate(self):
		att_min_tax = 0
		diff_lib = 0
		lib_amount = 0
		lib_bahbood = 0
		profit_los_min_tax =  self.getSumMintax()
		self.cc_profit_los_min_tax =  profit_los_min_tax
		tax_deducted_min = self.getSumTaxDed()
		self.cc_tax_deducted_min =  tax_deducted_min
		tc_record = sum(line.tax for line in self.tax_credits_id if line.check_min_tax != False)
		business_income =  sum(line.amount for line in self.tax_computation_ntr_id if line.receipt_type!='arg_in' and line.receipt_type!='foreign_remit'and line.receipt_type!='sal')
		salary_income =  sum(line.amount for line in self.tax_computation_ntr_id if line.receipt_type =='sal')
		vi_lib_amount = sum(line.amount for line in self.tax_computation_ntr_id if line.tax_type == 'minimum')
		td_min_amount = sum(line.amount for line in self.tax_deduct_link_id if line.tax_type == 'minimum')
		if business_income > salary_income:
			required_class = self.env['tax_rates_table.tax_rates_table'].search([('tax_year','=',self.tax_year.id)])
			tax_rate_book = required_class.business_rates_table_ids
			for x in tax_rate_book:
				if self.tc_ntr:
					if x.amount_from <= self.tc_ntr <= x.amount_to:    # 850000
						fixed_tax = x.fixed_tax_amount                        #32000
						taxable_amount = self.tc_ntr - x.amount_from   #100000
						tax_amount = taxable_amount * x.rate_of_tax				   #15000
						tax_rate = (tax_amount / self.tc_ntr) / 100
						actual_liabilty = self.tc_ntr * tax_rate + fixed_tax
						avg_rate = self.tc_tax_liabilty/self.tc_ntr
						self.createTCShareAop(avg_rate)
						for line in self.tax_computation_ntr_id:
							if line.tax_type == 'minimum':
								att_min_tax = line.amount * self.cc_avg_rate_tax
								diff_lib =  line.min_wh - att_min_tax
								if diff_lib > 0:
									lib_amount += diff_lib
							if line.tax_type == 'bahbood':
								bahbood_tax = line.amount * self.cc_avg_rate_tax
								bahbood_10 = line.amount * 0.1
								bahbood_diff = bahbood_tax - bahbood_10
								if bahbood_diff > 0:
									lib_bahbood += bahbood_diff

						self.cc_lib_bahbood =  lib_bahbood
						self.cc_actual_liabilty =  actual_liabilty
						self.cc_lib_amount =  lib_amount
						self.tc_tax_liabilty =  actual_liabilty

						# calculated_amount = ((actual_liabilty - tc_record )/self.tc_ntr) * profit_los_min_tax
						# difflib = tax_deducted_min - calculated_amount
						if lib_amount > 0:
							self.tax_lib_diff = lib_amount
						# if calculated_amount > 	tax_deducted_min:
						# 	self.tc_tax_liabilty = actual_liabilty
						# else:
						# 	self.tc_tax_liabilty =  (tax_deducted_min - ((actual_liabilty - tc_record )/self.tc_ntr) * profit_los_min_tax) + actual_liabilty
						# self.tc_tax_liabilty =  (tax_deducted_min - ((actual_liabilty - tc_record )/self.tc_ntr) * profit_los_min_tax) + actual_liabilty
						# amount_to_be = (tax_deducted_min - ((actual_liabilty - tc_record )/self.tc_ntr) * profit_los_min_tax) + actual_liabilty
						a = actual_liabilty - tc_record
						b = a/self.tc_ntr
						c = b * profit_los_min_tax
						d = tax_deducted_min - c
						e = d + actual_liabilty

						print tax_deducted_min
						print actual_liabilty
						print tc_record
						print self.tc_ntr
						print profit_los_min_tax
						print actual_liabilty
						print "xxxxxxxxxxxxxxxxxxxx"
						print "xxxxxxxxxxxxxxxxxxxx"
						print a
						print b
						print c
						print d
						print e

		else:
			print "xxxxxxxxxxxxxxxxxxxx"
			print "xxxxxxxxxxxxxxxxxxxx"
			required_class = self.env['tax_rates_table.tax_rates_table'].search([('tax_year','=',self.tax_year.id)])
			tax_rate_book = required_class.salaried_rates_table_ids
			for x in tax_rate_book:
				if self.tc_ntr:
					if x.amount_from <= self.tc_ntr <= x.amount_to:  #85000
						fixed_tax = x.fixed_tax_amount                       #14500
						taxable_amount = self.tc_ntr - x.amount_from # 100000
						tax_amount = taxable_amount * x.rate_of_tax               #10000
						tax_rate = (tax_amount / self.tc_ntr) / 100
						actual_liabilty = self.tc_ntr * tax_rate + fixed_tax
						avg_rate = actual_liabilty/ self.tc_ntr
						self.createTCShareAop(avg_rate)
						for line in self.tax_computation_ntr_id:
							if line.tax_type == 'minimum':
								att_min_tax = line.amount * avg_rate
								diff_lib =  line.min_wh - att_min_tax
								if diff_lib > 0:
									lib_amount += diff_lib
							if line.tax_type == 'bahbood':
								bahbood_tax = line.amount * avg_rate
								bahbood_10 = line.amount * 0.1
								bahbood_diff = bahbood_tax - bahbood_10
								if bahbood_diff > 0:
									lib_bahbood += bahbood_diff
						
						self.cc_lib_bahbood =  lib_bahbood
						self.cc_actual_liabilty =  actual_liabilty
						self.cc_lib_amount =  lib_amount
						self.tc_tax_liabilty =  actual_liabilty

						# calculated_amount = ((actual_liabilty - tc_record )/self.tc_ntr) * profit_los_min_tax
						# difflib = tax_deducted_min - calculated_amount
						if lib_amount > 0:
							self.tax_lib_diff = lib_amount
						# if calculated_amount > 	tax_deducted_min:
						# 	self.tc_tax_liabilty = actual_liabilty
						# else:
						# 	self.tc_tax_liabilty =  (tax_deducted_min - ((actual_liabilty - tc_record )/self.tc_ntr) * profit_los_min_tax) + actual_liabilty
						# self.tc_tax_liabilty =  (tax_deducted_min - ((actual_liabilty - tc_record )/self.tc_ntr) * profit_los_min_tax) + actual_liabilty
						# amount_to_be = (tax_deducted_min - ((actual_liabilty - tc_record )/self.tc_ntr) * profit_los_min_tax) + actual_liabilty
						a = actual_liabilty - tc_record
						b = a/self.tc_ntr
						c = b * profit_los_min_tax
						d = tax_deducted_min - c
						e = d + actual_liabilty

						print tax_deducted_min
						print actual_liabilty
						print tc_record
						print self.tc_ntr
						print profit_los_min_tax
						print actual_liabilty
						print "xxxxxxxxxxxxxxxxxxxx"
						print "xxxxxxxxxxxxxxxxxxxx"
						print a
						print b
						print c
						print d
						print e

	def getSumMintax(self):
		profit = 0 
		if self.pnl_computation:
			for line in self.pnl_computation:
				if line.business_name.name.business_type == 'sp':
					for rec in line.business_name.minimum_tax_ids:
						profit += rec.profit
		return profit

	def getSumTaxDed(self):
		amount = 0 
		if self.tax_deduct_link_id:
			for line in self.tax_deduct_link_id:
				if line.tax_type == 'minimum':
					amount += line.amount
		return amount

	def createTCShareAop(self, avg_rate):
		if self.tc_share_aop:
			tc_record = self.tax_credits_id.search([('description','=','Share of AOP')])
			if tc_record:
				if tc_record.rate != 0:
					tc_record.amount = self.tc_share_aop
					tc_record.rate = avg_rate
					tc_record.tax = self.tc_share_aop * (avg_rate)
			else:
				self.tax_credits_id.create({
					'description' : 'Share of AOP',
					'amount' : self.tc_share_aop,
					'tax_credits_id' : self.id,
					'rate' : avg_rate,
					'tax' : self.tc_share_aop * (avg_rate),
					})

	@api.multi
	def virtual_tax_minimum(self):
		print "cc"


	@api.multi
	def update_losses(self):
		if self.tc_business < 0 or self.tc_property < 0 or self.tc_other_sources < 0 or self.tc_cgt < 0 or self.tc_for_remit < 0:
			self.losses_ids.unlink()
			self.losses_ids.create({
				'business_loss': self.tc_business if self.tc_business < 0 else False,
				'property_loss': self.tc_property if self.tc_property < 0 else False,
				'other_src_loss': self.tc_other_sources if self.tc_other_sources < 0 else False,
				'cg_loss': self.tc_cgt if self.tc_cgt < 0 else False,
				'fr_remit_loss': self.tc_for_remit if self.tc_for_remit < 0 else False,
				'losses_id':self.id
				})


	@api.onchange('client_name','tax_year')
	def _get_comparative(self):
		required_class = self.env['comparative.wealth'].search([('name.id','=',self.client_name.id)])
		self.comparative_id = required_class.id
		client_name_seq = str(self.client_name.name)
		tax_year_seq    = str(self.tax_year.code)
		self.custom_seq = client_name_seq + " / " + tax_year_seq


	@api.multi
	def update_tax_depriciation(self):
		if self.pnl_computation:
			for line in self.pnl_computation:
				for sheet in self.comparative_id.balance_sheet_workbook_ids:
					for asset in sheet.business.balance_sheet_id:
						if asset.selection_type == "noncurrent":
							if line.business_name.id == sheet.business.tax_comp_bus.id:
								balance_sheet_rec =  line.business_name.accounting_tax_ids.search([('bal_sheet_asset_id','=',asset.id)])
								# balance_sheet_rec.unlink()
								if not balance_sheet_rec:
									line.business_name.accounting_tax_ids.create({
											'desc' : asset.description,
											'bal_sheet_asset_id' : asset.id,
											'accounting_tax_id' : line.business_name.id
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
			for pl in self.pnl_computation:
				for td in pl.business_name.accounting_tax_ids:
					for bls in self.comparative_id.balance_sheet_workbook_ids:
						for ast in bls.business.balance_sheet_id:
							if td.desc == ast.description:
								self.env.cr.execute("UPDATE balance_sheet_sub_sub_balance_sheet_sub_sub b SET    "+str(year)+" = a.wdv_cf FROM   pnl_tax_depreciation a WHERE  b.id = a.bal_sheet_asset_id")


		# Getting Accounting Depriciation Records from previous year
		# Previous Year WDV(CF)(Closing) is = Current Year WDV(BF)(Opening)
		for line in self.pnl_computation:
			year = str(int(self.tax_year.name)-1)
			tax_comp_recs = self.env['tax.computation'].search([('client_name.id','=',self.client_name.id),('tax_year.name','=',year)])
			if tax_comp_recs:
				for tcr in tax_comp_recs.pnl_computation:
					for ad in tcr.business_name.accounting_depreciation_ids:
						act_dep_recs = line.business_name.accounting_depreciation_ids.search([('desc','=',ad.desc),('accounting_depreciation_id','=',line.business_name.id)])
						if not act_dep_recs:
							line.business_name.accounting_depreciation_ids.create({
															'desc' : ad.desc,
															'rate' : ad.rate,
															'wdv_bf' : ad.wdv_cf,
															'depreciation' : ad.wdv_cf * ad.rate,
															'wdv_cf' : ad.wdv_cf - (ad.wdv_cf * ad.rate),
															'accounting_depreciation_id' : line.business_name.id
															})
						else:
							act_dep_recs.wdv_bf = ad.wdv_cf
							act_dep_recs.depreciation = (act_dep_recs.wdv_bf + (act_dep_recs.addition_new * (act_dep_recs.month_use / 12)) - (act_dep_recs.deletion * (act_dep_recs.month_use / 12))) * act_dep_recs.rate
