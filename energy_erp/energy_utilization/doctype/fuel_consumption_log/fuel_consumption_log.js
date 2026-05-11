frappe.ui.form.on('Fuel Consumption Log', {
    quantity_mt: calculate_heat_input,
    gcv_kcal_kg: calculate_heat_input
});

function calculate_heat_input(frm) {
    let qty = flt(frm.doc.quantity_mt);
    let gcv = flt(frm.doc.gcv_kcal_kg);
    if (qty > 0 && gcv > 0) {
        frm.set_value('heat_input_mkcal', (qty * gcv * 1000) / 1000000);
    }
}
