from odoo import fields, models


class HelpdeskMachineBrand(models.Model):
    _name = "helpdesk.machine.brand"
    _description = "Marca"

    name = fields.Char(string="Nombre", required=True)
    type_ids = fields.Many2many(
        string="Tipo de equipo",
        comodel_name="helpdesk.machine.type",
        relation="brand_type_rel",
        column1="brand_id",
        column2="type_id",
    )
    model_ids = fields.One2many(
        string="Modelos",
        comodel_name="helpdesk.machine.brand.model",
        inverse_name="brand_id"
    )
