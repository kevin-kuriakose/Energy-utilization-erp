frappe.ui.form.on('Deviation Settlement', {
    scheduled_mu: calculate_deviation,
    actual_mu: calculate_deviation,
    dsm_rate: calculate_deviation
});

function calculate_deviation(frm) {
    let dev = flt(frm.doc.actual_mu) - flt(frm.doc.scheduled_mu);
    frm.set_value('deviation_mu', dev);
    let net = Math.abs(dev) * 1000000 * flt(frm.doc.dsm_rate);
    frm.set_value('net_payable', net);
}
