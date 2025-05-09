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


from tgbot.category.getters import (
    on_name_entered,
    get_category_data,
    on_id_entered,
    get_category_data_delete,
    category_getter,
)
from tgbot.category.state import CategoryState, CategoryListState, CategoryDeleteState
from tgbot.category.until import on_confirm, on_confirm_delete


def get_dialog_category() -> Dialog:
    return Dialog(
        Window(
            Const("✏️ Введите название тега:"),
            MessageInput(on_name_entered),
            Cancel(Const("❌ Отмена")),
            state=CategoryState.name,
        ),
        Window(
            Format("✅ Подтвердите данные тега:\n\n" "Название: {name}\n"),
            Button(
                Const("✔️ Создать"),
                id="confirm",
                on_click=on_confirm,
            ),
            Back(Const("◀️ Назад")),
            Cancel(Const("❌ Отмена")),
            state=CategoryState.confirm,
            getter=get_category_data,
        ),
    )


def get_categories_dialog() -> Dialog:
    return Dialog(
        Window(
            Format("📁 Теги"),
            ScrollingGroup(
                Select(
                    Format("{item[name]}"),
                    id="category_sel",
                    item_id_getter=lambda item: item["category_id"],
                    items="categories",
                    on_click=category_getter,
                ),
                id="scroll_category",
                width=1,
                height=5,
            ),
            state=CategoryListState.list,
            getter=category_getter,
        ),
    )


def get_delete_categories_dialog() -> Dialog:
    return Dialog(
        Window(
            Const("✏️ Введите ID тега:"),
            MessageInput(on_id_entered),
            Cancel(Const("❌ Отмена")),
            state=CategoryDeleteState.category_id,
        ),
        Window(
            Format("✅ Подтвердите данные тега:\n\n" "ID: {category_id}\n"),
            Button(
                Const("✔️ Удалить"),
                id="confirm",
                on_click=on_confirm_delete,
            ),
            Back(Const("◀️ Назад")),
            Cancel(Const("❌ Отмена")),
            state=CategoryDeleteState.confirm,
            getter=get_category_data_delete,
        ),
    )
