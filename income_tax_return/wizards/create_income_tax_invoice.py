from openerp import models, fields, api
from openerp.exceptions import Warning
class Wizard(models.TransientModel):
    _name = 'income_tax_retrun.invoice_creation'
    @api.multi
    def incometax_multi_invoice(self):
        result = self.env['income.tax.returns'].browse(self._context.get('active_ids'))
        for line in result:
            if line.invoice_id == "":
                invoice_recs            = self.env['account.invoice']
                account_id              = self.env['account.account'].search([('code','=',110200)])
                account_id_invoice_line = self.env['account.account'].search([('code','=',200000)])
                invoice_line_data       = [
                                            (0, 0,
                                                {
                                                    'quantity': 1,
                                                    'name': line.description or 'No Description',
                                                    'account_id': account_id_invoice_line.id,
                                                    'price_unit': line.unit_price,
                                                }
                                            )
                                        ]
                res = {
                        'partner_id' : line.client_name.id,
                        'account_id' : account_id.id,
                        'invoice_line' : invoice_line_data,
                }
                invoice_recs.create(res)
                line.invoice_id  =  invoice_recs.search([])[0]
            else:
                raise Warning("The Invoice of this record already exist...!")
