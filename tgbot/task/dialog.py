from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import (
    Back,
    Cancel,
    Button,
    ScrollingGroup,
    Select,
)


from tgbot.task.getters import (
    on_title_entered,
    on_tags_entered,
    on_description_entered,
    on_due_date_entered,
    get_task_data,
    task_getter,
)
from tgbot.task.state import TaskState, TaskListState
from tgbot.task.until import on_confirm


def get_dialog_task() -> Dialog:
    return Dialog(
        Window(
            Const("✏️ Введите название задачи:"),
            MessageInput(on_title_entered),
            Cancel(Const("❌ Отмена")),
            state=TaskState.title,
        ),
        Window(
            Const("📝 Введите описание задачи:"),
            MessageInput(on_description_entered),
            Back(Const("◀️ Назад")),
            Cancel(Const("❌ Отмена")),
            state=TaskState.description,
        ),
        Window(
            Const("⏳ Введите дедлайн задачи (формат: ДД.ММ.ГГГГ ЧЧ:ММ):"),
            MessageInput(on_due_date_entered),
            Back(Const("◀️ Назад")),
            Cancel(Const("❌ Отмена")),
            state=TaskState.due_date,
        ),
        Window(
            Const("🏷 Введите теги задачи (через запятую):"),
            MessageInput(on_tags_entered),
            Back(Const("◀️ Назад")),
            Cancel(Const("❌ Отмена")),
            state=TaskState.tags,
        ),
        Window(
            Format(
                "✅ Подтвердите данные задачи:\n\n"
                "Название: {title}\n"
                "Описание: {description}\n"
                "Дедлайн: {due_date}\n"
                "Теги: {tags}"
            ),
            Button(
                Const("✔️ Создать"),
                id="confirm",
                on_click=on_confirm,
            ),
            Back(Const("◀️ Назад")),
            Cancel(Const("❌ Отмена")),
            state=TaskState.confirm,
            getter=get_task_data,
        ),
    )


def get_tasks_dialog() -> Dialog:
    return Dialog(
        Window(
            Format("📁 Теги"),
            ScrollingGroup(
                Select(
                    Format("{item[title]}"),
                    id="category_sel",
                    item_id_getter=lambda item: item["task_id"],
                    items="categories",
                    on_click=task_getter,
                ),
                id="scroll_category",
                width=1,
                height=5,
            ),
            state=TaskListState.list,
            getter=task_getter,
        ),
    )
