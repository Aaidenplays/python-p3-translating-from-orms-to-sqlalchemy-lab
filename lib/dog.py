from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ipdb
from models import Dog

engine = create_engine('sqlite:///:memory:')
# Session = sessionmaker(bind=engine)
# session = Session()

def create_table(base):
    base.metadata.create_all(engine)
    return engine
    

def save(session, dog):
    session.add(dog)
    session.commit()
    return session

def new_from_db(session, dog_from_db): #somn aint right here
    # ipdb.set_trace()
    return dog_from_db

def get_all(session):
    query = session.query(Dog)
    return query
    

def find_by_name(session, name):
    query = session.query(Dog).filter(Dog.name == name).first()
    return query
    

def find_by_id(session, id):
    query = session.query(Dog).filter(Dog.id == id).first()
    return query

def find_by_name_and_breed(session, name, breed):
    query = session.query(Dog).filter(Dog.name == name and Dog.breed == breed).first()
    return  query

def update_breed(session, dog, breed):
    query = session.query(Dog).filter(Dog.name == dog.name and Dog.breed == dog.breed).update({Dog.breed: breed})
    return query