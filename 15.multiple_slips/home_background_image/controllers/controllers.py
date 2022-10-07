# -*- coding: utf-8 -*-
import base64
from odoo.http import Controller, request, route
from werkzeug.utils import redirect

DEFAULT_IMAGE = '/home_background_image/static/src/img/background.png'

class DasboardBackgroundImage(Controller):

    @route(['/get_image'], type='http', auth='user', website=False)
    def dashboard(self, **post):
        company = request.env.user.company_id
        if company.dashboard_background_img:
            image = base64.b64decode(company.dashboard_background_img)
        else:
            return redirect(DEFAULT_IMAGE)

        return request.make_response(
            image, [('Content-Type', 'image')])
