frappe.ui.form.on('Grid Fault Report', {
    feeder: function(frm) {
        if (frm.doc.feeder) {
            frappe.db.get_value('Feeder', frm.doc.feeder, 'substation', function(r) {
                if (r && r.substation) frm.set_value('substation', r.substation);
            });
        }
    },
    restoration_datetime: function(frm) {
        if (frm.doc.fault_datetime && frm.doc.restoration_datetime) {
            let start = moment(frm.doc.fault_datetime);
            let end = moment(frm.doc.restoration_datetime);
            let minutes = end.diff(start, 'minutes');
            frm.set_value('outage_duration_minutes', minutes);
        }
    }
});
