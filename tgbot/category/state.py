from aiogram.fsm.state import State, StatesGroup


class CategoryState(StatesGroup):
    name = State()
    confirm = State()


class CategoryListState(StatesGroup):
    list = State()
    page = State()


class CategoryDeleteState(StatesGroup):
    delete = State()
    confirm = State()
    category_id = State()
