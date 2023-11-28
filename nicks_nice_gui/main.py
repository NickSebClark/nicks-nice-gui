from nicegui import ui

ui.label("Hello NiceGUI!")

with ui.dialog() as dialog, ui.card():
    ui.label("Hello world!")
    ui.button("Close", on_click=dialog.close)

ui.button("Open a dialog", on_click=dialog.open)

ui.run(port=8081)
