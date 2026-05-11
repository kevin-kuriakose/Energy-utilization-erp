import frappe
from frappe import _
from frappe.utils import flt


def execute(filters=None):
    filters = filters or {}
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {"label": _("Power Plant"), "fieldname": "power_plant", "fieldtype": "Link",
         "options": "Power Plant", "width": 150},
        {"label": _("Billing Month"), "fieldname": "billing_month", "fieldtype": "Date", "width": 110},
        {"label": _("Invoice No."), "fieldname": "invoice_number", "fieldtype": "Data", "width": 130},
        {"label": _("Fixed Charge"), "fieldname": "fixed_charge_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Variable Charge"), "fieldname": "variable_charge_amount", "fieldtype": "Currency", "width": 130},
        {"label": _("UI Charge"), "fieldname": "ui_charge_amount", "fieldtype": "Currency", "width": 110},
        {"label": _("Total GST"), "fieldname": "total_gst_amount", "fieldtype": "Currency", "width": 110},
        {"label": _("Total Amount"), "fieldname": "total_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Due Date"), "fieldname": "due_date", "fieldtype": "Date", "width": 100},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 90},
    ]


def get_data(filters):
    conditions = []
    values = {}

    if filters.get("power_plant"):
        conditions.append("power_plant = %(power_plant)s")
        values["power_plant"] = filters["power_plant"]

    if filters.get("from_date"):
        conditions.append("billing_month >= %(from_date)s")
        values["from_date"] = filters["from_date"]

    if filters.get("to_date"):
        conditions.append("billing_month <= %(to_date)s")
        values["to_date"] = filters["to_date"]

    if filters.get("status"):
        conditions.append("status = %(status)s")
        values["status"] = filters["status"]

    where = "WHERE " + " AND ".join(conditions) if conditions else ""

    rows = frappe.db.sql(f"""
        SELECT
            power_plant, billing_month, invoice_number,
            fixed_charge_amount, variable_charge_amount, ui_charge_amount,
            total_gst_amount, total_amount, due_date, status
        FROM `tabEnergy Bill`
        {where}
        ORDER BY billing_month DESC, power_plant
    """, values, as_dict=True)

    return [{
        "power_plant": r.power_plant,
        "billing_month": r.billing_month,
        "invoice_number": r.invoice_number or "",
        "fixed_charge_amount": flt(r.fixed_charge_amount),
        "variable_charge_amount": flt(r.variable_charge_amount),
        "ui_charge_amount": flt(r.ui_charge_amount),
        "total_gst_amount": flt(r.total_gst_amount),
        "total_amount": flt(r.total_amount),
        "due_date": r.due_date,
        "status": r.status,
    } for r in rows]
