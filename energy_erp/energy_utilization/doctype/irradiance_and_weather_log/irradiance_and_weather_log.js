frappe.ui.form.on('Irradiance and Weather Log', {
    actual_generation_kwh: calculate_pr,
    theoretical_generation_kwh: calculate_pr
});

function calculate_pr(frm) {
    let actual = flt(frm.doc.actual_generation_kwh);
    let theoretical = flt(frm.doc.theoretical_generation_kwh);
    if (theoretical > 0) {
        frm.set_value('performance_ratio_percent', (actual / theoretical) * 100);
    }
}
