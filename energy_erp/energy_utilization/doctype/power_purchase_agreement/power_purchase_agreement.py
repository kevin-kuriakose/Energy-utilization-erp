import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt, getdate


class PowerPurchaseAgreement(Document):

    def validate(self):
        self.validate_dates()
        self.validate_capacity()

    def validate_dates(self):
        if self.ppa_start_date and self.ppa_end_date:
            if getdate(self.ppa_end_date) <= getdate(self.ppa_start_date):
                frappe.throw(_("PPA End Date must be after PPA Start Date."))

    def validate_capacity(self):
        if flt(self.contracted_capacity_mw) <= 0:
            frappe.throw(_("Contracted Capacity must be greater than zero."))
