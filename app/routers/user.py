from fastapi import APIRouter

router = APIRouter(prefix='/user', tags=['user'])

@router.get('/all_users')
async def all_users():
    pass

@router.post('/create')
async def create_user():
    pass

@router.get('/user_id')
async def uset_by_id():
    pass



@router.put('/update')
async def update_user():
    pass

@router.delete('/delete')
async def delete_user():
    pass
