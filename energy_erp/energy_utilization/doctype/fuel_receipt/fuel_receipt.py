import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class FuelReceipt(Document):

    def validate(self):
        if flt(self.quantity_mt) <= 0:
            frappe.throw(_("Quantity must be greater than zero."))
        if flt(self.gcv_kcal_kg) < 0:
            frappe.throw(_("GCV cannot be negative."))
