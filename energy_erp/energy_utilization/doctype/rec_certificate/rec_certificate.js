frappe.ui.form.on('REC Certificate', {
    refresh: function(frm) {
        if (frm.doc.expiry_date) {
            let days = frappe.datetime.get_diff(frm.doc.expiry_date, frappe.datetime.get_today());
            if (days <= 30 && days > 0 && frm.doc.status === 'Available') {
                frm.dashboard.add_comment(__('REC expires in {0} days.', [days]), 'orange', true);
            }
        }
    }
});
