import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class FuelConsumptionLog(Document):

    def validate(self):
        self.calculate_derived_fields()

    def calculate_derived_fields(self):
        qty = flt(self.quantity_mt)
        gcv = flt(self.gcv_kcal_kg)

        if qty < 0:
            frappe.throw(_("Quantity cannot be negative."))
        if gcv < 0:
            frappe.throw(_("GCV cannot be negative."))

        # Heat input in Mkcal: qty (MT) * gcv (kcal/kg) * 1000 kg/MT / 1,000,000
        if qty > 0 and gcv > 0:
            self.heat_input_mkcal = (qty * gcv * 1000) / 1000000
        else:
            self.heat_input_mkcal = 0

        # SFC: quantity in kg / generation in kWh
        # Pull net generation from linked Generation Log if available
        if self.generation_log:
            net_gen_mu = flt(frappe.db.get_value('Generation Log', self.generation_log, 'net_generation_mu'))
            if net_gen_mu > 0:
                # net_gen_mu * 1000000 = kWh; qty_mt * 1000 = kg
                self.sfc_kg_kwh = (qty * 1000) / (net_gen_mu * 1000000)
            else:
                self.sfc_kg_kwh = 0
        else:
            self.sfc_kg_kwh = 0
