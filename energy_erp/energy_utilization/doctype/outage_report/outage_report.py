import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt, get_datetime


class OutageReport(Document):

    def validate(self):
        self.validate_dates()
        if flt(self.lost_generation_mu) < 0:
            frappe.throw(_("Lost Generation cannot be negative."))

    def validate_dates(self):
        if self.outage_end and self.outage_start:
            if get_datetime(self.outage_end) <= get_datetime(self.outage_start):
                frappe.throw(_("Outage End must be after Outage Start."))
