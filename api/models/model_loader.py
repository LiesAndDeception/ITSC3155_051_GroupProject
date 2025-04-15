from . import orders, order_details, recipes, sandwiches, resources, payment_information, resource_management

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    payment_information.Base.metadata.create_all(engine)
    resource_management.Base.metadata.create_all(engine)