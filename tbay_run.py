from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from tbay import Item, Bid

def highest_bid(item_id):
    item = session.query(Item.name).filter(Item.id == item_id).first()
    high_bidder = session.query(Bid.bidder_id, Bid.price).\
        filter(Bid.item_id == item_id).\
        order_by(Bid.price.desc()).first()
    msg = "The '{0}' goes to {1} with the bid of {2}.".format(
        item[0], high_bidder[0], high_bidder[1])
    return msg