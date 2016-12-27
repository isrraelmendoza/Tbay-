from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from tbay import User, Item, Bid

josh = User (username='josh')
chris = User (username='chris')
carlos = User (username='carlos')

session.add_all([josh, chris, carlos])
session.commit()

baseball = Item(name='baseball', owner=josh)

session.add_all([baseball])
session.commit()

bid1 = Bid(price=15.00, bidder=chris, auction_items=baseball)
bid2 = Bid(price=20.00, bidder=carlos)
bid3 = Bid(price=22.00, bidder=chris)
bid4 = Bid (price=25.00, bidder=carlos)

session.add_all([bid1, bid2, bid3, bid4])
session.commit()