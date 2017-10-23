# -*- coding: utf-8 -*-
################################################################
###########  Fields for WorkBook "Wealth Statement"##########
################################################################

from openerp import models, fields, api

class wealth_liability(models.Model):
	_name = 'wealth.liability'
	description = fields.Char(string = "Description", required=True)
	types = fields.Many2one('asset.types' , string ="Type")
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

	liability_id = fields.Many2one('comparative.wealth',
        ondelete='cascade', string="Wealth Statement", required=True)
	receipt_id = fields.Many2one('receipts',
        ondelete='cascade', string="receipts")