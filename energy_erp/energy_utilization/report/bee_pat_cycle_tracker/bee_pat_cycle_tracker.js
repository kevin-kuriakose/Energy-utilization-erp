frappe.query_reports["BEE PAT Cycle Tracker"] = {
    filters: [
        {fieldname: "power_plant", label: __("Power Plant"), fieldtype: "Link", options: "Power Plant"},
        {fieldname: "pat_cycle", label: __("PAT Cycle"), fieldtype: "Select",
         options: "\nPAT Cycle I (2012-15)\nPAT Cycle II (2016-19)\nPAT Cycle III (2017-20)\nPAT Cycle IV (2018-21)\nPAT Cycle V (2019-22)\nPAT Cycle VI (2020-23)\nPAT Cycle VII (2022-24)"}
    ]
};
