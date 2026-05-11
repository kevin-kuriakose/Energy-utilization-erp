frappe.ui.form.on('Energy Bill', {
    fixed_charge_amount: calculate_subtotal,
    variable_charge_amount: calculate_subtotal,
    ui_charge_amount: calculate_subtotal,
    incentive_amount: calculate_subtotal,
    penalty_amount: calculate_subtotal
});

function calculate_subtotal(frm) {
    let subtotal = flt(frm.doc.fixed_charge_amount)
        + flt(frm.doc.variable_charge_amount)
        + flt(frm.doc.ui_charge_amount)
        + flt(frm.doc.incentive_amount)
        - flt(frm.doc.penalty_amount);
    frm.set_value('subtotal_amount', subtotal);
}
