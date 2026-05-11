frappe.ui.form.on('Spare Parts Inventory', {
    refresh: function(frm) {
        if (frm.doc.quantity_on_hand <= frm.doc.reorder_level && !frm.is_new()) {
            frm.dashboard.add_comment(__('Stock is at or below reorder level. Please replenish.'), 'orange', true);
        }
    }
});
