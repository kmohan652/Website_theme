# -*- encoding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from odoo import http


class website(http.Controller):
    @http.route('/shop',auth='public', website=True)
    def shop(self, *args, **kw):
        print("in shop")
        return http.request.render('Website_theme.shop')