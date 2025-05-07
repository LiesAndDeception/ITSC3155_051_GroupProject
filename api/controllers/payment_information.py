from sqlalchemy.orm import Session
from ..models.payment_information import PaymentInformation
from ..schemas.payment_information import PaymentInformationCreate

def get_all_payments(db: Session):
    return db.query(PaymentInformation).all()

def create_payment(db: Session, payment: PaymentInformationCreate):
    db_payment = PaymentInformation(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment
