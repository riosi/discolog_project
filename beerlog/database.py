import warnings

from sqlmodel import Session, create_engine

from beerlog import models
from beerlog.config import settings

from sqlalchemy.exc import SAWarning
from sqlmodel.sql.expression import Select, SelectOfScalar

warnings.filterwarnings("ignore", category=SAWarning)
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True


engine = create_engine(settings.database.url)

models.SQLModel.metadata.create_all(engine)  # create table do sql


# retorna o objeto Session já conectado ao banco de dados, não expõe a engine
def get_session():
    return Session(engine)
