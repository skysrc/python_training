from sqlmodel import SQLModel, Session, create_engine
from models.event import Event 

database_file='planner.dbo'
database_connection_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False} #this only for SQLite
engine_url = create_engine(database_connection_string, echo=True)

# all tables will be created here
def conn():
    SQLModel.metadata.create_all(engine_url)

# return session obj
# 'with' and 'yield' will auto closing connection resources
def get_session():
    with Session(engine_url) as session:
        yield session