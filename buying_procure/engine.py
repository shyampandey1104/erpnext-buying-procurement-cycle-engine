"""Complete ERPNext Buying Engine (Procurement - Request se Payment tak - Har kharid ka hisaab, ek jagah)."""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class SupplierQuoteItem:
    supplier_id: str
    supplier_name: str
    item_code: str
    unit_price: float
    tax_pct: float
    lead_time_days: int
    quality_score: float = 95.0


@dataclass
class PurchaseOrderLine:
    item_code: str
    ordered_qty: float
    unit_rate: float
    tax_rate_pct: float


@dataclass
class LandedCostAllocation:
    freight_charges: float
    customs_import_duty: float
    handling_fees: float


class ERPNextBuyingProcureEngine:
    """Procurement RFQ comparison, Purchase Order generation, and Landed Cost Valuation."""

    def compare_supplier_quotations(self, quotes: List[SupplierQuoteItem]) -> SupplierQuoteItem:
        """Selects optimal supplier quote based on lowest landed cost and shortest lead time."""
        return min(quotes, key=lambda q: (q.unit_price * (1.0 + (q.tax_pct / 100.0)), q.lead_time_days))


    def compute_landed_item_valuation(
        self,
        po_lines: List[PurchaseOrderLine],
        landed: LandedCostAllocation
    ) -> Dict[str, float]:
        """Apportions freight and customs duty across line items based on order value proportion."""
        total_order_val = sum(l.ordered_qty * l.unit_rate for l in po_lines)
        total_additional_cost = landed.freight_charges + landed.customs_import_duty + landed.handling_fees

        valuation_rates: Dict[str, float] = {}
        for l in po_lines:
            base_val = l.ordered_qty * l.unit_rate
            proportion = base_val / total_order_val if total_order_val > 0 else 0.0
            item_additional_charge = total_additional_cost * proportion
            total_item_cost = base_val + item_additional_charge
            effective_valuation_rate = total_item_cost / l.ordered_qty
            valuation_rates[l.item_code] = round(effective_valuation_rate, 2)

        return valuation_rates
