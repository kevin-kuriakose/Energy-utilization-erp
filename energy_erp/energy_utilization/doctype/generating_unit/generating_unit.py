import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class GeneratingUnit(Document):

    def validate(self):
        if flt(self.rated_capacity_mw) <= 0:
            frappe.throw(_("Rated Capacity must be greater than zero."))
        if flt(self.design_auxiliary_consumption) < 0 or flt(self.design_auxiliary_consumption) > 100:
            frappe.throw(_("Design Auxiliary Consumption must be between 0 and 100."))
