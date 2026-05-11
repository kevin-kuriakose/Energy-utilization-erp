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
        {"label": _("Report Month"), "fieldname": "report_month", "fieldtype": "Date", "width": 110},
        {"label": _("Feeder"), "fieldname": "feeder", "fieldtype": "Link",
         "options": "Feeder", "width": 150},
        {"label": _("Substation"), "fieldname": "substation", "fieldtype": "Link",
         "options": "Substation", "width": 150},
        {"label": _("DISCOM Zone"), "fieldname": "discom_zone", "fieldtype": "Data", "width": 120},
        {"label": _("Energy Input (MU)"), "fieldname": "energy_input_mu", "fieldtype": "Float", "width": 130},
        {"label": _("Energy Billed (MU)"), "fieldname": "energy_billed_mu", "fieldtype": "Float", "width": 130},
        {"label": _("Energy Collected (MU)"), "fieldname": "energy_collected_mu", "fieldtype": "Float", "width": 140},
        {"label": _("AT&C Loss (%)"), "fieldname": "atc_loss_percent", "fieldtype": "Percent", "width": 110},
        {"label": _("Target Loss (%)"), "fieldname": "target_loss_percent", "fieldtype": "Percent", "width": 110},
        {"label": _("Variance (%)"), "fieldname": "loss_variance_percent", "fieldtype": "Percent", "width": 100},
    ]


def get_data(filters):
    conditions = []
    values = {}

    if filters.get("feeder"):
        conditions.append("feeder = %(feeder)s")
        values["feeder"] = filters["feeder"]

    if filters.get("from_date"):
        conditions.append("report_month >= %(from_date)s")
        values["from_date"] = filters["from_date"]

    if filters.get("to_date"):
        conditions.append("report_month <= %(to_date)s")
        values["to_date"] = filters["to_date"]

    where = "WHERE " + " AND ".join(conditions) if conditions else ""

    rows = frappe.db.sql(f"""
        SELECT
            report_month, feeder, substation, discom_zone,
            energy_input_mu, energy_billed_mu, energy_collected_mu,
            atc_loss_percent, target_loss_percent, loss_variance_percent
        FROM `tabAT and C Loss Report`
        {where}
        ORDER BY report_month DESC, feeder
    """, values, as_dict=True)

    return [{
        "report_month": r.report_month,
        "feeder": r.feeder,
        "substation": r.substation,
        "discom_zone": r.discom_zone,
        "energy_input_mu": flt(r.energy_input_mu),
        "energy_billed_mu": flt(r.energy_billed_mu),
        "energy_collected_mu": flt(r.energy_collected_mu),
        "atc_loss_percent": flt(r.atc_loss_percent),
        "target_loss_percent": flt(r.target_loss_percent),
        "loss_variance_percent": flt(r.loss_variance_percent),
    } for r in rows]
