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
        {"label": _("Generating Unit"), "fieldname": "generating_unit", "fieldtype": "Link",
         "options": "Generating Unit", "width": 140},
        {"label": _("Outage Type"), "fieldname": "outage_type", "fieldtype": "Data", "width": 150},
        {"label": _("Outage Start"), "fieldname": "outage_start", "fieldtype": "Datetime", "width": 140},
        {"label": _("Outage End"), "fieldname": "outage_end", "fieldtype": "Datetime", "width": 140},
        {"label": _("Lost Generation (MU)"), "fieldname": "lost_generation_mu", "fieldtype": "Float",
         "width": 150},
        {"label": _("Root Cause"), "fieldname": "root_cause", "fieldtype": "Data", "width": 200},
        {"label": _("SLDC Notified"), "fieldname": "notified_to_sldc", "fieldtype": "Check", "width": 110},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 90},
    ]


def get_data(filters):
    conditions = []
    values = {}

    if filters.get("power_plant"):
        conditions.append("power_plant = %(power_plant)s")
        values["power_plant"] = filters["power_plant"]

    if filters.get("outage_type"):
        conditions.append("outage_type = %(outage_type)s")
        values["outage_type"] = filters["outage_type"]

    if filters.get("from_date"):
        conditions.append("DATE(outage_start) >= %(from_date)s")
        values["from_date"] = filters["from_date"]

    if filters.get("to_date"):
        conditions.append("DATE(outage_start) <= %(to_date)s")
        values["to_date"] = filters["to_date"]

    where = "WHERE " + " AND ".join(conditions) if conditions else ""

    rows = frappe.db.sql(f"""
        SELECT
            power_plant, generating_unit, outage_type,
            outage_start, outage_end, lost_generation_mu,
            root_cause, notified_to_sldc, status
        FROM `tabOutage Report`
        {where}
        ORDER BY outage_start DESC
    """, values, as_dict=True)

    return [{
        "power_plant": r.power_plant,
        "generating_unit": r.generating_unit,
        "outage_type": r.outage_type,
        "outage_start": r.outage_start,
        "outage_end": r.outage_end,
        "lost_generation_mu": flt(r.lost_generation_mu),
        "root_cause": r.root_cause or "",
        "notified_to_sldc": r.notified_to_sldc,
        "status": r.status,
    } for r in rows]
