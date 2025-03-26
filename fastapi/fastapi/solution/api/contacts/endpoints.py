from fastapi import APIRouter, Response, Form
from api.contacts.contacts import add_contact, find_contact, all_contacts, update_contact, delete_contact

router = APIRouter(tags=["Contact"])

@router.get("/")
async def find_contact(id: str|None = None):
    # pokud metoda dostane id:
    if id is not None:
        try:
            return find_contact(id)
        except ValueError as e:
            return Response(status_code=404, content="Contact with given id was not found")
    
    else:
        return all_contacts()

@router.post("/")
async def create_contact(name: str = Form(...), discord: str = Form(...)):
    return Response(status_code=200, content=add_contact(name, discord))

@router.put("/")
async def put_contact(id: str = Form(...), name: str|None = Form(None), discord: str|None = Form(None)):
    try:
        return update_contact(id, name, discord)
    except ValueError as e:
        return Response(status_code=404, content="Contact with given id not found")

@router.delete("/")
async def delete(id: str = Form(...)):
    try:
        delete_contact(id)
        return Response(status_code=204)
    except ValueError as e:
        return Response(status_code=404, content="Contact with given id not found")