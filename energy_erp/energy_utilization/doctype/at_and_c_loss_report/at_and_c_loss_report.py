import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class AtAndCLossReport(Document):

    def validate(self):
        self.calculate_atc_loss()

    def calculate_atc_loss(self):
        energy_input = flt(self.energy_input_mu)
        energy_collected = flt(self.energy_collected_mu)

        if energy_input <= 0:
            self.atc_loss_percent = 0
            self.loss_variance_percent = 0
            return

        # AT&C loss = 1 - (energy collected / energy input), expressed as %
        self.atc_loss_percent = (1 - (energy_collected / energy_input)) * 100
        self.loss_variance_percent = flt(self.atc_loss_percent) - flt(self.target_loss_percent)
