# -*- coding: utf-8 -*-
#####################################################
###########  'res_partner_extension'##########
#####################################################

from openerp import models, fields, api
from openerp.exceptions import ValidationError

# class res_partner_extension(models.Model):
# 	_inherit  = 'res.partner'

# 	@api.constrains('name')
# 	def _check_something(self):
# 	    for record in self:
# 	        if record.name == self.name :
# 	            raise ValidationError("The name %s is already in use" % record.name)