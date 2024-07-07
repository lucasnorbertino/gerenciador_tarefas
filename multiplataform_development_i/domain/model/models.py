from datetime import datetime
from sqlalchemy import Column, Integer, String

from multiplataform_development_i.config.database import Base, engine


class Tarefa(Base):
    __tablename__ = 'tarefas'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(50))
    description = Column(String(50))
    status = Column(String(50))
    created_at = Column(String(10))

    def __repr__(self):
        return f'<User(id={self.id}, titulo={self.titulo}, description={self.description}, status={self.status}, created_at={self.created_at})>'

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)