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
        {"label": _("Compliance Year"), "fieldname": "compliance_year", "fieldtype": "Data", "width": 120},
        {"label": _("RPO Category"), "fieldname": "rpo_category", "fieldtype": "Link",
         "options": "RPO Category", "width": 160},
        {"label": _("Obligation (MU)"), "fieldname": "obligation_mu", "fieldtype": "Float", "width": 120},
        {"label": _("Procured (MU)"), "fieldname": "procured_mu", "fieldtype": "Float", "width": 110},
        {"label": _("REC Used (MU)"), "fieldname": "rec_used_mu", "fieldtype": "Float", "width": 110},
        {"label": _("Deficit (MU)"), "fieldname": "deficit_mu", "fieldtype": "Float", "width": 110},
        {"label": _("Compliance Status"), "fieldname": "compliance_status", "fieldtype": "Data", "width": 140},
        {"label": _("SERC Notification"), "fieldname": "serc_notification_ref", "fieldtype": "Data", "width": 150},
    ]


def get_data(filters):
    conditions = []
    values = {}

    if filters.get("compliance_year"):
        conditions.append("compliance_year = %(compliance_year)s")
        values["compliance_year"] = filters["compliance_year"]

    where = "WHERE " + " AND ".join(conditions) if conditions else ""

    rows = frappe.db.sql(f"""
        SELECT
            compliance_year, rpo_category, obligation_mu, procured_mu,
            rec_used_mu, deficit_mu, compliance_status, serc_notification_ref
        FROM `tabRPO Compliance Record`
        {where}
        ORDER BY compliance_year DESC, rpo_category
    """, values, as_dict=True)

    return [{
        "compliance_year": r.compliance_year,
        "rpo_category": r.rpo_category,
        "obligation_mu": flt(r.obligation_mu),
        "procured_mu": flt(r.procured_mu),
        "rec_used_mu": flt(r.rec_used_mu),
        "deficit_mu": flt(r.deficit_mu),
        "compliance_status": r.compliance_status,
        "serc_notification_ref": r.serc_notification_ref or "",
    } for r in rows]
