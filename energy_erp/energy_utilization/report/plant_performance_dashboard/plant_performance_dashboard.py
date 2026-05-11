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
         "options": "Power Plant", "width": 160},
        {"label": _("Generating Unit"), "fieldname": "generating_unit", "fieldtype": "Link",
         "options": "Generating Unit", "width": 140},
        {"label": _("Log Date"), "fieldname": "log_date", "fieldtype": "Date", "width": 100},
        {"label": _("Gross Gen (MU)"), "fieldname": "gross_generation_mu", "fieldtype": "Float",
         "width": 120},
        {"label": _("Net Gen (MU)"), "fieldname": "net_generation_mu", "fieldtype": "Float",
         "width": 120},
        {"label": _("Aux Consumption (MU)"), "fieldname": "auxiliary_consumption_mu",
         "fieldtype": "Float", "width": 140},
        {"label": _("PLF (%)"), "fieldname": "plf_percent", "fieldtype": "Percent", "width": 90},
        {"label": _("Target PLF (%)"), "fieldname": "target_plf_percent", "fieldtype": "Percent",
         "width": 110},
        {"label": _("Heat Rate (kcal/kWh)"), "fieldname": "heat_rate", "fieldtype": "Float",
         "width": 140},
        {"label": _("Availability (%)"), "fieldname": "availability_factor_percent",
         "fieldtype": "Percent", "width": 110},
    ]


def get_data(filters):
    conditions = []
    values = {}

    if filters.get("power_plant"):
        conditions.append("gl.power_plant = %(power_plant)s")
        values["power_plant"] = filters["power_plant"]

    if filters.get("from_date"):
        conditions.append("gl.log_date >= %(from_date)s")
        values["from_date"] = filters["from_date"]

    if filters.get("to_date"):
        conditions.append("gl.log_date <= %(to_date)s")
        values["to_date"] = filters["to_date"]

    where = "WHERE " + " AND ".join(conditions) if conditions else ""

    rows = frappe.db.sql(f"""
        SELECT
            gl.power_plant,
            gl.generating_unit,
            gl.log_date,
            gl.gross_generation_mu,
            gl.net_generation_mu,
            gl.auxiliary_consumption_mu,
            gl.plf_percent,
            gl.target_plf_percent,
            gl.heat_rate,
            gl.availability_factor_percent
        FROM `tabGeneration Log` gl
        {where}
        ORDER BY gl.log_date DESC, gl.power_plant
    """, values, as_dict=True)

    result = []
    for row in rows:
        result.append({
            "power_plant": row.power_plant,
            "generating_unit": row.generating_unit,
            "log_date": row.log_date,
            "gross_generation_mu": flt(row.gross_generation_mu),
            "net_generation_mu": flt(row.net_generation_mu),
            "auxiliary_consumption_mu": flt(row.auxiliary_consumption_mu),
            "plf_percent": flt(row.plf_percent),
            "target_plf_percent": flt(row.target_plf_percent),
            "heat_rate": flt(row.heat_rate),
            "availability_factor_percent": flt(row.availability_factor_percent),
        })
    return result
