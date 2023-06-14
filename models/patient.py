from odoo import fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    first_name = fields.Char()
    last_name = fields.Char()
    doctor_name_ids = fields.Many2many(
        comodel_name='hr.hospital.name'
    )

