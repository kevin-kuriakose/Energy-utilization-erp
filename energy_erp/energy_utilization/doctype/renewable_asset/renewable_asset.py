import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class RenewableAsset(Document):

    def validate(self):
        if flt(self.installed_capacity_mwp) < 0:
            frappe.throw(_("Installed Capacity cannot be negative."))
        if flt(self.cuf_target_percent) < 0 or flt(self.cuf_target_percent) > 100:
            frappe.throw(_("CUF Target must be between 0 and 100."))
