from odoo import fields, models


class HospitalVisit(models.Model):
    _name = 'hospital.visit'
    _description = 'Hospital Visit'

    visit_date = fields.Date(
        string='Date',
        default=fields.Date.today,)

    doctor_ids = fields.Many2one(
        comodel_name='hospital.doctor',)

    patient_ids = fields.Many2one(
        comodel_name='hospital.patient',)

    disease_ids = fields.Many2one(
        comodel_name='hospital.disease',)
