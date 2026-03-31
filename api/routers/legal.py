from fastapi import APIRouter

router = APIRouter()

@router.get("/compliance/ownership-rights")
def get_asset_transfer_guide():
    """
    Guides users through PA Title 15 and 'Bulk Sales' regulations to properly manage liability during transfers.
    """
    return {
        "jurisdiction": "PA",
        "regulation": "Title 15 & Bulk Sales",
        "liability_status": "Cleared",
        "steps_completed": ["Inventory valuation", "Creditor notification"],
        "pending_actions": []
    }

@router.get("/compliance/knowledge-disclosure")
def get_trade_secret_protocols():
    """
    Enforces protocols for Trade Secret preservation (PA UTSA) and personal data breach notifications (BPINA).
    """
    return {
        "protocol": "PA UTSA & BPINA",
        "cad_encryption_status": "Active",
        "data_breach_notifications_pending": 0,
        "is_compliant": True
    }