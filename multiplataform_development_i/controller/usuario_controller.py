from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from multiplataform_development_i.config.database import get_db
from multiplataform_development_i.domain.dto.dtos import TarefaDTO, TarefaCreateDTO, TarefaUpdateDTO
from multiplataform_development_i.repository.usuario_repository import TarefaRepository
from multiplataform_development_i.service.usuario_service import TarefaService

user_router = APIRouter(prefix='/users', tags=['Users'])

def get_user_repo(session: Session = Depends(get_db)):
    return TarefaRepository(session=session)


@user_router.post('/', status_code=201, description='Cria uma nova tarefa', response_model=TarefaDTO)
async def create(request: TarefaCreateDTO, user_repo: TarefaRepository = Depends(get_user_repo)):
    usuario_service = TarefaService(user_repo)
    return usuario_service.create(request)


@user_router.get('/{user_id}', status_code=200, description='Buscar tarefa por ID', response_model=TarefaDTO)
async def find_by_id(user_id: int, user_repo: TarefaRepository = Depends(get_user_repo)):
    usuario_service = TarefaService(user_repo)
    return usuario_service.read(user_id=user_id)


@user_router.get('/', status_code=200, description='Buscar todas as tarefas', response_model=list[TarefaDTO])
async def find_all(user_repo: TarefaRepository = Depends(get_user_repo)):
    usuario_service = TarefaService(user_repo)
    return usuario_service.find_all()


@user_router.put('/{user_id}', status_code=200, description='Atualizar uma tarefa', response_model=TarefaDTO)
async def find_by_id(user_id: int, user_data: TarefaUpdateDTO, user_repo: TarefaRepository = Depends(get_user_repo)):
    usuario_service = TarefaService(user_repo)
    return usuario_service.update(user_id, user_data)


@user_router.delete('/{user_id}', status_code=204, description='Deletar uma tarefa')
async def find_by_id(user_id: int, user_repo: TarefaRepository = Depends(get_user_repo)):
    usuario_service = TarefaService(user_repo)
    usuario_service.delete(user_id=user_id)