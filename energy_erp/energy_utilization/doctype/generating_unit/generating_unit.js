frappe.ui.form.on('Generating Unit', {
    refresh: function(frm) {
        frm.set_query('power_plant', function() {
            return { filters: { status: 'Operational' } };
        });
    }
});
