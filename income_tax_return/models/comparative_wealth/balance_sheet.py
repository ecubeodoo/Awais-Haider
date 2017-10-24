# -*- coding: utf-8 -*-
#####################################################################
###########  Fields for WorkBook balance_sheet Working' ##########
#####################################################################

from openerp import models, fields, api

class balance_sheet_years_prototype(models.Model):
	_name = 'balance.sheet.years.prototype'

	y2014 = fields.Float(string = "2014")
	y2015 = fields.Float(string = "2015")
	y2016 = fields.Float(string = "2016")
	y2017 = fields.Float(string = "2017")

class balance_sheet_sub(models.Model):
	_name               = 'balance_sheet_sub.balance_sheet_sub'
	_rec_name 			= 'tax_comp_bus'
	tax_comp_bus 		= fields.Many2one('pnl.computation', string = "Business Name")
	name_of_business 	= fields.Many2one('business.name', string = "Business Name")
	business            = fields.Char(string = "Business")
	all_years           = fields.Boolean(string="All Years", default=False)
	name                = fields.Many2one('res.partner','Client Name', required=True)
	balance_sheet_id  = fields.One2many('balance_sheet_sub_sub.balance_sheet_sub_sub', 'balance_sheet_sub_id')
	balance_sheet_ids = fields.One2many('balance_sheet_sub_sub.balance_sheet_sub_sub', 'balance_sheet_sub_id')
	balance_sheet_lib_id = fields.One2many('balance_sheet_sub_sub_lib.balance_sheet_sub_sub_lib', 'balance_sheet_sub_lib_id')
	balance_sheet_cap_id = fields.One2many('balance_sheet_sub_sub_cap.balance_sheet_sub_sub_cap', 'balance_sheet_sub_cap_id')

	total_2014 = fields.Float(string="Total_2014 : ")
	total_2015 = fields.Float(string="Total_2015 : ")
	total_2016 = fields.Float(string="Total_2016 : ")
	total_2017 = fields.Float(string="Total_2017 : ")

	@api.multi
	def write(self, vals):
		result = super(balance_sheet_sub, self).write(vals)
		self.getCashDifference()
		self.getCapitalLine()
		return result
	@api.multi
	def update(self):
		self.getCashDifference()
		self.getCapitalLine()

		
	def getCashDifference(self):
		if self.balance_sheet_id or self.balance_sheet_cap_id or self.balance_sheet_lib_id:
			cw_fields = "total_20"
			op_fields = "y20"
			for x in xrange(10,25):
				cw_req_field = cw_fields+str(x)
				op_req_field = op_fields + str(x)
				total_assets = self.getValues("balance_sheet_sub_sub_balance_sheet_sub_sub",op_req_field,"balance_sheet_sub_id")
				total_liability =  self.getValues("balance_sheet_sub_sub_lib_balance_sheet_sub_sub_lib",op_req_field,"balance_sheet_sub_lib_id")
				total_capital =  self.getValues("balance_sheet_sub_sub_cap_balance_sheet_sub_sub_cap",op_req_field,"balance_sheet_sub_cap_id")
				if total_assets != None and total_capital != None and total_liability != None:
					net = (total_assets - total_liability) - total_capital
					self.env.cr.execute("update balance_sheet_sub_balance_sheet_sub set "+str(cw_req_field)+" =  "+str(net)+" WHERE id = "+str(self.id)+"")

	def getCapitalLine(self):
		if self.tax_comp_bus.capital_closing:
			self.balance_sheet_cap_id.unlink()
			record = self.balance_sheet_cap_id.create({
				'description':'Capital Closing',
				'balance_sheet_sub_cap_id':self.id,
				})
			req_field = 'y' + str(self.tax_comp_bus.tax_year.code)
			self.updateValues('balance_sheet_sub_sub_cap_balance_sheet_sub_sub_cap',req_field,record.id, self.tax_comp_bus.capital_closing)

