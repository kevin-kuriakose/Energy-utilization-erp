frappe.ui.form.on('Fuel Stock Entry', {
    opening_stock_mt: calculate_closing,
    receipts_mt: calculate_closing,
    consumption_mt: calculate_closing
});

function calculate_closing(frm) {
    let closing = flt(frm.doc.opening_stock_mt) + flt(frm.doc.receipts_mt) - flt(frm.doc.consumption_mt);
    frm.set_value('closing_stock_mt', closing);
    if (flt(frm.doc.consumption_mt) > 0) {
        frm.set_value('days_of_stock', closing / (flt(frm.doc.consumption_mt) / 30.0));
    }
}
