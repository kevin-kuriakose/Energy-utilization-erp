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
        {"label": _("Generating Unit"), "fieldname": "generating_unit", "fieldtype": "Link",
         "options": "Generating Unit", "width": 150},
        {"label": _("Consumption Date"), "fieldname": "consumption_date", "fieldtype": "Date", "width": 120},
        {"label": _("Fuel Type"), "fieldname": "fuel_type", "fieldtype": "Data", "width": 100},
        {"label": _("Quantity (MT)"), "fieldname": "quantity_mt", "fieldtype": "Float", "width": 110},
        {"label": _("GCV (kcal/kg)"), "fieldname": "gcv_kcal_kg", "fieldtype": "Float", "width": 120},
        {"label": _("Heat Input (Mkcal)"), "fieldname": "heat_input_mkcal", "fieldtype": "Float", "width": 130},
        {"label": _("SFC (kg/kWh)"), "fieldname": "sfc_kg_kwh", "fieldtype": "Float", "width": 110},
        {"label": _("Net Gen (MU)"), "fieldname": "net_generation_mu", "fieldtype": "Float", "width": 110},
        {"label": _("Heat Rate (kcal/kWh)"), "fieldname": "heat_rate", "fieldtype": "Float", "width": 140},
    ]


def get_data(filters):
    conditions = []
    values = {}

    if filters.get("generating_unit"):
        conditions.append("fcl.generating_unit = %(generating_unit)s")
        values["generating_unit"] = filters["generating_unit"]

    if filters.get("from_date"):
        conditions.append("fcl.consumption_date >= %(from_date)s")
        values["from_date"] = filters["from_date"]

    if filters.get("to_date"):
        conditions.append("fcl.consumption_date <= %(to_date)s")
        values["to_date"] = filters["to_date"]

    where = "WHERE " + " AND ".join(conditions) if conditions else ""

    rows = frappe.db.sql(f"""
        SELECT
            fcl.generating_unit,
            fcl.consumption_date,
            fcl.fuel_type,
            fcl.quantity_mt,
            fcl.gcv_kcal_kg,
            fcl.heat_input_mkcal,
            fcl.sfc_kg_kwh,
            gl.net_generation_mu,
            gl.heat_rate
        FROM `tabFuel Consumption Log` fcl
        LEFT JOIN `tabGeneration Log` gl ON gl.name = fcl.generation_log
        {where}
        ORDER BY fcl.consumption_date DESC
    """, values, as_dict=True)

    result = []
    for row in rows:
        result.append({
            "generating_unit": row.generating_unit,
            "consumption_date": row.consumption_date,
            "fuel_type": row.fuel_type,
            "quantity_mt": flt(row.quantity_mt),
            "gcv_kcal_kg": flt(row.gcv_kcal_kg),
            "heat_input_mkcal": flt(row.heat_input_mkcal),
            "sfc_kg_kwh": flt(row.sfc_kg_kwh),
            "net_generation_mu": flt(row.net_generation_mu),
            "heat_rate": flt(row.heat_rate),
        })
    return result
