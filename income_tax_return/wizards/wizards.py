# -*- coding: utf-8 -*-
#############################################
###############  #######################
############################################

from openerp import models, fields, api, _

class DedyYuristiawan(models.TransientModel):
    _name = "dedy.yuristiawan.wizard"

    # client_name  = fields.Many2one('res.partner','Client Name', required=True)

    year_shifting    = fields.Selection([
            # ('y2005', '2005'),
            # ('y2006', '2006'),
            # ('y2007', '2007'),
            # ('y2008', '2008'),
            # ('y2009', '2009'),
            # ('y2010', '2010'),
            # ('y2011', '2011'),
            # ('y2012', '2012'),
            # ('y2013', '2013'),
            ('y2014', '2014'),
            ('y2015', '2015'),
            # ('y2016', '2016'),
            # ('y2017', '2017'),
            # ('y2018', '2018'),
            # ('y2019', '2019'),
            # ('y2020', '2020')
            ], default='y2015')

    year_receiving    = fields.Selection([
            # ('y2005', '2005'),
            # ('y2006', '2006'),
            # ('y2007', '2007'),
            # ('y2008', '2008'),
            # ('y2009', '2009'),
            # ('y2010', '2010'),
            # ('y2011', '2011'),
            # ('y2012', '2012'),
            # ('y2013', '2013'),
            # ('y2014', '2014'),
            ('y2015', '2015'),
            ('y2016', '2016'),
            # ('y2017', '2017'),
            # ('y2018', '2018'),
            # ('y2019', '2019'),
            # ('y2020', '2020')
            ], default='y2016')
    
    @api.multi
    def create_request(self):
        
        active_class =self.env['comparative.wealth'].browse(self._context.get('active_id'))
        sending_year = self.year_shifting
        receiving_year = self.year_receiving
        a_n_l_recs  = self.env.cr.execute('SELECT id,'+sending_year+' FROM wealth_assets WHERE assets_id ='+str(active_class.id))

        a_n_l_recs_info = self.env.cr.fetchall()
        for p in a_n_l_recs_info:
            self.env.cr.execute("update wealth_assets set "+receiving_year+"='"+str(p[1])+"' WHERE id = "+str(p[0]))