import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class Substation(Document):

    def validate(self):
        if flt(self.transformer_capacity_mva) < 0:
            frappe.throw(_("Transformer Capacity cannot be negative."))
