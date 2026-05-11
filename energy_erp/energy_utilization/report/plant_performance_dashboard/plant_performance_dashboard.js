frappe.query_reports["Plant Performance Dashboard"] = {
    filters: [
        {
            fieldname: "power_plant",
            label: __("Power Plant"),
            fieldtype: "Link",
            options: "Power Plant"
        },
        {
            fieldname: "from_date",
            label: __("From Date"),
            fieldtype: "Date",
            default: frappe.datetime.add_months(frappe.datetime.get_today(), -1)
        },
        {
            fieldname: "to_date",
            label: __("To Date"),
            fieldtype: "Date",
            default: frappe.datetime.get_today()
        }
    ]
};
