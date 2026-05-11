import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class SparePartsInventory(Document):

    def validate(self):
        if flt(self.quantity_on_hand) < 0:
            frappe.throw(_("Quantity on Hand cannot be negative."))
        if flt(self.reorder_level) < 0:
            frappe.throw(_("Reorder Level cannot be negative."))
