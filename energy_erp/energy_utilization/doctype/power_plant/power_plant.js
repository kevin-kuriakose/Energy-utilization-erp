frappe.ui.form.on('Power Plant', {
    refresh: function(frm) {
        frm.set_query('ppa', function() {
            return {
                filters: {
                    'power_plant': frm.doc.name
                }
            };
        });
    }
});
