from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Back, Cancel, Button


from tgbot.category.getters import on_name_entered, get_category_data
from tgbot.category.state import CategoryState
from tgbot.category.until import on_confirm


def get_dialog_category() -> Dialog:
    return Dialog(
        Window(
            Const("✏️ Введите название тега:"),
            MessageInput(on_name_entered),
            Cancel(Const("❌ Отмена")),
            state=CategoryState.name,
        ),
        Window(
            Format(
                "✅ Подтвердите данные тега:\n\n"
                "Название: {name}\n"
            ),
            Button(
                Const("✔️ Создать"), id="confirm", on_click=on_confirm,
            ),
            Back(Const("◀️ Назад")),
            Cancel(Const("❌ Отмена")),
            state=CategoryState.confirm,
            getter=get_category_data,
        ),
    )
