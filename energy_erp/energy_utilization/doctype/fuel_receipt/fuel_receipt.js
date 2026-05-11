frappe.ui.form.on('Fuel Receipt', {
    fuel_supply_agreement: function(frm) {
        if (frm.doc.fuel_supply_agreement) {
            frappe.db.get_value('Fuel Supply Agreement', frm.doc.fuel_supply_agreement,
                ['power_plant', 'fuel_type'], function(r) {
                    if (r) {
                        if (r.power_plant) frm.set_value('power_plant', r.power_plant);
                        if (r.fuel_type) frm.set_value('fuel_type', r.fuel_type);
                    }
                }
            );
        }
    }
});
