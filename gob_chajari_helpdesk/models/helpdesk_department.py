from odoo import fields, models


class HelpdeskDepartment(models.Model):
    _name = "helpdesk.department"
    _description = "Dependencia"

    name = fields.Char(string="Nombre", required=True)
