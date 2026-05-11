frappe.query_reports["Outage Analysis Report"] = {
    filters: [
        {fieldname: "power_plant", label: __("Power Plant"), fieldtype: "Link", options: "Power Plant"},
        {fieldname: "outage_type", label: __("Outage Type"), fieldtype: "Select",
         options: "\nPlanned Outage\nForced Outage\nAnnual Overhaul\nExtension of Overhaul\nPartial Load Restriction"},
        {fieldname: "from_date", label: __("From Date"), fieldtype: "Date",
         default: frappe.datetime.add_months(frappe.datetime.get_today(), -3)},
        {fieldname: "to_date", label: __("To Date"), fieldtype: "Date",
         default: frappe.datetime.get_today()}
    ]
};
