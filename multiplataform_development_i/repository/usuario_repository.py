from sqlalchemy.orm import Session

from multiplataform_development_i.domain.model.models import Tarefa


class TarefaRepository:

    def __init__(self, session: Session):
        self.session = session

    def save(self, user: Tarefa):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def delete(self, user: Tarefa):
        self.session.delete(user)
        self.session.commit()

    def read(self, user_id: int):
        return self.session.query(Tarefa).filter(Tarefa.id == user_id).first()

    def find_all(self):
        return self.session.query(Tarefa).all()