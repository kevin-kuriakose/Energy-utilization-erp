frappe.query_reports["AT and C Loss Trend"] = {
    filters: [
        {fieldname: "feeder", label: __("Feeder"), fieldtype: "Link", options: "Feeder"},
        {fieldname: "from_date", label: __("From Date"), fieldtype: "Date",
         default: frappe.datetime.add_months(frappe.datetime.get_today(), -6)},
        {fieldname: "to_date", label: __("To Date"), fieldtype: "Date",
         default: frappe.datetime.get_today()}
    ]
};
