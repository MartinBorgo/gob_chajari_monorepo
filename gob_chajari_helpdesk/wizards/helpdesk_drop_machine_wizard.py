from odoo import fields, models
from odoo.exceptions import ValidationError

class HelpdeskDropMachineWizard(models.TransientModel):
    _name = "helpdesk.drop.machine.wizard"
    _description = "Wizard para dar de baja un equipo"

    machine_id = fields.Many2one(
        string="Equipo",
        comodel_name="helpdesk.machine",
        required=True
    )
    drop_reason_id = fields.Many2one(
        string="Motivo de la baja",
        comodel_name="helpdesk.drop.reason",
        required=True
    )

    def action_confirm(self):
        if self.drop_reason_id:
            self.machine_id.drop_reason_id = self.drop_reason_id
            self.machine_id.state = "broken"

        else:
            raise ValidationError(
                "Para poder dar de baja un equipo debe seleccionar "
                "un motivo de baja. En caso de que dicho motivo no se encuentre "
                "puede crearlo yendo Configuración > Propiedades de equipo > Motivos de baja."
            )

        return {"type": "ir.actions.act_window_close"}

