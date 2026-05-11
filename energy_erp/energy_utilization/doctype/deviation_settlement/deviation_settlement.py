import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class DeviationSettlement(Document):

    def validate(self):
        self.calculate_deviation()

    def calculate_deviation(self):
        scheduled = flt(self.scheduled_mu)
        actual = flt(self.actual_mu)
        self.deviation_mu = actual - scheduled

        # Net payable = |deviation_mu| * 1000000 kWh * dsm_rate Rs/kWh
        deviation_kwh = abs(flt(self.deviation_mu)) * 1000000
        self.net_payable = deviation_kwh * flt(self.dsm_rate)

        if flt(self.deviation_mu) < 0:
            self.payable_receivable = "Payable"
        elif flt(self.deviation_mu) > 0:
            self.payable_receivable = "Receivable"
        else:
            self.payable_receivable = "Nil"
