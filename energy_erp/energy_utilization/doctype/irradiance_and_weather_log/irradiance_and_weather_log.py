import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class IrradianceAndWeatherLog(Document):

    def validate(self):
        self.calculate_performance_ratio()

    def calculate_performance_ratio(self):
        actual = flt(self.actual_generation_kwh)
        theoretical = flt(self.theoretical_generation_kwh)
        if theoretical > 0:
            self.performance_ratio_percent = (actual / theoretical) * 100
        else:
            self.performance_ratio_percent = 0
        if flt(self.ghi_kwh_m2) < 0:
            frappe.throw(_("GHI cannot be negative."))
