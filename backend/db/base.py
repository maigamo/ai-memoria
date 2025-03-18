# Import all the models, so that Base has them before being
# imported by Alembic
from db.base_class import Base  # noqa
from db.models.content import Content  # noqa
from db.models.file import File  # noqa
from db.models.user import User  # noqa 