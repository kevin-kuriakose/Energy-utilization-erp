import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class EnvironmentalComplianceReport(Document):

    def validate(self):
        self.assess_compliance()

    def assess_compliance(self):
        self.sox_compliant = 1 if flt(self.sox_mg_nm3) <= flt(self.sox_limit_mg_nm3) else 0
        self.nox_compliant = 1 if flt(self.nox_mg_nm3) <= flt(self.nox_limit_mg_nm3) else 0
        self.spm_compliant = 1 if flt(self.spm_mg_nm3) <= flt(self.spm_limit_mg_nm3) else 0
        self.overall_compliant = 1 if (self.sox_compliant and self.nox_compliant and self.spm_compliant) else 0

        if not self.overall_compliant:
            self.status = "Non-Compliant"
            frappe.msgprint(
                _("One or more emission parameters exceed MoEF norms. Status set to Non-Compliant."),
                alert=True
            )
