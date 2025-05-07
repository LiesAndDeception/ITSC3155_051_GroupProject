from . import orders, order_details, recipes, resources, drinks, payment_information, resource_management, menu_items, customers, deliveries

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    customers.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    drinks.Base.metadata.create_all(engine)
    payment_information.Base.metadata.create_all(engine)
    resource_management.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    deliveries.Base.metadata.create_all(engine)
