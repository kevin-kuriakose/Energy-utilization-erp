frappe.ui.form.on('Energy Meter Reading', {
    current_reading: calculate_units,
    previous_reading: calculate_units,
    multiplying_factor: calculate_units
});

function calculate_units(frm) {
    let diff = flt(frm.doc.current_reading) - flt(frm.doc.previous_reading);
    let factor = flt(frm.doc.multiplying_factor) || 1.0;
    frm.set_value('units_consumed', diff * factor);
}