############################################### SELECT SQL Query For SUM of Records ##############################################################################
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
############################################### Update SQL Query For Single Record ##############################################################################
	def updateValues(self, table_name, column_name, parent_id, amount):
		self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = '"+table_name+"' AND COLUMN_NAME = '"+column_name+"'")
		check_column = self.env.cr.fetchone()
		if check_column != None:
			self.env.cr.execute("UPDATE "+str(table_name)+" SET "+str(column_name)+" = "+str(amount)+"  WHERE id = "+str(parent_id)+"")
			return True
	# @api.multi
	# def write(self, vals):
	# 	result = super(balance_sheet_sub, self).write(vals)
	# 	self.sendAssetsTaxDep()
	# 	return result
	# ################## Method for sending assets lines to tax depriciation#################
	# def sendAssetsTaxDep(self):
	# 	if self.tax_comp_bus:
	# 		for asset in self.balance_sheet_id:
	# 			if asset.selection_type == "noncurrent":
	# 				balance_sheet_rec =  self.tax_comp_bus.accounting_tax_ids.search([('bal_sheet_asset_id','=',asset.id)])
	# 				balance_sheet_rec.unlink()
	# 				self.tax_comp_bus.accounting_tax_ids.create({
	# 						'desc' : asset.description,
	# 						'bal_sheet_asset_id' : asset.id,
	# 						'accounting_tax_id' : self.tax_comp_bus.id
	# 						})

	@api.onchange('name_of_business')
	def onchange_name_of_business(self):
		if self.name_of_business:
			self.tax_comp_bus = self.name_of_business

class balance_sheet_sub_sub(models.Model):
	_name       = 'balance_sheet_sub_sub.balance_sheet_sub_sub'
	_inherit = 'balance.sheet.years.prototype'
	description = fields.Char(required=True)
	selection_type = fields.Selection([
            ('current', 'Current'),
            ('noncurrent', 'Non Current'),
            ])

	sequence = fields.Integer(string ='Sequence')
	_order   = 'sequence'

	balance_sheet_sub_id = fields.Many2one('balance_sheet_sub.balance_sheet_sub',
        ondelete='cascade', string="Balance Sheet Working Sub", required=True)

class balance_sheet_sub_sub_lib(models.Model):
	_name       = 'balance_sheet_sub_sub_lib.balance_sheet_sub_sub_lib'
	_inherit = 'balance.sheet.years.prototype'
	description = fields.Char(required=True)
	selection_type = fields.Selection([
            ('current', 'Current'),
            ('noncurrent', 'Non Current'),
            ])

	sequence = fields.Integer(string ='Sequence')
	_order   = 'sequence'

	balance_sheet_sub_lib_id = fields.Many2one('balance_sheet_sub.balance_sheet_sub',
        ondelete='cascade', string="Balance Sheet Working Sub", required=True)

class balance_sheet(models.Model):
	_name    = 'balance_sheet.balance_sheet'
	_inherit = 'balance.sheet.years.prototype'
	business = fields.Many2one('balance_sheet_sub.balance_sheet_sub', domain="[('name','=',parent.name)]", string = "Business", required=True)
	sequence = fields.Integer(string ='Sequence')
	_order   = 'sequence'

	balance_sheet_id = fields.Many2one('comparative.wealth',
        ondelete='cascade', string="Balance Sheet Working", required=True)

	@api.onchange('business')
	def _onchange_business(self):
		if len(self.business) > 0:
			bb = self.business
			balance_sheet = self.env['balance_sheet_sub.balance_sheet_sub'].search([('business','=',bb.business),('id','=',self.business.id)])
			self.y2014 = sum(x.y2014 for x in balance_sheet.balance_sheet_ids)
			self.y2015 = sum(x.y2015 for x in balance_sheet.balance_sheet_ids)
			self.y2016 = sum(x.y2016 for x in balance_sheet.balance_sheet_ids)
			self.y2017 = sum(x.y2017 for x in balance_sheet.balance_sheet_ids)

class balance_sheet_sub_sub_cap(models.Model):
	_name       = 'balance_sheet_sub_sub_cap.balance_sheet_sub_sub_cap'
	_inherit = 'balance.sheet.years.prototype'
	description = fields.Char(required=True)
	selection_type = fields.Selection([
            ('current', 'Current'),
            ('noncurrent', 'Non Current'),
            ])

	sequence = fields.Integer(string ='Sequence')
	_order   = 'sequence'

	balance_sheet_sub_cap_id = fields.Many2one('balance_sheet_sub.balance_sheet_sub',
        ondelete='cascade', string="Balance Sheet Working Sub", required=True)

	pnl_id = fields.Many2one('pnl.computation' , 'PNL ID')