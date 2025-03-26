from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from api.generator.endpoints import router as gen_router
from api.contacts.endpoints import router as c_router

app = FastAPI()

@app.get("/")
async def root() -> HTMLResponse:
    html = """
    <body>
        <h1>Naše nová API</h1>
        <div>Toto je API, která umí generovat a pracovat s kontakty.</div>
    </body>
    """
    return HTMLResponse(content=html)


app.include_router(gen_router, prefix="/generator", tags=["Generator"])
app.include_router(c_router, prefix="/contact", tags=["Contact"])