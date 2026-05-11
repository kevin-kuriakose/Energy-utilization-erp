import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt, getdate


class FuelSupplyAgreement(Document):

    def validate(self):
        if self.start_date and self.end_date:
            if getdate(self.end_date) <= getdate(self.start_date):
                frappe.throw(_("End Date must be after Start Date."))
        if flt(self.annual_quantity_mt) < 0:
            frappe.throw(_("Annual Quantity cannot be negative."))
