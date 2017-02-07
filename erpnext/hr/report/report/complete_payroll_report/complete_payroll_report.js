// Copyright (c) 2016, Prosadata and contributors
// For license information, please see license.txt

frappe.query_reports["Complete Payroll Report"] = {
	"filters": [
		{
			"fieldname":"user",
			"label": __("user"),
			"fieldtype": "Data"
		},
		
		{
			"fieldname":"from",
			"label": __("From"),
			"fieldtype": "Date"
		},

		{
			"fieldname":"end",
			"label": __("To"),
			"fieldtype": "Date"
		}
		


	],

	onload: function(report) {
		report.page.add_inner_button(__("Complete Payroll Report"), function() {
			
			var filters = report.get_values();
			frappe.set_route('script-report','Complete Payroll Report', {user: filters.user, from: filters.from, to: filters.end});
		});

	}
}

