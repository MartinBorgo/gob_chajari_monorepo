from odoo import api, fields, models


class HelpdeskIssue(models.Model):
    _name = "helpdesk.issue"
    _description = "Problema"

    name = fields.Char(
        string="Idenfiticador",
        default="Nuevo problema",
        required=True
    )
    date = fields.Date(
        string="Fecha",
        default=fields.Date.today,
        required=True
    ) 
    description = fields.Html(
        string="Descripción",
        default="<h2>Detalle</h2><p><br/></p><h2>Solución</h2>"
    )
    machine_id = fields.Many2one(
        string="Equipo",
        comodel_name="helpdesk.machine",
        required=True
    )

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        Sequence = self.env["ir.sequence"]
        for rec in records:
            if rec.name == "Nuevo problema":
                rec.name = Sequence.next_by_code("helpdesk.issue")

        return records
