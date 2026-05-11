import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt, getdate


class MaintenanceWorkOrder(Document):

    def validate(self):
        self.validate_dates()
        self.calculate_costs()

    def validate_dates(self):
        if self.scheduled_start_date and self.scheduled_end_date:
            if getdate(self.scheduled_end_date) < getdate(self.scheduled_start_date):
                frappe.throw(_("Scheduled End Date cannot be before Scheduled Start Date."))

    def calculate_costs(self):
        total_parts = 0.0
        for row in self.parts_used or []:
            row.total_cost = flt(row.qty) * flt(row.unit_cost)
            total_parts += flt(row.total_cost)
        self.total_parts_cost = total_parts
        self.total_cost = total_parts + flt(self.labour_cost)
