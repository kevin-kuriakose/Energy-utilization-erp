import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import getdate, today


class AssetInspectionReport(Document):

    def validate(self):
        if self.next_inspection_date:
            if getdate(self.next_inspection_date) <= getdate(self.inspection_date):
                frappe.throw(_("Next Inspection Date must be after Inspection Date."))
