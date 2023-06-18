from odoo import fields, models


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor'

    name = fields.Char()

    profession = fields.Char()

    cabinet = fields.Integer()
