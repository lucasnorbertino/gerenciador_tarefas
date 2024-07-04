from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from starlette.responses import RedirectResponse

app = FastAPI(
    title="API de Usuários",
    description="APi para gerenciamento de usuários",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url=None,
    redoc_url=None,
    contact={
        "name": "Luan Fernandes",
        "email": "luan.santos26@fatec.sp.gov.br",
        "url": "https://luanfernandes.dev"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    },
    servers=[
        {
            "url": "http://localhost:8000",
            "description": "Development server"
        },
        {
            "url": "http://user.luanfernandes.dev",
            "description": "Production server"
        }
    ]
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