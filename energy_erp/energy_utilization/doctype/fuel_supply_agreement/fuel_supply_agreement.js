frappe.ui.form.on('Fuel Supply Agreement', {
    fuel_type: function(frm) {
        frm.set_query('grade', function() {
            return {
                filters: { fuel_type: frm.doc.fuel_type }
            };
        });
    }
});
