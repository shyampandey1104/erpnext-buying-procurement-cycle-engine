# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "buying_procure"
app_title = "Erpnext Buying Procurement Cycle Engine"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Buying Procurement Cycle Engine - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/buying_procure/css/buying_procure.bundle.css"
app_include_js = "/assets/buying_procure/js/buying_procure.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext Buying Procurement Cycle Engine Entry": {
        "validate": "buying_procure.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "buying_procure.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "buying_procure.tasks.hourly_sync"
    ],
    "daily": [
        "buying_procure.tasks.daily_reconciliation"
    ],
    "weekly": [
        "buying_procure.tasks.weekly_digest"
    ]
}
