import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class EnergyBill(Document):

    def validate(self):
        self.calculate_gst()
        self.calculate_totals()

    def calculate_gst(self):
        for row in self.gst_details or []:
            taxable = flt(row.taxable_amount)
            rate = flt(row.gst_rate_percent)
            total_gst = taxable * rate / 100
            row.cgst_amount = total_gst / 2
            row.sgst_amount = total_gst / 2
            row.igst_amount = flt(row.igst_amount)
            row.total_gst_amount = flt(row.cgst_amount) + flt(row.sgst_amount) + flt(row.igst_amount)

    def calculate_totals(self):
        subtotal = (
            flt(self.fixed_charge_amount)
            + flt(self.variable_charge_amount)
            + flt(self.ui_charge_amount)
            + flt(self.incentive_amount)
            - flt(self.penalty_amount)
        )
        self.subtotal_amount = subtotal

        total_gst = sum(flt(r.total_gst_amount) for r in self.gst_details or [])
        self.total_gst_amount = total_gst
        self.total_amount = subtotal + total_gst
