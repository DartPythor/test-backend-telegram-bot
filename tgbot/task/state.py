from aiogram.fsm.state import State, StatesGroup


class TaskState(StatesGroup):
    title = State()
    description = State()
    due_date = State()
    tags = State()
    confirm = State()
