frappe.ui.form.on('RPO Compliance Record', {
    obligation_mu: calculate_deficit,
    procured_mu: calculate_deficit,
    rec_used_mu: calculate_deficit
});

function calculate_deficit(frm) {
    let obligation = flt(frm.doc.obligation_mu);
    let total = flt(frm.doc.procured_mu) + flt(frm.doc.rec_used_mu);
    frm.set_value('deficit_mu', Math.max(0, obligation - total));
}
