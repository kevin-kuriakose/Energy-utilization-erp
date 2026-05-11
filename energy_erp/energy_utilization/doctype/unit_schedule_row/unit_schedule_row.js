frappe.ui.form.on('Unit Schedule Row', {
    actual_injection_mw: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, 'deviation_mw',
            (row.actual_injection_mw || 0) - (row.declared_capacity_mw || 0)
        );
    },
    declared_capacity_mw: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, 'deviation_mw',
            (row.actual_injection_mw || 0) - (row.declared_capacity_mw || 0)
        );
    }
});
