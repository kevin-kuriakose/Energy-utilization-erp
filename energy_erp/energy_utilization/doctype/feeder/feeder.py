import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class Feeder(Document):

    def validate(self):
        if flt(self.connected_load_mw) < 0:
            frappe.throw(_("Connected Load cannot be negative."))
