frappe.ui.form.on('GST Row', {
    taxable_amount: calculate_gst,
    gst_rate_percent: calculate_gst,
    igst_amount: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, 'total_gst_amount',
            flt(row.cgst_amount) + flt(row.sgst_amount) + flt(row.igst_amount)
        );
    }
});

function calculate_gst(frm, cdt, cdn) {
    let row = locals[cdt][cdn];
    let taxable = flt(row.taxable_amount);
    let rate = flt(row.gst_rate_percent);
    let total_gst = taxable * rate / 100;
    // Default split: CGST + SGST (intra-state); user can override for IGST
    let half = total_gst / 2;
    frappe.model.set_value(cdt, cdn, 'cgst_amount', half);
    frappe.model.set_value(cdt, cdn, 'sgst_amount', half);
    frappe.model.set_value(cdt, cdn, 'igst_amount', 0);
    frappe.model.set_value(cdt, cdn, 'total_gst_amount', total_gst);
}
