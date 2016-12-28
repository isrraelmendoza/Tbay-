from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
 
engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
 
from datetime import datetime
 
class Item(Base):
    __tablename__ = "items"
 
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    #relationship establishing one user can "own" many items
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    #relationship extablishing that one item can have many bi
    bids = relationship("Bid", backref="item")
     
class User(Base):
    __tablename__ = "users"
     
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    #one to many users to items
    items = relationship("Item", backref="user")
    #one to many users to bids
    bids = relationship("Bid", backref="user")
     
class Bid(Base):
    __tablename__ = "bids"
    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    #one to many users to bids
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
     
Base.metadata.create_all(engine)
 
jeff = User()
jeff.username = "jmsword"
jeff.password = "Alyeska9"
 
ryan = User()
ryan.username = "ryry"
ryan.password = "mustang"
 
tara = User()
tara.username = "tara"
tara.password = "kia"
 
baseball = Item(name = "baseball", description = "McGuires homerun ball", user=jeff)
 
bid1 = Bid(price = 10, user=ryan, item=baseball)
bid2 = Bid(price = 12, user=tara, item=baseball)
bid3 = Bid(price = 14, user=ryan, item=baseball)
bid4 = Bid(price = 16, user=tara, item=baseball)
 
session.add_all([jeff, ryan, tara, baseball, bid1, bid2, bid3, bid4])