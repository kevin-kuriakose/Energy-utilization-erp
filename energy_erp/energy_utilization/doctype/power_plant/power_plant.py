import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class PowerPlant(Document):

    def validate(self):
        self.validate_capacity()

    def validate_capacity(self):
        if flt(self.installed_capacity_mw) <= 0:
            frappe.throw(_("Installed Capacity must be greater than zero."))
