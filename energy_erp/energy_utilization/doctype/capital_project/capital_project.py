import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt, getdate


class CapitalProject(Document):

    def validate(self):
        if self.start_date and self.expected_completion_date:
            if getdate(self.expected_completion_date) < getdate(self.start_date):
                frappe.throw(_("Expected Completion Date cannot be before Start Date."))
        if flt(self.sanctioned_cost) < 0:
            frappe.throw(_("Sanctioned Cost cannot be negative."))
        if flt(self.expenditure_to_date) > flt(self.sanctioned_cost) and flt(self.sanctioned_cost) > 0:
            frappe.msgprint(_("Warning: Expenditure to Date exceeds Sanctioned Cost."), alert=True)
