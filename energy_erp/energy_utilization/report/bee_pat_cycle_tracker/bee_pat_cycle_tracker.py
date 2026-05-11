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
        {"label": _("PAT Cycle"), "fieldname": "pat_cycle", "fieldtype": "Data", "width": 180},
        {"label": _("SEC Baseline"), "fieldname": "sec_baseline", "fieldtype": "Float", "width": 120},
        {"label": _("SEC Target"), "fieldname": "sec_target", "fieldtype": "Float", "width": 110},
        {"label": _("SEC Achieved"), "fieldname": "sec_achieved", "fieldtype": "Float", "width": 120},
        {"label": _("SEC Improvement"), "fieldname": "sec_improvement", "fieldtype": "Float", "width": 130},
        {"label": _("Energy Savings (MTOE)"), "fieldname": "energy_savings_mtoe", "fieldtype": "Float",
         "width": 150},
        {"label": _("ESCert Eligible"), "fieldname": "escert_eligible", "fieldtype": "Check", "width": 110},
        {"label": _("ESCert Qty"), "fieldname": "escert_quantity", "fieldtype": "Float", "width": 100},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 130},
    ]


def get_data(filters):
    conditions = []
    values = {}

    if filters.get("power_plant"):
        conditions.append("power_plant = %(power_plant)s")
        values["power_plant"] = filters["power_plant"]

    if filters.get("pat_cycle"):
        conditions.append("pat_cycle = %(pat_cycle)s")
        values["pat_cycle"] = filters["pat_cycle"]

    where = "WHERE " + " AND ".join(conditions) if conditions else ""

    rows = frappe.db.sql(f"""
        SELECT
            power_plant, pat_cycle, sec_baseline, sec_target, sec_achieved,
            energy_savings_mtoe, escert_eligible, escert_quantity, status
        FROM `tabBEE Energy Audit`
        {where}
        ORDER BY power_plant, pat_cycle
    """, values, as_dict=True)

    result = []
    for row in rows:
        baseline = flt(row.sec_baseline)
        achieved = flt(row.sec_achieved)
        improvement = baseline - achieved if baseline > 0 else 0
        result.append({
            "power_plant": row.power_plant,
            "pat_cycle": row.pat_cycle,
            "sec_baseline": baseline,
            "sec_target": flt(row.sec_target),
            "sec_achieved": achieved,
            "sec_improvement": improvement,
            "energy_savings_mtoe": flt(row.energy_savings_mtoe),
            "escert_eligible": row.escert_eligible,
            "escert_quantity": flt(row.escert_quantity),
            "status": row.status,
        })
    return result
