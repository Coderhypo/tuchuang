from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from app.config import get_config_obj

config_obj = get_config_obj()
print(config_obj.SQLALCHEMY_DATABASE_URI)
engine = create_engine(config_obj.SQLALCHEMY_DATABASE_URI, echo=True, max_overflow=5)
METADATA = MetaData(bind=engine)
model = declarative_base(bind=engine, metadata=METADATA)
Session = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))

