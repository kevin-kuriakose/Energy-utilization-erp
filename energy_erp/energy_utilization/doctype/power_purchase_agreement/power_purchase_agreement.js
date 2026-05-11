frappe.ui.form.on('Power Purchase Agreement', {
    refresh: function(frm) {
        if (frm.doc.ppa_end_date) {
            let today = frappe.datetime.get_today();
            let days_left = frappe.datetime.get_diff(frm.doc.ppa_end_date, today);
            if (days_left <= 180 && days_left > 0) {
                frm.dashboard.add_comment(
                    __('PPA expires in {0} days. Please initiate renewal.', [days_left]),
                    'orange', true
                );
            } else if (days_left <= 0) {
                frm.dashboard.add_comment(__('PPA has expired.'), 'red', true);
            }
        }
    }
});
