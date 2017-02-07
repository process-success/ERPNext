# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe.model.document import Document


class workOrder_tool(Document):
	pass


#@frappe.whitelist()
#def get_employees(date, department=None, branch=None, company=None):
#	attendance_not_marked = []
#	attendance_marked = []
#employee_list = frappe.get_list("Employee", fields=["employee", "employee_name"], filters={
#		"status": "Active", "department": department, "branch": branch, "company": company}, order_by="employee_name")
#	marked_employee = {}
#	for emp in frappe.get_list("Attendance", fields=["employee", "status"],
#	filters={"att_date": date}):
#		marked_employee[emp['employee']] = emp['status']
#
#	for employee in employee_list:
#		employee['status'] = marked_employee.get(employee['employee'])
#		if employee['employee'] not in marked_employee:
#			attendance_not_marked.append(employee)
#		else:
#	attendance_marked.append(employee)
#	return {
#		"marked": attendance_marked,
#		"unmarked": attendance_not_marked
#	}


#@frappe.whitelist()
#def mark_employee_attendance(employee_list, status, date, company=None):
#	employee_list = json.loads(employee_list)
#	for employee in employee_list:
#		attendance = frappe.new_doc("Attendance")
#		attendance.employee = employee['employee']
#		attendance.employee_name = employee['employee_name']
#		attendance.att_date = date
#		attendance.status = status
#		if company:
#			attendance.company = company
#		else:
#			attendance.company = frappe.db.get_value("Employee", employee['employee'], "Company")
#		attendance.submit()
#
#@frappe.whitelist()
#def mark_single_employee_attendance(employee, employee_name,  date, status, company=None):
#	attendance = frappe.new_doc("Attendance")
#	attendance.employee = employee
#	attendance.employee_name = employee_name
#	attendance.att_date = date
#	attendance.status = status
#	if company:
#		attendance.company = company
#	else:
#		attendance.company = frappe.db.get_value("Employee", employee, "company")
#		attendance.submit()
#	return "mark_single_employee_attendance"

@frappe.whitelist()
def mark_single_workOrder(subject, status,  project, priority, sDate, eDate, eTime, progress):
	attendance = frappe.new_doc("Work Order")
	#attendance.naming_series = series
	attendance.subject = subject
	attendance.project = project
	attendance.status = employee_name
	attendance.priority = date
	attendance.status = status
	attendance.exp_start_date = sDate
	attendance.exp_end_date = eDate
	attendance.expected_time = eTime
	attendance.progress = progress
	attendance.submit()
	return "mark_single_workOrder"
