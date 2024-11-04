from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


# Usando DATETIME com timezone
def current_time():
    return func.DATETIME(func.CURRENT_TIMESTAMP(), 'localtime')


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        init=False,
        primary_key=True,
    )
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(
        init=False,
        server_default=current_time(),
    )
    # 'uptated_at' está com erro de digitação, deveria ser 'updated_at'
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=current_time(), onupdate=current_time()
    )
