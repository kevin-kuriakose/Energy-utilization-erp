frappe.query_reports["Fuel Cost per Unit Report"] = {
    filters: [
        {fieldname: "generating_unit", label: __("Generating Unit"), fieldtype: "Link",
         options: "Generating Unit"},
        {fieldname: "from_date", label: __("From Date"), fieldtype: "Date",
         default: frappe.datetime.add_months(frappe.datetime.get_today(), -1)},
        {fieldname: "to_date", label: __("To Date"), fieldtype: "Date",
         default: frappe.datetime.get_today()}
    ]
};
