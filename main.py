from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException
from models import User, Gender, Role


app = FastAPI()


db: List[User] = [
    User(id=UUID("5e31e462-6605-446a-af8a-4b8b980d21cf"),
         first_name='Serhey',
         last_name='Shtepa',
         gender=Gender.male,
         roles=[Role.student]
         ),
    User(id=UUID("ea312e26-39be-4d35-9edb-883c2e8be331"),
         first_name='ALina',
         last_name='Shtepa',
         gender=Gender.female,
         roles=[Role.user, Role.admin]
         )
]


@app.get("/")
async def root():
    return {"message": "Hello Serhey"}


@app.get('/api/v1/users')
async def fetch_users():
    return db


@app.post('/api/v1/users')
async def register_user(user: User):
    db.append(user)
    return {'id': user.id}


@app.delete('/api/v1/users/{user_id}')
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f'user with id: {user_id} does not exists'
    )

