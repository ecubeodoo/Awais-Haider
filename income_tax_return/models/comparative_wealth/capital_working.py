# -*- coding: utf-8 -*-
#####################################################################
###########  Fields for WorkBook 'Capital Working' ##########
#####################################################################

from openerp import models, fields, api

class capital_working_sub(models.Model):
	_name               = 'capital_working_sub.capital_working_sub'
	business            = fields.Char(string = "Business", required=True)
	all_years           = fields.Boolean(string="All Years", default=False)
	name                = fields.Many2one('res.partner','Client Name', required=True)
	_rec_name 			= 'business'
	capital_working_id  = fields.One2many('capital_working_sub_sub.capital_working_sub_sub', 'capital_working_sub_id')
	capital_working_ids = fields.One2many('capital_working_sub_sub.capital_working_sub_sub', 'capital_working_sub_id')

class capital_working_sub_sub(models.Model):
	_name       = 'capital_working_sub_sub.capital_working_sub_sub'
	description = fields.Char(required=True)
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

	capital_working_sub_id = fields.Many2one('capital_working_sub.capital_working_sub',
        ondelete='cascade', string="Capital Working Sub", required=True)

class capital_working(models.Model):
	_name    = 'capital_working.capital_working'

	business = fields.Many2one('capital_working_sub.capital_working_sub', domain="[('name','=',parent.name)]", string = "Business", required=True)
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

	capital_working_id = fields.Many2one('comparative.wealth',
        ondelete='cascade', string="Capital Working", required=True)

	@api.onchange('business')
	def _onchange_business(self):
		if len(self.business) > 0:
			bb = self.business
			capital_total = self.env['capital_working_sub.capital_working_sub'].search([('business','=',bb.business),('id','=',self.business.id)])
			self.y2005 = sum(x.y2005 for x in capital_total.capital_working_ids)
			self.y2006 = sum(x.y2006 for x in capital_total.capital_working_ids)
			self.y2007 = sum(x.y2007 for x in capital_total.capital_working_ids)
			self.y2008 = sum(x.y2008 for x in capital_total.capital_working_ids)
			self.y2009 = sum(x.y2009 for x in capital_total.capital_working_ids)
			self.y2010 = sum(x.y2010 for x in capital_total.capital_working_ids)
			self.y2011 = sum(x.y2011 for x in capital_total.capital_working_ids)
			self.y2012 = sum(x.y2012 for x in capital_total.capital_working_ids)
			self.y2013 = sum(x.y2013 for x in capital_total.capital_working_ids)
			self.y2014 = sum(x.y2014 for x in capital_total.capital_working_ids)
			self.y2015 = sum(x.y2015 for x in capital_total.capital_working_ids)
			self.y2016 = sum(x.y2016 for x in capital_total.capital_working_ids)
			self.y2017 = sum(x.y2017 for x in capital_total.capital_working_ids)
			self.y2018 = sum(x.y2018 for x in capital_total.capital_working_ids)
			self.y2019 = sum(x.y2019 for x in capital_total.capital_working_ids)
			self.y2020 = sum(x.y2020 for x in capital_total.capital_working_ids)