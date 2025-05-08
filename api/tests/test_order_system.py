from fastapi.testclient import TestClient
from fastapi import HTTPException, status, Response
from ..controllers import orders as ordercontroller
from ..controllers import order_details as detailscontroller
from ..main import app
import pytest
from ..models import orders as ordermodel
from ..models import order_details as detailsmodel

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_order_and_order_detail(db_session):
    # Create a sample order
    order_data = {
        "customer_name": "John Doe",
        "order_number": "434",
        "total_price": 12.35
    }

    order_object = ordermodel.Order(**order_data)

    # Call the create function
    created_order = ordercontroller.create(db_session, order_object)

    # Assertions for create function
    assert created_order is not None
    assert created_order.customer_name == "John Doe"
    assert created_order.order_number == "434"
    assert created_order.total_price == 12.35

    # Call read_one function
    read_order = ordercontroller.read_one(db_session, 0)

    # Assertions for read_one function
    assert read_order is not None
    assert created_order.customer_name == "John Doe"
    assert created_order.order_number == "434"
    assert created_order.total_price == 12.35

    # Create sample order detail
    order_detail_data = {
        "amount": 3,
        "special_requests": "peanut allergy",
        "is_delivery": True
    }

    order_detail_object = detailsmodel.OrderDetail(**order_detail_data)

    # Call create function
    created_order_detail = detailscontroller.create(db_session, order_detail_object)

    # Assertions for create function
    assert created_order_detail is not None
    assert created_order_detail.amount == 3
    assert created_order_detail.special_requests == "peanut allergy"
    assert created_order_detail.is_delivery == True

    # Call delete function for order detail
    detailscontroller.delete(db_session, 0)

    # Assertion for delete function [checks that created_order's
    # order_details attribute is empty, signifying the created_order_detail
    # object was deleted]
    assert created_order.order_details == []
