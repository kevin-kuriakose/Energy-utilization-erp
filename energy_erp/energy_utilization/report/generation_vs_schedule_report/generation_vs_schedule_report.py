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
        {"label": _("Schedule Date"), "fieldname": "schedule_date", "fieldtype": "Date", "width": 110},
        {"label": _("Power Plant"), "fieldname": "power_plant", "fieldtype": "Link",
         "options": "Power Plant", "width": 150},
        {"label": _("ESO No."), "fieldname": "eso_name", "fieldtype": "Data", "width": 140},
        {"label": _("Declared Capacity (MW)"), "fieldname": "total_declared_capacity_mw",
         "fieldtype": "Float", "width": 160},
        {"label": _("Actual Injection (MW)"), "fieldname": "total_actual_injection_mw",
         "fieldtype": "Float", "width": 150},
        {"label": _("Deviation (MW)"), "fieldname": "deviation_mw", "fieldtype": "Float", "width": 120},
        {"label": _("Deviation (%)"), "fieldname": "deviation_pct", "fieldtype": "Percent", "width": 110},
        {"label": _("Issuing Authority"), "fieldname": "issuing_authority", "fieldtype": "Data", "width": 130},
    ]


def get_data(filters):
    conditions = []
    values = {}

    if filters.get("power_plant"):
        conditions.append("power_plant = %(power_plant)s")
        values["power_plant"] = filters["power_plant"]

    if filters.get("from_date"):
        conditions.append("schedule_date >= %(from_date)s")
        values["from_date"] = filters["from_date"]

    if filters.get("to_date"):
        conditions.append("schedule_date <= %(to_date)s")
        values["to_date"] = filters["to_date"]

    where = "WHERE " + " AND ".join(conditions) if conditions else ""

    rows = frappe.db.sql(f"""
        SELECT
            name as eso_name,
            schedule_date,
            power_plant,
            total_declared_capacity_mw,
            total_actual_injection_mw,
            issuing_authority
        FROM `tabEnergy Scheduling Order`
        {where}
        ORDER BY schedule_date DESC
    """, values, as_dict=True)

    result = []
    for row in rows:
        declared = flt(row.total_declared_capacity_mw)
        actual = flt(row.total_actual_injection_mw)
        deviation = actual - declared
        deviation_pct = (deviation / declared * 100) if declared else 0
        result.append({
            "schedule_date": row.schedule_date,
            "power_plant": row.power_plant,
            "eso_name": row.eso_name,
            "total_declared_capacity_mw": declared,
            "total_actual_injection_mw": actual,
            "deviation_mw": deviation,
            "deviation_pct": deviation_pct,
            "issuing_authority": row.issuing_authority,
        })
    return result
