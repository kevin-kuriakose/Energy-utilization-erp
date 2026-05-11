import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt, getdate


class TariffOrder(Document):

    def validate(self):
        self.validate_dates()
        self.validate_charges()

    def validate_dates(self):
        if self.effective_to and self.effective_from:
            if getdate(self.effective_to) < getdate(self.effective_from):
                frappe.throw(_("Effective To cannot be before Effective From."))

    def validate_charges(self):
        for field in ["fixed_charge_rs_kw", "variable_charge_rs_kwh", "fuel_surcharge_rs_kwh"]:
            if flt(getattr(self, field, 0)) < 0:
                frappe.throw(_(f"{field} cannot be negative."))
