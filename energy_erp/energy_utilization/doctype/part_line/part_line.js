frappe.ui.form.on('Part Line', {
    qty: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, 'total_cost',
            (row.qty || 0) * (row.unit_cost || 0)
        );
    },
    unit_cost: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, 'total_cost',
            (row.qty || 0) * (row.unit_cost || 0)
        );
    }
});
