frappe.ui.form.on('AT and C Loss Report', {
    energy_input_mu: calculate_atc,
    energy_collected_mu: calculate_atc,
    target_loss_percent: calculate_atc
});

function calculate_atc(frm) {
    let input = flt(frm.doc.energy_input_mu);
    let collected = flt(frm.doc.energy_collected_mu);
    if (input > 0) {
        let atc = (1 - collected / input) * 100;
        frm.set_value('atc_loss_percent', atc);
        frm.set_value('loss_variance_percent', atc - flt(frm.doc.target_loss_percent));
    }
}
