import frappe


def after_install():
    frappe.db.commit()
    print("energy_erp installed successfully.")
