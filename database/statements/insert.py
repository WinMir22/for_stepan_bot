from sqlalchemy.ext.asyncio import AsyncSession

from database.models import UsersTable


async def add_user(check: bool, user_id: int, full_name: str, username: str, session: AsyncSession):
    if check:
        add_user_statement = UsersTable(
            user_id=user_id,
            full_name=full_name,
            username=username
        )
        async with session:
            session.add(add_user_statement)
            return
    return