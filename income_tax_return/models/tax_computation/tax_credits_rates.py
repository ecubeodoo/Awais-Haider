from openerp import models, fields, api

class tax_credits_tree(models.Model):
	_name = 'tax.credits.tree'
	_inherit   		= ['mail.thread', 'ir.needaction_mixin']
	

	name = fields.Char()
	rate      = fields.Float()
	description      = fields.Char()

	tax_credits_id = fields.Many2one('tax.computation','TCComputation ID')

		