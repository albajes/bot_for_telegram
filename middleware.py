from typing import Any, Callable, Dict, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from settings import MEMBERS


class UserCheckMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        user = data["event_from_user"]
        if user.username in MEMBERS.keys():
            return await handler(event, data)
        await event.answer('Вы не зарегистрированы в системе, '
                           'обратитесь к администратору для добавления вас в список пользователей')
        return

