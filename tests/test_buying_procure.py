import unittest
from buying_procure.engine import ERPNextBuyingProcureEngine, SupplierQuoteItem, PurchaseOrderLine, LandedCostAllocation

class TestBuyingEngine(unittest.TestCase):
    def test_rfq_comparison(self):
        engine = ERPNextBuyingProcureEngine()
        quotes = [
            SupplierQuoteItem("SUP-01", "Fast Traders", "SKU-VALVE", 500.0, 18.0, lead_time_days=10),
            SupplierQuoteItem("SUP-02", "Economy Goods", "SKU-VALVE", 420.0, 18.0, lead_time_days=12)
        ]
        winner = engine.compare_supplier_quotations(quotes)
        self.assertEqual(winner.supplier_id, "SUP-02")

    def test_landed_cost_valuation(self):
        engine = ERPNextBuyingProcureEngine()
        lines = [
            PurchaseOrderLine("ITEM-A", 10.0, 100.0, 18.0), # ₹1000 base
            PurchaseOrderLine("ITEM-B", 20.0, 200.0, 18.0)  # ₹4000 base -> Total = ₹5000
        ]
        landed = LandedCostAllocation(freight_charges=500.0, customs_import_duty=500.0, handling_fees=0.0) # ₹1000 extra (20% on base)
        val = engine.compute_landed_item_valuation(lines, landed)
        self.assertEqual(val["ITEM-A"], 120.0) # 100 + 20% = 120
        self.assertEqual(val["ITEM-B"], 240.0) # 200 + 20% = 240

if __name__ == "__main__":
    unittest.main()
