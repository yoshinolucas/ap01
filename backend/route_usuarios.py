from fastapi import  APIRouter, FastAPI, Depends, HTTPException, status, Response

from  database import engine,SessionLocal, Base
from schema import UsuariosSchema
from sqlalchemy.orm import Session
from models import Usuarios

#cria a tabela
Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/usuarios")   

def get_db():
    try:
        db = SessionLocal()
        #TODO 
        yield db
    finally:
        db.close()




@router.post("/add")
async def add_usuarios(request:UsuariosSchema, db: Session = Depends(get_db)):
    usuarios_on_db = usuarios(id=request.id, item=request.item, peso=request.peso, numero_caixas=request.numero_caixas)
    db.add(usuarios_on_db)
    db.commit()
    db.refresh(usuarios_on_db)
    return usuarios_on_db

@router.get("/{usuarios_name}", description="Listar o usuarios pelo nome")
def get_usuarios(usuarios_name,db: Session = Depends(get_db)):
    usuarios_on_db= db.query(usuarios).filter(usuarios.item == usuarios_name).first()
    return usuarios_on_db

@router.get("/usuarios/listar")
async def get_tarefas(db: Session = Depends(get_db)):
    usuarios= db.query(usuarios).all()
    return usuarios


@router.delete("/{id}", description="Deletar o usuarios pelo id")
def delete_usuarios(id: int, db: Session = Depends(get_db)):
    usuarios_on_db = db.query(usuarios).filter(usuarios.id == id).first()
    if usuarios_on_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sem usuarios com este id')
    db.delete(usuarios_on_db)
    db.commit()
    return f"Banco with id {id} deletado.", Response(status_code=status.HTTP_200_OK)

# @app.put("/usuarios/{id}",response_model=usuarios)
# async def update_usuarios(request:UsuariosSchema, id: int, db: Session = Depends(get_db)):
#     usuarios_on_db = db.query(usuarios).filter(usuarios.id == id).first()
#     print(usuarios_on_db)
#     if usuarios_on_db is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sem usuarios com este id')
#     usuarios_on_db = usuarios(id=request.id, item=request.item, peso=request.peso, numero_caixas=request.numero_caixas)
#     db.up
#     db.(usuarios_on_db)
#     db.commit()
#     db.refresh(usuarios_on_db)
#     return usuarios_on_db, Response(status_code=status.HTTP_204_NO_CONTENT)


# router = APIRouter()
