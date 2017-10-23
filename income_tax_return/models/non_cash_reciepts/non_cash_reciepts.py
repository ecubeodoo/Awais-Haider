# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# 
# 
# ---------------------------------------------------------------------
from openerp import models, fields, api

class non_cash_reciepts(models.Model):

	_name      = 'non.cash.receipts'
	_description = "Non Cash Receipts"
	_inherit   = ['mail.thread', 'ir.needaction_mixin']
	_rec_name = 'assets'

	name           = fields.Many2one('res.partner','Client Name', required=True)
	assets         = fields.Many2one('wealth.assets',domain="[('assets_id.name.id','=',name)]")
	non_receipt_ids = fields.One2many('non.cash.receipts.tree','non_receipts_id')

	receipts_ids = fields.Integer('receipts')



class non_cash_receipts_tree(models.Model):

	_name      = 'non.cash.receipts.tree'
	ncr_year     = fields.Many2one('account.fiscalyear',string="Year")
	ncr_addition = fields.Float(string="Addition")
	ncr_cash  = fields.Float(string="Cash")
	# net_amount = fields.Float(string="Net", compute="_compute_total")
	description    = fields.Char()
	year_purchase  = fields.Many2one('account.fiscalyear')
	sale_value     = fields.Float()
	purchase_value = fields.Float()
	capital_gain   = fields.Float()
	sold_value   = fields.Float()
	remaining_value   = fields.Float()
	# receipts_ids = fields.Many2many('receipts')
	non_receipts_id = fields.Many2one('non.cash.receipts', 'NCR ID')


	@api.depends('ncr_addition', 'ncr_deletion')
	def _compute_total(self):
		for line in self:
			line.net_amount = line.ncr_addition - line.ncr_deletion


	@api.onchange('sale_value','purchase_value','sold_value','ncr_addition','ncr_cash')
	def _onchange_get_ncr_cg(self):
		self.capital_gain = self.sale_value - self.sold_value
		self.remaining_value = self.purchase_value - self.sold_value + self.ncr_addition + self.ncr_cash


	@api.onchange('ncr_year')
	def _onchange_get_ncr_year(self):
		if self.ncr_year and self.non_receipts_id:
			receipt_id = self.non_receipts_id.receipts_ids
			year = "y"+str(int(self.ncr_year.code)-1)
			self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = 'wealth_assets' AND COLUMN_NAME = '"+year+"'")
			check_column = self.env.cr.fetchone()
			if check_column != None:
				if self.env['wealth.assets'].search([('receipts_id','=',receipt_id)]):
					self.env.cr.execute("select "+year+"  FROM wealth_assets WHERE receipts_id = "+str(receipt_id)+"")
					asset_value = self.env.cr.fetchone()[0]
					if asset_value:
						self.purchase_value = asset_value
					else:
						self.purchase_value = 0






























	# def _onchange_get_ncr_year(self):
	# 	if self.ncr_year:
	# 		assets_recd = self.non_receipts_id.assets.browse("y"+str(int(self.ncr_year.code)-1)).id
	# 		self.env.cr.execute("select "+assets_recd+"  FROM wealth_assets WHERE id = "+str(self.non_receipts_id.assets.id)+" ")
	# 		asset_value = self.env.cr.fetchone()[0]
	# 		if asset_value != None:
	# 			self.purchase_value = asset_value
	# 		else:
	# 			self.purchase_value = 0