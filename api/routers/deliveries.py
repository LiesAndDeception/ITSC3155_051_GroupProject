from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import deliveries as controller
from ..schemas import deliveries as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Deliveries'],
    prefix="/deliveries"
)


@router.post("/", response_model=schema.Delivery)
def create(request: schema.DeliveryCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Delivery])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.Delivery)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.Delivery)
def update(item_id: int, request: schema.DeliveryUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)


@router.put("_out_for_delivery/{item_id}", response_model=schema.Delivery)
def update_in_progress(item_id: int, request: schema.DeliveryStatusOutForDelivery, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.put("_delivered/{item_id}", response_model=schema.Delivery)
def update_completed(item_id: int, request: schema.DeliveryStatusDelivered, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)