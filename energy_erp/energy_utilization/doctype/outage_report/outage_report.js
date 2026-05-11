frappe.ui.form.on('Outage Report', {
    generating_unit: function(frm) {
        if (frm.doc.generating_unit) {
            frappe.db.get_value('Generating Unit', frm.doc.generating_unit, 'power_plant', function(r) {
                if (r && r.power_plant) frm.set_value('power_plant', r.power_plant);
            });
        }
    },
    outage_type: function(frm) {
        if (frm.doc.outage_type === 'Forced Outage') {
            frappe.msgprint({
                title: __('Forced Outage'),
                message: __('Please ensure SLDC is notified within 30 minutes of forced outage.'),
                indicator: 'red'
            });
        }
    }
});
