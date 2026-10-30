{
    "name": "Soporte técnico",
    "version": "19.0.1.0.0",
    "application": True,
    "summary": "Documentación de equipos y problemas en los mismos.",
    "depends": ["base"],
    "data": [
        # Security
        "security/security.xml",
        "security/ir.model.access.csv",
        # Wizards
        "wizards/helpdesk_drop_machine_wizard_views.xml",
        # Views
        "views/helpdesk_building_views.xml",
        "views/helpdesk_department_views.xml",
        "views/helpdesk_drop_reason_views.xml",
        "views/helpdesk_machine_views.xml",
        "views/helpdesk_machine_type_views.xml",
        "views/helpdesk_machine_brand_views.xml",
        "views/helpdesk_machine_brand_model_views.xml",
        "views/helpdesk_issue_views.xml",
        "views/menu.xml",
        # Data
        "data/helpdesk_machine_type_data.xml",
        "data/helpdesk_machine_brand_data.xml",
        "data/helpdesk_drop_reason_data.xml",
        "data/helpdesk_building_data.xml",
        "data/ir_sequence_data.xml"
    ],
    "author": "Municipalidad de Chajari",
    "license": "LGPL-3"
}


