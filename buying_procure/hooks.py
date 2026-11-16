# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "buying_procure"
app_title = "Erpnext Buying Procurement Cycle Engine"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Buying Procurement Cycle Engine for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/buying_procure/css/buying_procure.bundle.css"
app_include_js = "/assets/buying_procure/js/buying_procure.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "buying_procure.engine.on_document_submit",
        "on_cancel": "buying_procure.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "buying_procure.engine.daily_scheduled_sync"
    ]
}
