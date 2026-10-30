from odoo import api, fields, models


class HelpdeskMachine(models.Model):
    _name = "helpdesk.machine"
    _description = "Equipo"

    _unique_name = models.Constraint(
        "UNIQUE(name)",
        "No puede cargar este equipo dado que ya existe otro equipo con el mismo identificador."
    )
    
    name = fields.Char(
        string="Identificador",
        required=True
    )
    type_id = fields.Many2one(
        string="Tipo",
        comodel_name="helpdesk.machine.type",
        required=True
    )
    has_technical_detail = fields.Boolean(
        string="Tienen detalle técnico",
        compute="_compute_has_technical_detail"
    )
    state = fields.Selection(
        string="Estado",
        selection=[
            ("in_use", "En uso"),
            ("broken", "Fuera de funcionamiento"),
            ("replaced", "Reemplazado")
        ],
        default="in_use",
        required=True
    )
    adquisition_date = fields.Date(
        string="Adquisición",
        default=fields.Date.today,
        required=True
    )
    operative_system = fields.Char(string="Sistema operativo")
    processor = fields.Char(string="Procesador")
    ram = fields.Integer(
        string="RAM",
        help="La capacidad de la memoria RAM de los equipos se expresa en GB."
    )
    motherboard = fields.Char(string="Placa madre")
    share_files = fields.Boolean(
        string="Comprate archivos",
        help="Si el equipo comparte archivo dentro de la red se debe tildar esta casilla."
    )
    file_server = fields.Boolean(
        string="Servidor de archivo",
        help="Si el equipo se comporta como servidor central de archivos se debe tildar esta casilla."
    )
    ip_address = fields.Char(string="Dirección IP")
    brand_id = fields.Many2one(
        string="Marca",
        comodel_name="helpdesk.machine.brand",
        domain="[('type_ids', 'in', [type_id])]"
    )
    model_id = fields.Many2one(
        string="Modelo",
        comodel_name="helpdesk.machine.brand.model",
        domain="[('brand_id', '=', brand_id)]",
    )
    building_id = fields.Many2one(
        string="Edificio",
        comodel_name="helpdesk.building",
        required=True
    )
    department_id = fields.Many2one(
        string="Dependencia",
        comodel_name="helpdesk.department",
        required=True
    )
    replacement_id = fields.Many2one(
        string="Reemplazo",
        comodel_name="helpdesk.machine"
    )
    drop_reason_id = fields.Many2one(
        string="Motivo de baja",
        comodel_name="helpdesk.drop.reason"
    )
    issue_ids = fields.One2many(
        string="Problemas",
        comodel_name="helpdesk.issue",
        inverse_name="machine_id"
    )
    anydesk_code = fields.Char(string="Identificador")
    anydesk_pwd = fields.Char(string="Contraseña de acceso")
    
    @api.depends("type_id")
    def _compute_has_technical_detail(self):
        for rec in self:
            if rec.type_id:
                rec.has_technical_detail = rec.type_id.technical_detail

            else:
                rec.has_technical_detail = False

    def show_replacement_button_action(self):
        self.ensure_one()

        return {
            "name": f"Reemplazo de equipo {self.name}",
            "type": "ir.actions.act_window",
            "res_model": "helpdesk.machine",
            "view_mode": "form",
            "res_id": self.replacement_id.id,
            "target": "current"
        }
   
    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)

        replaced_machine_id = self.env.context.get("replaced_machine_id")
        if replaced_machine_id and records:
            replaced_machine = self.browse(replaced_machine_id)
            if replaced_machine.exists():
                replaced_machine.write({
                    "replacement_id": records[0].id,
                    "state": "replaced"
                })
            
        return records
