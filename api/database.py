from sqlmodel import create_engine, SQLModel, Session
from contextlib import contextmanager
import api.config as config

engine = create_engine(config.DB_CONNECTION_STRING)

def create_tables():
    SQLModel.metadata.create_all(engine)

# only for use in `session = Depends(get_session)`
def get_session():
    with Session(engine) as session:
        yield session

# only for use in `with session_scope() as session:`
@contextmanager
def session_scope():
    with Session(engine) as session:
        yield session