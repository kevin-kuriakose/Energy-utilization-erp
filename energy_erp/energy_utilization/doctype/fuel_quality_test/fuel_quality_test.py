import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class FuelQualityTest(Document):

    def validate(self):
        for field in ["moisture_percent", "ash_percent", "sulphur_percent",
                      "volatile_matter_percent", "fixed_carbon_percent"]:
            val = flt(getattr(self, field, 0))
            if val < 0 or val > 100:
                frappe.throw(_(f"{field} must be between 0 and 100."))
