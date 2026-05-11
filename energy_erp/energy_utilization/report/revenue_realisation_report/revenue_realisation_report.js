frappe.query_reports["Revenue Realisation Report"] = {
    filters: [
        {fieldname: "power_plant", label: __("Power Plant"), fieldtype: "Link", options: "Power Plant"},
        {fieldname: "status", label: __("Status"), fieldtype: "Select",
         options: "\nDraft\nIssued\nPaid\nOverdue\nDisputed\nCancelled"},
        {fieldname: "from_date", label: __("From Date"), fieldtype: "Date",
         default: frappe.datetime.add_months(frappe.datetime.get_today(), -6)},
        {fieldname: "to_date", label: __("To Date"), fieldtype: "Date",
         default: frappe.datetime.get_today()}
    ]
};
