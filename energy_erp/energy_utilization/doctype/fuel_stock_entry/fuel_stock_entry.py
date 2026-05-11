import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class FuelStockEntry(Document):

    def validate(self):
        self.calculate_closing_stock()

    def calculate_closing_stock(self):
        opening = flt(self.opening_stock_mt)
        receipts = flt(self.receipts_mt)
        consumption = flt(self.consumption_mt)

        if opening < 0:
            frappe.throw(_("Opening Stock cannot be negative."))
        if receipts < 0:
            frappe.throw(_("Receipts cannot be negative."))
        if consumption < 0:
            frappe.throw(_("Consumption cannot be negative."))

        closing = opening + receipts - consumption
        if closing < 0:
            frappe.throw(_("Closing Stock cannot be negative. Check consumption vs stock figures."))

        self.closing_stock_mt = closing

        # Days of stock = closing stock / daily consumption
        # Use 30-day average if consumption > 0
        if flt(consumption) > 0:
            self.days_of_stock = closing / (consumption / 30.0)
        else:
            self.days_of_stock = 0
