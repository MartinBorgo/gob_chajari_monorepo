from odoo import fields, models


class HelpdeskMachineType(models.Model):
    _name = "helpdesk.machine.type"
    _description = "Tipo de equipo"

    name = fields.Char(string="Nombre", required=True)
    technical_detail = fields.Boolean(
        string="Detalle técnico",
        help="""Los tipos que poseen detalle tecnicos permiten
        al usuario cargar caracteristicas como el procesador, cantidad
        de memoria RAM entre otras cosas. Activar si dicha información
        es relevante para el equipo de soporte.""",
        default=False
    )
    machine_ids = fields.One2many(
        string="Equipos",
        comodel_name="helpdesk.machine",
        inverse_name="type_id"
    )
    brand_ids = fields.Many2many(
        string="Marcas",
        comodel_name="helpdesk.machine.brand",
        relation="brand_type_rel",
        column1="type_id",
        column2="brand_id"
    )
    
