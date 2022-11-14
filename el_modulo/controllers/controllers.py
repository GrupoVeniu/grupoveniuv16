# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json


class MyModule(http.Controller):
    @http.route('/api/attendance/hours/<user_id>/<day_week>', auth='public', methods=['GET'])
    def get_attendances_hours(self, user_id, day_week, **kw):
        try:
            calendar_id = http.request.env['hr.employee'].sudo()\
                .search([('user_id', '=', int(user_id))]).resource_calendar_id
            hours = http.request.env['resource.calendar.attendance'].sudo()\
                .search_read([('calendar_id', '=', int(calendar_id)), ('dayofweek', '=', day_week)], 
                ['hour_from', 'hour_to'])
        except Exception as e:
            return build_response ({'err': str(e)})

    def build_response(self, entity):
        response = json.dumps(entity, ensure_ascii=False).encode('utf8')
        return Response (response, content_type='aplication/json;charset=utf-8',status=200)

#     @http.route('/my_module/my_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_module.listing', {
#             'root': '/my_module/my_module',
#             'objects': http.request.env['my_module.my_module'].search([]),
#         })

#     @http.route('/my_module/my_module/objects/<model("my_module.my_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_module.object', {
#             'object': obj
#         })
