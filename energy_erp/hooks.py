app_name = "energy_erp"
app_title = "Energy ERP"
app_publisher = "Your Company"
app_description = "Full-stack energy ERP for India covering thermal and renewable power generation, grid distribution, plant asset management, fuel supply chain, BEE energy audits, CERC regulatory reporting, outage management, and real-time generation monitoring across multiple plant sites."
app_email = "dev@yourcompany.com"
app_license = "MIT"
app_version = "0.0.1"

required_apps = ["frappe", "bizaxl_erp"]

app_include_css = "/assets/energy_erp/css/energy_erp.css"
app_include_js = "/assets/energy_erp/js/energy_erp.js"

doc_events = {}

scheduler_events = {
    "daily": [],
    "weekly": [],
}

    {"dt": "Custom Field", "filters": [["module", "=", "Energy Utilization"]]},
    {"dt": "Property Setter", "filters": [["module", "=", "Energy Utilization"]]},
]

override_doctype_class = {
    # Phase 1 — Master Doctypes
    "Power Plant": "energy_erp.energy_utilization.doctype.power_plant.power_plant.PowerPlant",
    "Substation": "energy_erp.energy_utilization.doctype.substation.substation.Substation",
    "Tariff Order": "energy_erp.energy_utilization.doctype.tariff_order.tariff_order.TariffOrder",
    "Renewable Asset": "energy_erp.energy_utilization.doctype.renewable_asset.renewable_asset.RenewableAsset",
    "Plant Asset": "energy_erp.energy_utilization.doctype.plant_asset.plant_asset.PlantAsset",
    "Spare Parts Inventory": "energy_erp.energy_utilization.doctype.spare_parts_inventory.spare_parts_inventory.SparePartsInventory",
    "Fuel Grade": "energy_erp.energy_utilization.doctype.fuel_grade.fuel_grade.FuelGrade",
    "Voltage Level": "energy_erp.energy_utilization.doctype.voltage_level.voltage_level.VoltageLevel",
    "Regulatory Body": "energy_erp.energy_utilization.doctype.regulatory_body.regulatory_body.RegulatoryBody",
    "RPO Category": "energy_erp.energy_utilization.doctype.rpo_category.rpo_category.RpoCategory",
    # Phase 2 — Core Transactional Doctypes
    "Generating Unit": "energy_erp.energy_utilization.doctype.generating_unit.generating_unit.GeneratingUnit",
    "Power Purchase Agreement": "energy_erp.energy_utilization.doctype.power_purchase_agreement.power_purchase_agreement.PowerPurchaseAgreement",
    "Feeder": "energy_erp.energy_utilization.doctype.feeder.feeder.Feeder",
    "Fuel Supply Agreement": "energy_erp.energy_utilization.doctype.fuel_supply_agreement.fuel_supply_agreement.FuelSupplyAgreement",
    "Energy Scheduling Order": "energy_erp.energy_utilization.doctype.energy_scheduling_order.energy_scheduling_order.EnergySchedulingOrder",
    "Unit Schedule Row": "energy_erp.energy_utilization.doctype.unit_schedule_row.unit_schedule_row.UnitScheduleRow",
    "Maintenance Work Order": "energy_erp.energy_utilization.doctype.maintenance_work_order.maintenance_work_order.MaintenanceWorkOrder",
    "Part Line": "energy_erp.energy_utilization.doctype.part_line.part_line.PartLine",
    "Annual Overhaul Plan": "energy_erp.energy_utilization.doctype.annual_overhaul_plan.annual_overhaul_plan.AnnualOverhaulPlan",
    "Asset Inspection Report": "energy_erp.energy_utilization.doctype.asset_inspection_report.asset_inspection_report.AssetInspectionReport",
    # Phase 3 — Operational Logging Doctypes
    "Generation Log": "energy_erp.energy_utilization.doctype.generation_log.generation_log.GenerationLog",
    "Outage Report": "energy_erp.energy_utilization.doctype.outage_report.outage_report.OutageReport",
    "Fuel Receipt": "energy_erp.energy_utilization.doctype.fuel_receipt.fuel_receipt.FuelReceipt",
    "Fuel Quality Test": "energy_erp.energy_utilization.doctype.fuel_quality_test.fuel_quality_test.FuelQualityTest",
    "Fuel Stock Entry": "energy_erp.energy_utilization.doctype.fuel_stock_entry.fuel_stock_entry.FuelStockEntry",
    "Fuel Consumption Log": "energy_erp.energy_utilization.doctype.fuel_consumption_log.fuel_consumption_log.FuelConsumptionLog",
    "Energy Meter Reading": "energy_erp.energy_utilization.doctype.energy_meter_reading.energy_meter_reading.EnergyMeterReading",
    "AT and C Loss Report": "energy_erp.energy_utilization.doctype.at_and_c_loss_report.at_and_c_loss_report.AtAndCLossReport",
    "Grid Fault Report": "energy_erp.energy_utilization.doctype.grid_fault_report.grid_fault_report.GridFaultReport",
    # Phase 4 — Renewable, Finance and Regulatory Doctypes
    "REC Certificate": "energy_erp.energy_utilization.doctype.rec_certificate.rec_certificate.RecCertificate",
    "RPO Compliance Record": "energy_erp.energy_utilization.doctype.rpo_compliance_record.rpo_compliance_record.RpoComplianceRecord",
    "Irradiance and Weather Log": "energy_erp.energy_utilization.doctype.irradiance_and_weather_log.irradiance_and_weather_log.IrradianceAndWeatherLog",
    "GST Row": "energy_erp.energy_utilization.doctype.gst_row.gst_row.GstRow",
    "Energy Bill": "energy_erp.energy_utilization.doctype.energy_bill.energy_bill.EnergyBill",
    "Deviation Settlement": "energy_erp.energy_utilization.doctype.deviation_settlement.deviation_settlement.DeviationSettlement",
    "BEE Energy Audit": "energy_erp.energy_utilization.doctype.bee_energy_audit.bee_energy_audit.BeeEnergyAudit",
    "Milestone Row": "energy_erp.energy_utilization.doctype.milestone_row.milestone_row.MilestoneRow",
    "Capital Project": "energy_erp.energy_utilization.doctype.capital_project.capital_project.CapitalProject",
    "Environmental Compliance Report": "energy_erp.energy_utilization.doctype.environmental_compliance_report.environmental_compliance_report.EnvironmentalComplianceReport",
}

after_install = "energy_erp.install.after_install"

fixtures = [
    {"doctype": "Workspace", "filters": [["name", "in", ["Energy Utilization"]]]},
    {"doctype": "Notification", "filters": [["document_type", "in", [
        "Energy Bill", "Generation Log", "Outage Report", "Fuel Stock Entry",
        "Power Purchase Agreement", "REC Certificate", "Environmental Compliance Report"
    ]]]},
]
