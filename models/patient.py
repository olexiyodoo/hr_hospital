from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient'

    name = fields.Char()

    age = fields.Integer()

    doctor_ids = fields.Many2one(
        comodel_name='hospital.doctor', )
