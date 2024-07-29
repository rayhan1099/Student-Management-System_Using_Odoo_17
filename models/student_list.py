from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError

today = date.today()
print(today)
def calculate_age_in_ymd(days, calculated_age=None):
    years = days//365
    months = (days - years*365)//30
    days = (days - years*365 - months*30)
    calculated_age = str(years)+"Y "+str(months)+"M "+str(days)+"D"
    return calculated_age

class StudentList(models.Model):
    _name = 'student.list'
    _description = 'Student List'

    name = fields.Char(string="Name", required=True)
    fathers_name = fields.Char(string="Father's Name")
    mothers_name = fields.Char(string="Mohter's Name")
    dob = fields.Date(string="Date of Birth", required=True)
    institude = fields.Char(string="Instutude Name")
    dept = fields.Many2one('student.dept' ,string="Department")
    image = fields.Binary(string='Image')
    age = fields.Char(string='Age')

    @api.onchange('dob')
    def auto_update_age(self):
        if self.dob and self.dob > today:
            raise ValidationError("Date of Birth can't be greater than today")
        elif self.dob:
            age_in_days = (today - self.dob).days
            age = calculate_age_in_ymd(age_in_days)
            self.age = age


class StudentDept(models.Model):
    _name = "student.dept"
    _description = "Student Department"

    name = fields.Char(string="DepartmentName")
    dept_head = fields.Char(string="Head of Department")
