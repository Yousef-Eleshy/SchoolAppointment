# -*- coding: utf-8 -*-
from odoo import http
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pytz
from babel.dates import format_datetime, format_date

from werkzeug.urls import url_encode

from odoo import http, _, fields
from odoo.http import request
from odoo.tools import html2plaintext, DEFAULT_SERVER_DATETIME_FORMAT as dtf
from odoo.tools.misc import get_lang
from odoo.addons.website.controllers.main import Website
from odoo.addons.website_calendar.controllers.main import WebsiteCalendar

# Overriding the controller and inheriting from its class
class CustomWebsite(WebsiteCalendar):
    # Defining Route
    @http.route('/add', auth="public", website=True)
    def add(self, **kw):
        return http.request.render('websit_appointment.add',{})


    @http.route(['/website/calendar/<model("calendar.appointment.type"):appointment_type>/submit'], type='http', auth="public", website=True, method=["POST"])
    def calendar_appointment_submit(self, appointment_type, datetime_str, employee_id, name, phone, email, country_id=False, **kwargs):
        timezone = request.session['timezone']
        tz_session = pytz.timezone(timezone)
        date_start = tz_session.localize(fields.Datetime.from_string(datetime_str)).astimezone(pytz.utc)
        date_end = date_start + relativedelta(hours=appointment_type.appointment_duration)

        # check availability of the employee again (in case someone else booked while the client was entering the form)
        Employee = request.env['hr.employee'].sudo().browse(int(employee_id))
        if Employee.user_id and Employee.user_id.partner_id:
            if not Employee.user_id.partner_id.calendar_verify_availability(date_start, date_end):
                return request.redirect('/website/calendar/%s/appointment?failed=employee' % appointment_type.id)

        country_id = int(country_id) if country_id else None
        country_name = country_id and request.env['res.country'].browse(country_id).name or ''
        Partner = request.env['res.partner'].sudo().search([('email', '=like', email)], limit=1)
        if Partner:
            if not Partner.calendar_verify_availability(date_start, date_end):
                return request.redirect('/website/calendar/%s/appointment?failed=partner' % appointment_type.id)
            if not Partner.mobile or len(Partner.mobile) <= 5 and len(phone) > 5:
                Partner.write({'mobile': phone})
            if not Partner.country_id:
                Partner.country_id = country_id
        else:
            Partner = Partner.create({
                'name': name,
                'country_id': country_id,
                'mobile': phone,
                'email': email,

            })
            
        # Storing user input in the 'Description' section of the Calendar Event    
        description = ('Mobile Number: %s\n'
                       'Email: %s\n'
                       'First Name: %s\n'
                       'Last Name: %s\n'                        
						'Confirm Email: %s\n'
						'Please Choose Educational System: %s\n'
						'Student Name: %s\n'
						'Student Last: %s\n'
						'Student Name Arabic: %s\n'
						'Student Date Of Birth: %s\n'
						'Birthplace: %s\n'
						'Gender: %s\n'
						'Nationality: %s\n'
						'Student National Id: %s\n'
						'Student Passport: %s\n'
						'Address Line: %s\n'
						'City: %s\n'
						'State: %s\n'
						'Previous School/Nursery: %s\n'
						'Student Please Specify : %s\n'
						'Student Second language: %s\n'
						'Does your child require special accommodation?: %s\n'
						'Please Specify: %s\n'
						'Father Name: %s\n'
						'Father Last Name: %s\n'
						'Father Email: %s\n'
						'Father Confirm Email: %s\n'
						'Father Mobile Number: %s\n'
						'Father Home Phone: %s\n'
						'Father Nationality: %s\n'
						'Father National Id: %s\n'
						'Father Passport: %s\n'
						'Father Home Address: %s\n'
						'Father Educational Degree: %s\n'
						'Father Occupation: %s\n'
						'Father Company / Organization Name : %s\n'
						'Father English_language: %s\n'
						'Mother First Name: %s\n'
						'Mother Last Name: %s\n'
						'Mother Email: %s\n'
						'Mother Confirm Email: %s\n'
						'Mother Mobile Number: %s\n'
						'Mother Home Phone: %s\n'
						'Mother Nationality: %s\n'
						'Mother Nationality Id: %s\n'
						'Mother Passport No: %s\n'
						'Mother Home Address: %s\n'
						'Mother Educational Degree: %s\n'
						'Mother Occupation: %s\n'
						'Mother Company / Organization Name: %s\n'
						'Mother English Language Proficiency: %s\n'
						'Mother Marital Status: %s\n'
                        'Legal guardian: %s\n'
						'Other Legal guardian: %s\n'
						'Primary Contact Name: %s\n'
						'Primary Contact Mobile Phone: %s\n'
						'Primary Contact Relation to Student: %s\n'
						'Secondary Contact Name: %s\n'
						'Secondary Contact Mobile Phone: %s\n' 
						'Secondary Contact Relation to Student: %s\n'
						'Applicant’s Sibling: %s\n'
						'Sibling Name: %s\n'
						'Sibling Grade level: %s\n'
						'Sibling School: %s\n'
						'Condition: %s\n' % (phone, email,name, kwargs['last'],kwargs['confirm_email'],

						kwargs['stu_education_system'] if 'stu_education_system' in kwargs else '',
						kwargs['student_name'],
						kwargs['student_last'],
						kwargs['student_name_arabic'],
						kwargs['student_date'],
						kwargs['birthplace'],
						kwargs['gender'] if 'gender' in kwargs else '',
						kwargs['nationality'] if 'nationality' in kwargs else '',
						kwargs['stu_address'],
						kwargs['stu_passport'],
						kwargs['address_line'],
						kwargs['city'],
						kwargs['state'],
						kwargs['previous_school'] if 'previous_school' in kwargs else '',
						kwargs['stu_specify'],
						kwargs['stu_second_lang'] if 'stu_second_lang' in kwargs else '',
						kwargs['stu_accommodation'] if 'stu_accommodation' in kwargs else '',
						kwargs['wpforms[fields][41]'] if 'wpforms[fields][41]' in kwargs else '',
						kwargs['fname_first'],
						kwargs['flast_name'],
						kwargs['femail_primary'],
						kwargs['femail_secondary'],
						kwargs['fmobile_number'],
						kwargs['fhome_phone'],
						kwargs['fnationality'] if 'fnationality' in kwargs else '',
						kwargs['fnational_id'],
						kwargs['fpassport'],
						kwargs['fhome_address'],
						kwargs['feducational_degree'],
						kwargs['foccupation'],
						kwargs['mcompany_name'],
						kwargs['fenglish_language'] if 'fenglish_language' in kwargs else '',
						kwargs['first_name'],
						kwargs['last_name'],
						kwargs['primary_email'],
						kwargs['secondary_email'],
						kwargs['mmobile_number'],
						kwargs['home_phone'],
						kwargs['nationality_mother'] if 'nationality_mother' in kwargs else '',
						kwargs['nationality_id'],
						kwargs['passport_no'],
						kwargs['home_address'],
						kwargs['educational_degree'],
						kwargs['occupation'],
						kwargs['campany_organization'],
						kwargs['english_language'] if 'english_language' in kwargs else '',
						kwargs['marital_status'] if 'marital_status' in kwargs else '',
                        kwargs['legal_guardian'] if 'legal_guardian' in kwargs else '',                    
						kwargs['other_legal'],
						kwargs['primary_contact'],
						kwargs['emergency_contact_mobile'],
						kwargs['primary_contact_student'],
						kwargs['secondary_contact_name'],
						kwargs['secondary_contact_mobile'],
						kwargs['secondary_contact'],
						kwargs['applicant_sibling'] if 'applicant_sibling' in kwargs else '',
						kwargs['sibling_name'],
						kwargs['grade_level'],
						kwargs['sibling_school'],
						kwargs['condition'] if 'condition' in kwargs else '',
						
						))


        for question in appointment_type.question_ids:
            key = 'question_' + str(question.id)
            if question.question_type == 'checkbox':
                answers = question.answer_ids.filtered(lambda x: (key + '_answer_' + str(x.id)) in kwargs)
                description += question.name + ': ' + ', '.join(answers.mapped('name')) + '\n'
            elif kwargs.get(key):
                if question.question_type == 'text':
                    description += '\n* ' + question.name + ' *\n' + kwargs.get(key, False) + '\n\n'
                else:
                    description += question.name + ': ' + kwargs.get(key) + '\n'

        categ_id = request.env.ref('website_calendar.calendar_event_type_data_online_appointment')
        alarm_ids = appointment_type.reminder_ids and [(6, 0, appointment_type.reminder_ids.ids)] or []
        partner_ids = list(set([Employee.user_id.partner_id.id] + [Partner.id]))
        event = request.env['calendar.event'].sudo().create({
            'state': 'open',
            'name': _('%s with %s') % (appointment_type.name, name),
            'start': date_start.strftime(dtf),
            # FIXME master
            # we override here start_date(time) value because they are not properly
            # recomputed due to ugly overrides in event.calendar (reccurrencies suck!)
            #     (fixing them in stable is a pita as it requires a good rewrite of the
            #      calendar engine)
            'start_date': date_start.strftime(dtf),
            'start_datetime': date_start.strftime(dtf),
            'stop': date_end.strftime(dtf),
            'stop_datetime': date_end.strftime(dtf),
            'allday': False,
            'duration': appointment_type.appointment_duration,
            'description': description,
            'alarm_ids': alarm_ids,
            'location': appointment_type.location,
            'partner_ids': [(4, pid, False) for pid in partner_ids],
            'categ_ids': [(4, categ_id.id, False)],
            'appointment_type_id': appointment_type.id,
            'user_id': Employee.user_id.id,
        })
        event.attendee_ids.write({'state': 'accepted'})
        return request.redirect('/website/calendar/view/' + event.access_token + '?message=new')     