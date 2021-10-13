from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://template:123_Temp@localhost/api_template')
Session = sessionmaker(bind = engine)
session = Session()


