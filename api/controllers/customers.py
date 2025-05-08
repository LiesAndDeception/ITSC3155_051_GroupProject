from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import customers as model
from sqlalchemy.exc import SQLAlchemyError



def create(db: Session, request):
    new_customer = model.Customer(
        name=request.name,
        email=request.email,
        phone=request.phone,
        address=request.address
    )
    try:
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))
        print(f"Database error: {error}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    except Exception as e:
        db.rollback()
        print(f"Unhandled exception: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    return new_customer




def read_all(db: Session):
    try:
        customers = db.query(model.Customer).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return customers



def read_one(db: Session, customer_id: int):
    customer = db.query(model.Customer).filter(model.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return customer


def update(db: Session, customer_id: int, request):
    customer = db.query(model.Customer).filter(model.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    update_data = request.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(customer, key, value)
    db.commit()
    db.refresh(customer)
    return customer

def delete(db: Session, customer_id: int):
    customer = db.query(model.Customer).filter(model.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    db.delete(customer)
    db.commit()
    return {"detail": "Customer deleted successfully"}
