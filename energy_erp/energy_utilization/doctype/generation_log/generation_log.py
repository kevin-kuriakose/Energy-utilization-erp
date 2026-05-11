import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class GenerationLog(Document):

    def validate(self):
        self.calculate_net_generation()
        self.validate_values()

    def calculate_net_generation(self):
        self.net_generation_mu = flt(self.gross_generation_mu) - flt(self.auxiliary_consumption_mu)
        if self.net_generation_mu < 0:
            frappe.throw(_("Auxiliary Consumption cannot exceed Gross Generation."))

    def validate_values(self):
        if flt(self.gross_generation_mu) < 0:
            frappe.throw(_("Gross Generation cannot be negative."))
        if flt(self.plf_percent) < 0 or flt(self.plf_percent) > 100:
            frappe.throw(_("PLF % must be between 0 and 100."))
        if flt(self.heat_rate) < 0:
            frappe.throw(_("Heat Rate cannot be negative."))
