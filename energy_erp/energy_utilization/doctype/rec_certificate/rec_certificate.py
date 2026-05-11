import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt, getdate, today


class RecCertificate(Document):

    def validate(self):
        if flt(self.quantity_mwh) <= 0:
            frappe.throw(_("Quantity must be greater than zero."))
        if self.expiry_date and getdate(self.expiry_date) < getdate(today()):
            if self.status not in ("Expired", "Redeemed", "Sold"):
                frappe.msgprint(_("Warning: REC expiry date is in the past. Consider updating status to Expired."), alert=True)
