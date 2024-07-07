from fastapi import FastAPI, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse
from multiplataform_development_i.config.log_config import setup_logging
from multiplataform_development_i.controller.usuario_controller import user_router

logger = setup_logging()
logger.info('Iniciando a aplicação')

app = FastAPI(
    title="API de Tarefas",
    description="API para gerenciamento de tarefas",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url=None,
    redoc_url=None
)

app.include_router(user_router)


@app.exception_handler(Exception)
async def general_exception_handler(request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Um erro inesperado ocorreu no servidor"}
    )


@app.exception_handler(HTTPException)
async def general_exception_handler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )


@app.get('/', tags=['Redirect'], include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url='/docs')


@app.get('/docs', tags=['Redirect'], include_in_schema=False)
async def get_openapi():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="OpenApi UI"
    )


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='localhost', port=8000)