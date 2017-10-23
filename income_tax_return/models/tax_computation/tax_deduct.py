# -*- coding: utf-8 -*-
###############################################################
########### Fields for WorkBook "Tax Deduct" ##########
###############################################################


from openerp import models, fields, api

class tax_deduct(models.Model):
	_name = 'tax.deduct'

	description = fields.Char()
	amount      = fields.Float()
	tax_type    = fields.Selection([
        ('adjustable', 'Adjustable'),
        ('minimum', 'Minimum'),
		('tax_ftr', 'FTR'),
        ('sbi','SBI (IMM)'),
        ('sbi_sec','SBI (SEC)'),
		('deductible_allowance', ''),

        ])

	sub_type = fields.Selection([
            ('sal', 'Salary'),
            ('bus', 'Business'),
            ('property', 'Property'),
            ('oth_sour', 'Other Sources'),
            ('cgtim', 'CGT  (IMV)'),
            ('cgtsec', 'CGT  (Sec)'),
            ('cgt', ' CGT'),
            ])

	tax_deduct_id = fields.Many2one('tax.computation',
        ondelete='cascade')

	payments_id = fields.Many2one('payments',
        ondelete='cascade', string="Payments")