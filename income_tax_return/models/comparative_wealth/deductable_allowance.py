# -*- coding: utf-8 -*-
#####################################################################
###########  Fields for WorkBook 'Deductable Allowlance' ##########
#####################################################################

from openerp import models, fields, api

class deductable_allowance(models.Model):
	_name               = 'deductable.allowance'
	name                = fields.Char('Name')