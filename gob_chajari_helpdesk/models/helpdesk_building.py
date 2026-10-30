from odoo import fields, models


class HelpdeskBuilding(models.Model):
    _name = "helpdesk.building"
    _description = "Edificio"

    name = fields.Char(string="Nombre", required=True)
