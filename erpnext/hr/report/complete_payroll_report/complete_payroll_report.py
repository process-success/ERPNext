# Copyright (c) 2013, Prosadata and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import getdate
from frappe import _
import time
from datetime import datetime, timedelta

def execute(filters=None):
	person_details = []
	if len(filters) == 3:
		
		parse = str(filters["from"]).split("-")
		base = datetime(int(parse[0]),int(parse[1]),int(parse[2]),0,0,0)
		parse = str(filters["end"]).split("-")
		top = datetime(int(parse[0]),int(parse[1]),int(parse[2]),23,59,59)
		frappe.errprint(top)
		for acc in frappe.db.sql("select last_name, time_in,time_out,job_code,break from tabEmployees_Hours join tabcoastal_range_wineyards_employees e on coastal_range_wineyards_employees = e.name where e.user = '" + filters["user"] + "' and time_in BETWEEN CAST('" + str(base) + "' AS DATETIME) and CAST('" + str(top) + "' AS DATETIME) order by time_in", as_dict=1):
		
			person_details.append(acc)
			frappe.errprint(acc)
	
		
		columns = []
		data = []
		columns= get_columns(filters)
		data = get_result(filters, person_details)
		return columns, data
	else:
		return [], []

def get_columns(filters):
	columns = [
		_("week") + ":Data:90",
		_("weekday") + ":Data:90",
		_("time_in") + ":Datetime:90",
		_("time_out") + ":Datetime:90",
		_("job_code") + ":Int:90",
		_("break") + ":Data:90",
		_("Hours") + ":Int:90",
		_("Reg") + ":Time:90",
		_("Ovt1") + ":Time:90",
		_("Ovt2") + ":Time:90",
		_("Day_Total") + ":Time:90"]
	return columns

def toLetter(day_number):
	if day_number == 0:
		return "Mo"
	elif day_number == 1:
		return "Tu"
	elif day_number == 2:
		return "We" 
	elif day_number == 3:
		return "Th"
	elif day_number == 4:
		return "Fr"
	elif day_number == 5:
		return "Sa"
	else:
		return "Su"

def get_result(filters, person_details):
	i = 0
	week_number = 2
	result = []
	if len(person_details) > 0:
		date = str(person_details[0]["time_in"]).split(' ')[0]
		total_hours = timedelta(0)
		day_number = person_details[0]["time_in"].weekday()
		day = toLetter(day_number)
		person_details[0]["weekday"] = day
		person_details[0]["week"] = 1
		for row in person_details:
			if not row["break"]:
				row["break"] = ""
				hours = row["time_out"] - row["time_in"]
				row["Hours"] = hours
				result.append(row)
				if str(row["time_in"]).split(' ')[0] == date:
					total_hours = total_hours + hours
				else:
					result[i-1]["Day_Total"] = total_hours
					total_hours = hours
					day_number = row["time_in"].weekday()
					day = toLetter(day_number)
					result[i]["weekday"] = day
					if (day == "Su") and (result[i]["week"] != ""):
						result[i]["week"] = week_number
						
					elif (day == "Su"):
						result[i]["week"] = week_number - 1
					week_number = week_number + 1
					date = str(row["time_in"]).split(' ')[0]
				i = i+1
				
			else:
				prev = result[i-1]
				duration = str(row["time_out"] - row["time_in"])
				prev["break"] = str(int(duration.split(':')[0])*60 + int(duration.split(':')[1])) + "u"
		result[i-1]["Day_Total"] = total_hours
	return result
