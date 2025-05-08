from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..controllers import payment_information as payment_controller
from ..schemas.payment_information import PaymentInformationCreate, PaymentInformation

router = APIRouter(
    prefix="/payments",
    tags=["payments"]
)

@router.get("/", response_model=list[PaymentInformation])
def get_all_payments(db: Session = Depends(get_db)):
    return payment_controller.get_all_payments(db)

@router.post("/", response_model=PaymentInformation)
def create_payment(payment: PaymentInformationCreate, db: Session = Depends(get_db)):
    return payment_controller.create_payment(db, payment)
