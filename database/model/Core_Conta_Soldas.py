from datetime import datetime
from sqlalchemy import (create_engine, MetaData, Column, 
                            Table, Integer, DateTime)


engine = create_engine("mysql+pymysql://root@localhost/tcc-db")

metadata = MetaData(bind=engine)

conta_soldas = Table('CONTA_SOLDAS', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('eletrodo', Integer, index=True),
                    Column('soldagens', Integer, nullable=False),
                    Column('atualizado_em', DateTime, default=datetime.now, onupdate=datetime.now)
                    )

# metadata.create_all()