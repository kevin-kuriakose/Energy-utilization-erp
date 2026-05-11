frappe.ui.form.on('Capital Project', {
    refresh: function(frm) {
        if (frm.doc.sanctioned_cost && frm.doc.expenditure_to_date) {
            let pct = (flt(frm.doc.expenditure_to_date) / flt(frm.doc.sanctioned_cost)) * 100;
            frm.dashboard.add_comment(__('Budget utilisation: {0}%', [pct.toFixed(1)]), 'blue', true);
        }
    }
});
