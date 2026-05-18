# Standard Operating Procedure (SOP): Energy Utilization ERP

## Overview
This document serves as a comprehensive, end-to-end guide for utilizing the Energy Utilization ERP from a customer/end-user perspective. This system is designed for thermal and renewable power generation, grid distribution, plant asset management, fuel supply chain, regulatory reporting, and real-time generation monitoring.

## 1. System Setup and Master Data Configuration
Before beginning regular operations, the initial structural and master data must be recorded in the system.

### 1.1 Infrastructure Setup
- **Power Plant & Generating Unit**: Register your facilities under the `Power Plant` module. Define individual units (turbines, boilers, solar arrays) within each plant using the `Generating Unit` module.
- **Grid Configuration**: Map your power distribution network by configuring `Substation`, `Voltage Level`, and `Feeder` records.
- **Asset Registry**: Record all physical equipment, including non-generating assets, using `Plant Asset` and `Renewable Asset` forms. This ensures traceability for maintenance.

### 1.2 Commercial Agreements
- **Power Purchase Agreements (PPA)**: Enter the details of off-take agreements, including buyer details, agreed capacity, and tariff rates under `Power Purchase Agreement`.
- **Fuel Supply Agreements (FSA)**: For thermal plants, define vendor contracts, expected coal/fuel grades, and supply quantities in `Fuel Supply Agreement`.

---

## 2. Day-to-Day Operations

### 2.1 Fuel Management (Thermal Plants)
- **Receipt & Inspection**: As fuel shipments arrive, log them using `Fuel Receipt`. Samples should be sent for testing, and the results recorded in `Fuel Quality Test`.
- **Inventory Management**: Update stock levels through `Fuel Stock Entry`.
- **Consumption Tracking**: Operators must log daily fuel usage in the `Fuel Consumption Log`, linking it back to the respective Generating Unit.

### 2.2 Power Generation & Monitoring
- **Generation Log**: Shift engineers must record gross and net power generation periodically in the `Generation Log`.
- **Weather & Irradiance**: For solar/wind plants, record real-time environmental data in `Irradiance and Weather Log` to correlate with power output.
- **Energy Meter Reading**: Periodically record exact export/import figures from grid boundary meters in `Energy Meter Reading`.

### 2.3 Scheduling and Dispatch
- **Energy Scheduling Order**: Based on grid demand and PPA obligations, plant managers receive and record schedules via `Energy Scheduling Order` to dictate unit loads for upcoming time blocks.

---

## 3. Maintenance and Asset Management

### 3.1 Planned Maintenance
- **Annual Overhaul Plan**: Long-term capital maintenance should be planned and budgeted using the `Annual Overhaul Plan`.
- **Asset Inspection**: Routine checks are recorded under `Asset Inspection Report`. Any detected anomalies should trigger a work order.
- **Maintenance Work Order**: Manage ongoing repairs, allocate `Spare Parts Inventory`, and track labor hours through work orders.

### 3.2 Unplanned Outages & Faults
- **Outage Reporting**: When a generating unit trips or is forced offline, log the event immediately in `Outage Report` detailing the cause, duration, and generation loss.
- **Grid Faults**: Transmission-side issues must be tracked using `Grid Fault Report`.

---

## 4. Billing, Settlement, and Commercials

### 4.1 Invoicing
- **Energy Bill**: At the end of the billing cycle, generate an `Energy Bill` based on the Meter Readings, Generation Logs, and applicable PPA Tariffs.
- **Deviation Settlement**: If actual generation deviated from the Scheduled Order, compute UI (Unscheduled Interchange) charges or penalties using the `Deviation Settlement` form.

### 4.2 Loss Accounting
- **AT&C Loss Report**: Distribution companies must track Aggregate Technical and Commercial losses to identify inefficiencies or theft across Feeders.

---

## 5. Regulatory Compliance and Reporting

### 5.1 CERC / SERC Compliance
- **Tariff Orders**: Record state/central regulatory tariff mandates in the `Tariff Order` module. Updates here will automatically affect billing logic.
- **BEE Energy Audit**: Log statutory energy audits (conducted by the Bureau of Energy Efficiency) under `BEE Energy Audit` to ensure specific energy consumption targets are met.
- **Environmental Compliance**: Record emissions (SOx, NOx, SPM), water usage, and ash disposal metrics via the `Environmental Compliance Report`.

### 5.2 Renewable Obligations
- **RPO Compliance Record**: Discoms or captive consumers must track their Renewable Purchase Obligations here.
- **REC Certificate**: Manage the earning, trading, and redeeming of Renewable Energy Certificates.

---

## Conclusion
By following these procedures, operators, managers, and stakeholders can ensure streamlined plant operations, accurate billing, strict regulatory compliance, and maximized asset lifespans. For any technical support or unhandled edge cases, please refer to the internal Helpdesk.
