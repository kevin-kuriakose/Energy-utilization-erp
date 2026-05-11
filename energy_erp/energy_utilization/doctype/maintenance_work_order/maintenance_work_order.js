frappe.ui.form.on('Maintenance Work Order', {
    plant_asset: function(frm) {
        if (frm.doc.plant_asset) {
            frappe.db.get_value('Plant Asset', frm.doc.plant_asset, 'power_plant', function(r) {
                if (r && r.power_plant) {
                    frm.set_value('power_plant', r.power_plant);
                }
            });
        }
    },
    labour_cost: function(frm) {
        frm.set_value('total_cost',
            flt(frm.doc.total_parts_cost) + flt(frm.doc.labour_cost)
        );
    }
});
