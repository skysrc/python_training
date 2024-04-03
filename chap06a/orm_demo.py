from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///demo.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
sess = Session()

# this represent user table
class User(Base):
    __tablename__ = 'users' #optional if table and class name matched
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String[50])
    email = Column(String[50])

# automatically create tables base on the prev class
Base.metadata.create_all(engine)

# insert data into users table
new_user = User(name='John Doe', email='john@gmail.com')
sess.add(new_user)
sess.commit()