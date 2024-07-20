import sqlalchemy.ext.declarative as dec
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

SqlAlchemyBase = dec.declarative_base()

__factory = None


def global_init(db_file):
    global __factory

    if __factory:
        return

    conn_str = f'sqlite:///{db_file}'
    print(f'Подключаемся к базе данных по адресу:{conn_str}?check_same_thread=False')

    engine = create_engine(conn_str)
    __factory = sessionmaker(bind=engine)

    from . import __all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()