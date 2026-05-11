import frappe
from frappe.model.document import Document
from frappe.utils import flt


class EnergySchedulingOrder(Document):

    def validate(self):
        self.calculate_totals()

    def calculate_totals(self):
        total_declared = 0.0
        total_actual = 0.0
        for row in self.unit_schedules or []:
            total_declared += flt(row.declared_capacity_mw)
            total_actual += flt(row.actual_injection_mw)
            row.deviation_mw = flt(row.actual_injection_mw) - flt(row.declared_capacity_mw)
        self.total_declared_capacity_mw = total_declared
        self.total_actual_injection_mw = total_actual
