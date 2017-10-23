#-*- coding:utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 OpenERP SA (<http://openerp.com>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api
import time
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT
from openerp.exceptions import Warning


class SampleDevelopmentReport(models.AbstractModel):
    _name = 'report.comparative_wealth_report.module_report'

    @api.model
    def render_html(self,docids, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('comparative_wealth_report.module_report')
        # records = self.env['comparative.wealth'].browse(docids)
        active_wizard = self.env['comparative.wealth.wizard'].search([])

        record_wizard = self.env['comparative.wealth.wizard'].search([('id','=',active_wizard[-1].id)])
        record_wizard_del = self.env['comparative.wealth.wizard'].search([('id','!=',active_wizard[-1].id)])
        record_wizard_del.unlink()

        records = self.env['comparative.wealth'].search([('name','=',record_wizard.client_name.id)])
        year = []
        for x in xrange(int(record_wizard.select_year_from.code), (int(record_wizard.select_year_to.code)+1)):
            year.append(x)

###################Get year values and show in report line wise of selected years ##############################################
        def get_year_value(getYear, line_id, table_name):
            req_year = 'y'+str(getYear)
            self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = '"+table_name+"' AND COLUMN_NAME = '"+req_year+"'")
            check_column = self.env.cr.fetchone() ####2016
            if check_column != None:
                self.env.cr.execute("select ("+req_year+")  FROM "+table_name+" WHERE id = "+str(line_id)+" ")
                amount = self.env.cr.fetchone()[0]
                if amount != None:
                    return amount
                if amount == None:
                    return 0

################### Get SUM of year values and show in report #################
        def get_total_value(getYear, line_id, table_name, table_id):
            req_year = 'y'+str(getYear)
            self.env.cr.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_NAME = '"+table_name+"' AND COLUMN_NAME = '"+req_year+"'")
            check_column = self.env.cr.fetchone() ####2016
            if check_column != None:
                self.env.cr.execute("select sum("+req_year+")  FROM "+table_name+" WHERE "+table_id+" = "+str(line_id)+" ")
                amount = self.env.cr.fetchone()[0]
                if amount != None:
                    return  amount
                if amount == None:
                    return 0

        
        docargs = {
            'doc_ids': docids,
            'doc_model': 'comparative.wealth',
            'docs': records,
            'data': data,
            'year': year,
            'get_year_value': get_year_value,
            'get_total_value': get_total_value
            }

        return report_obj.render('comparative_wealth_report.module_report', docargs)



class wizard(models.Model):
    _name = 'comparative.wealth.wizard'

    select_year_from = fields.Many2one('account.fiscalyear', 'Year From')
    select_year_to = fields.Many2one('account.fiscalyear', 'Year To')
    client_name = fields.Many2one('res.partner', 'Client Name')

    @api.multi
    def something(self):
        docids = self.env['comparative.wealth'].search([])
        for line in docids:
            myreport = self.env['report.comparative_wealth_report.module_report']
            myreport.render_html(line.id, data=None)

