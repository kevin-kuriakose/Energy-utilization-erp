import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class RpoComplianceRecord(Document):

    def validate(self):
        self.calculate_deficit()

    def calculate_deficit(self):
        obligation = flt(self.obligation_mu)
        procured = flt(self.procured_mu)
        rec_used = flt(self.rec_used_mu)
        total_met = procured + rec_used
        self.deficit_mu = max(0, obligation - total_met)

        if obligation > 0:
            if total_met >= obligation:
                self.compliance_status = "Compliant"
            elif total_met > 0:
                self.compliance_status = "Partially Compliant"
            else:
                self.compliance_status = "Non-Compliant"
