from odoo import fields, models


class HospitalVisit(models.Model):
    _name = 'hospital.visit'
    _description = 'Hospital Visit'

    visit_date = fields.Date(
        string='Дата',
        default=fields.Date.today,
    )

    doctor_name_ids = fields.Many2many(
        string='Лікар',
        comodel_name='hospital.doctor.name',
    )
    patient_name_ids = fields.Many2many(
        string='Пацієнт',
        comodel_name='hospital.patient.name',
    )

    disease_ids = fields.Many2many(
        string='Діагноз',
        comodel_name='hospital.disease.name',
    )
