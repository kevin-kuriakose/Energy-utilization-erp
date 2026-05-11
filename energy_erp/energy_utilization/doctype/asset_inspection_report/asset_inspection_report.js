frappe.ui.form.on('Asset Inspection Report', {
    condition_rating: function(frm) {
        if (frm.doc.condition_rating === 'Critical') {
            frappe.msgprint({
                title: __('Critical Condition'),
                message: __('Asset is in Critical condition. Please raise a Maintenance Work Order immediately.'),
                indicator: 'red'
            });
        }
    }
});
