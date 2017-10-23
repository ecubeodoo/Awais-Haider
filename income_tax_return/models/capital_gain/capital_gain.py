# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# 
# 
# ---------------------------------------------------------------------
from openerp import models, fields, api

class capital_gain(models.Model):

	_name      = 'capital_gain.capital_gain'
	_description = "Capital Gain"
	_inherit   = ['mail.thread', 'ir.needaction_mixin']

	_rec_name = 'assets'



	name           = fields.Many2one('res.partner','Client Name', required=True)
	description    = fields.Char()
	year_purchase  = fields.Many2one('account.fiscalyear')
	year_sale      = fields.Many2one('account.fiscalyear')
	assets         = fields.Many2one('wealth.assets',domain="[('assets_id.name.id','=',name)]")
	sale_value     = fields.Float()
	purchase_value = fields.Float()
	capital_gain   = fields.Float()
	sold_value   = fields.Float()
	remaining_value   = fields.Float()
	comparative_wealth = fields.Many2one('comparative.wealth')

	capital_gain_ids = fields.One2many('capital.gain.tree','capital_gain_id')

	@api.onchange('sale_value','purchase_value','sold_value')
	def _onchange_get_capital_gain(self):
		self.capital_gain = self.sale_value - self.sold_value
		self.remaining_value = self.purchase_value - self.sold_value


	@api.onchange('year_sale','assets')
	def _onchange_get_year_sale(self):
		if self.year_sale and self.assets:
			assets_recd = self.assets.browse("y"+str(int(self.year_sale.name))).id
			self.env.cr.execute("select "+assets_recd+"  FROM wealth_assets WHERE id = "+str(self.assets.id)+" ")
			asset_value = self.env.cr.fetchone()[0]
			if asset_value != None:
				self.purchase_value = asset_value
			else:
				self.purchase_value = 0



class capital_gain_tree(models.Model):

	_name      = 'capital.gain.tree'
	description    = fields.Char()
	year_purchase  = fields.Many2one('account.fiscalyear')
	year_sale      = fields.Many2one('account.fiscalyear')
	sale_value     = fields.Float()
	purchase_value = fields.Float()
	capital_gain   = fields.Float()
	sold_value   = fields.Float()
	remaining_value   = fields.Float()
	no_of_months   = fields.Integer()
	details = fields.Selection([
		('aca', 'Accquired After 1.7.2012'),
		('acb', 'Accquired Before 1.7.2012'),
        ('pme', 'Pakistan Mercantile Exchange'),
        ], string="Details")
	im_sec_type = fields.Selection([
		('imp', 'Immoveable Property'),
		('sec', 'Securites'),
        ], string="Type")
	capital_gain_id = fields.Many2one('capital_gain.capital_gain', 'Capital ID')



	@api.onchange('sale_value','purchase_value','sold_value')
	def _onchange_get_capital_gain(self):
		self.capital_gain = self.sale_value - self.sold_value
		self.remaining_value = self.purchase_value - self.sold_value


	@api.onchange('year_sale')
	def _onchange_get_year_sale(self):
		if self.year_sale and self.capital_gain_id.assets:
			assets_recd = self.capital_gain_id.assets.browse("y"+str(int(self.year_sale.name))).id
			self.env.cr.execute("select "+assets_recd+"  FROM wealth_assets WHERE id = "+str(self.capital_gain_id.assets.id)+" ")
			asset_value = self.env.cr.fetchone()[0]
			if asset_value != None:
				self.purchase_value = asset_value
			else:
				self.purchase_value = 0