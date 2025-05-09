from aiogram.fsm.state import State, StatesGroup


class TaskState(StatesGroup):
    title = State()
    description = State()
    due_date = State()
    tags = State()
    confirm = State()


class TaskListState(StatesGroup):
    list = State()
    page = State()


class TaskDeleteState(StatesGroup):
    delete = State()
    confirm = State()
    task_id = State()
