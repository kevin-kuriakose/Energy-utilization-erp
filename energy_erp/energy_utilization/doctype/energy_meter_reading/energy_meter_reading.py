import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class EnergyMeterReading(Document):

    def validate(self):
        self.calculate_units_consumed()

    def calculate_units_consumed(self):
        current = flt(self.current_reading)
        previous = flt(self.previous_reading)
        factor = flt(self.multiplying_factor) or 1.0

        if current < previous:
            frappe.throw(_("Current Reading cannot be less than Previous Reading."))

        self.units_consumed = (current - previous) * factor
