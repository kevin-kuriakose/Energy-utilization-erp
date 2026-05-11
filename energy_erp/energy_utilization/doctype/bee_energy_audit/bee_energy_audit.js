frappe.ui.form.on('BEE Energy Audit', {
    sec_achieved: function(frm) {
        if (flt(frm.doc.sec_achieved) <= flt(frm.doc.sec_target) && flt(frm.doc.sec_target) > 0) {
            frm.set_value('escert_eligible', 1);
        } else {
            frm.set_value('escert_eligible', 0);
        }
    }
});
