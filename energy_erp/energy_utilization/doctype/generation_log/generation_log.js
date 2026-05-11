frappe.ui.form.on('Generation Log', {
    generating_unit: function(frm) {
        if (frm.doc.generating_unit) {
            frappe.db.get_value('Generating Unit', frm.doc.generating_unit, 'power_plant', function(r) {
                if (r && r.power_plant) {
                    frm.set_value('power_plant', r.power_plant);
                }
            });
        }
    },
    gross_generation_mu: function(frm) {
        frm.set_value('net_generation_mu',
            flt(frm.doc.gross_generation_mu) - flt(frm.doc.auxiliary_consumption_mu)
        );
    },
    auxiliary_consumption_mu: function(frm) {
        frm.set_value('net_generation_mu',
            flt(frm.doc.gross_generation_mu) - flt(frm.doc.auxiliary_consumption_mu)
        );
    }
});
