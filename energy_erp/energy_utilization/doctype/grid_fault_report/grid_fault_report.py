import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt, get_datetime, time_diff_in_seconds


class GridFaultReport(Document):

    def validate(self):
        self.calculate_outage_duration()

    def calculate_outage_duration(self):
        if self.fault_datetime and self.restoration_datetime:
            start = get_datetime(self.fault_datetime)
            end = get_datetime(self.restoration_datetime)
            if end <= start:
                frappe.throw(_("Restoration Date/Time must be after Fault Date/Time."))
            seconds = time_diff_in_seconds(end, start)
            self.outage_duration_minutes = flt(seconds) / 60
