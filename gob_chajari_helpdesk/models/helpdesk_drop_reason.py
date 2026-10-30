from odoo import fields, models


class HelpdeskDropReason(models.Model):
    _name = "helpdesk.drop.reason"
    _description = "Motivo de baja"

    name = fields.Char(string="Motivo", required=True)
    machine_ids = fields.One2many(
        string="Equipos",
        comodel_name="helpdesk.machine",
        inverse_name="drop_reason_id"
    )
