import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt, getdate


class AnnualOverhaulPlan(Document):

    def validate(self):
        if getdate(self.planned_end_date) < getdate(self.planned_start_date):
            frappe.throw(_("Planned End Date cannot be before Planned Start Date."))
        if flt(self.estimated_cost) < 0:
            frappe.throw(_("Estimated Cost cannot be negative."))
