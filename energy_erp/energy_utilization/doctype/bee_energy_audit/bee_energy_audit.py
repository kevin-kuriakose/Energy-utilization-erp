import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class BeeEnergyAudit(Document):

    def validate(self):
        self.evaluate_escert_eligibility()

    def evaluate_escert_eligibility(self):
        sec_baseline = flt(self.sec_baseline)
        sec_achieved = flt(self.sec_achieved)
        sec_target = flt(self.sec_target)

        if sec_achieved > 0 and sec_target > 0 and sec_achieved <= sec_target:
            self.escert_eligible = 1
        else:
            self.escert_eligible = 0
            self.escert_quantity = 0
