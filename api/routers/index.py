from . import orders, order_details, order_mgmt, deliveries, customers, payment_information


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(order_mgmt.router)
    app.include_router(deliveries.router)
    app.include_router(customers.router)
    app.include_router(payment_information.router)
