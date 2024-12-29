from aiogram import Router, F

from .start import start_router
from .my_info import  my_info_router
from .random import random_router
from .restaurant import  menu_router
from .review_dialog import dialog_router
from .restaurant_management import restaurant_management_router
from .dishes import restaurant_router

from .other_message import echo_router

individual_router = Router()


individual_router.include_router(start_router)
individual_router.include_router(my_info_router)
individual_router.include_router(random_router)
individual_router.include_router(menu_router)
individual_router.include_router(dialog_router)
individual_router.include_router(restaurant_management_router)
individual_router.include_router(restaurant_router)
individual_router.include_router(echo_router)

individual_router.message.filter(F.chat.type == "individual")
individual_router.callback_query.filter(F.chat.type == "individual")