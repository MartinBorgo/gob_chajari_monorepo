from odoo import fields, models


class HelpdeskMachineBrandModel(models.Model):
    _name = "helpdesk.machine.brand.model"
    _description = "Modelo"

    name = fields.Char(string="Nombre", required=True)
    brand_id = fields.Many2one(
        string="Marca",
        comodel_name="helpdesk.machine.brand",
        required=True
    )
