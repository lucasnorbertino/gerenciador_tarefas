from fastapi import HTTPException
from pydantic import TypeAdapter
from sqlalchemy.exc import IntegrityError

from multiplataform_development_i.domain.dto.dtos import TarefaCreateDTO, TarefaDTO, TarefaUpdateDTO
from multiplataform_development_i.domain.model.models import Tarefa
from multiplataform_development_i.repository.usuario_repository import TarefaRepository


class TarefaService:

    def __init__(self, usuario_repository: TarefaRepository):
        self.usuario_repository = usuario_repository

    def create(self, user_data: TarefaCreateDTO) -> TarefaDTO:
        user = Tarefa(**user_data.model_dump())
        try:
            created = self.usuario_repository.save(user)
            return TypeAdapter(TarefaDTO).validate_python(created)
        except IntegrityError as e:
            print(f'Erro ao criar a tarefa: {user_data.model_dump()}. Erro: {str(e)}')
            raise HTTPException(status_code=409, detail=f'Tarefa já existe na base: {e.args[0]}')

    def read(self, user_id: int) -> TarefaDTO:
        return TypeAdapter(TarefaDTO).validate_python(self._read(user_id))

    def _read(self, user_id: int) -> Tarefa:
        user = self.usuario_repository.read(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail=f'Tarefa {user_id} não encontrada.')
        return user

    def find_all(self) -> list[TarefaDTO]:
        users = self.usuario_repository.find_all()
        return [TypeAdapter(TarefaDTO).validate_python(user) for user in users]

    def update(self, user_id: int, user_data: TarefaUpdateDTO):
        user = self._read(user_id)
        user_data = user_data.model_dump(exclude_unset=True)
        for key, value in user_data.items():
            setattr(user, key, value)
        user_updated = self.usuario_repository.save(user)
        return TypeAdapter(TarefaDTO).validate_python(user_updated)

    def delete(self, user_id: int) -> int:
        user = self._read(user_id)
        self.usuario_repository.delete(user)
        return user_id