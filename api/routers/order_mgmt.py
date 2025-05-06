from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas import orders as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Order Status Mgmt'],
    prefix="/order_status"
)


@router.put("_received/{item_id}", response_model=schema.Order)
def update_received(item_id: int, request: schema.OrderStatusReceived, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.put("_in_progress/{item_id}", response_model=schema.Order)
def update_in_progress(item_id: int, request: schema.OrderStatusInProgress, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.put("_completed/{item_id}", response_model=schema.Order)
def update_completed(item_id: int, request: schema.OrderStatusCompleted, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)
