frappe.ui.form.on('Environmental Compliance Report', {
    sox_mg_nm3: check_compliance,
    nox_mg_nm3: check_compliance,
    spm_mg_nm3: check_compliance,
    sox_limit_mg_nm3: check_compliance,
    nox_limit_mg_nm3: check_compliance,
    spm_limit_mg_nm3: check_compliance
});

function check_compliance(frm) {
    frm.set_value('sox_compliant', flt(frm.doc.sox_mg_nm3) <= flt(frm.doc.sox_limit_mg_nm3) ? 1 : 0);
    frm.set_value('nox_compliant', flt(frm.doc.nox_mg_nm3) <= flt(frm.doc.nox_limit_mg_nm3) ? 1 : 0);
    frm.set_value('spm_compliant', flt(frm.doc.spm_mg_nm3) <= flt(frm.doc.spm_limit_mg_nm3) ? 1 : 0);
}
