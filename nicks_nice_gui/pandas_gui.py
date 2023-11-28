#!/usr/bin/env python3
import pandas as pd
from pandas.api.types import is_bool_dtype, is_numeric_dtype

from nicegui import ui

df = pd.DataFrame(
    data={
        "col1": [x for x in range(4)],
        "col2": ["This", "column", "contains", "strings."],
        "col3": [x / 4 for x in range(4)],
        "col4": [True, False, True, False],
    }
)

json = [
    {
        "array": [1, 2, 3],
        "boolean": True,
        "color": "#82b92c",
        None: None,
        "number": 123,
        "object": {
            "a": "b",
            "c": "d",
        },
        "time": 1575599819000,
        "string": "Hello World",
    },
    {
        "array": [1, 2, 3],
        "boolean": True,
        "color": "#82b92c",
        None: None,
        "number": 123,
        "object": {
            "a": "b",
            "c": "d",
        },
        "time": 1575599819000,
        "string": "Hello World",
    },
]


def update(*, df: pd.DataFrame, r: int, c: int, value):
    df.iat[r, c] = value
    ui.notify(f"Set ({r}, {c}) to {value}")


with ui.splitter() as splitter:
    with splitter.before:
        with ui.grid(rows=len(df.index) + 1).classes("grid-flow-col"):
            for c, col in enumerate(df.columns):
                ui.label(col).classes("font-bold")
                for r, row in enumerate(df.loc[:, col]):
                    if is_bool_dtype(df[col].dtype):
                        cls = ui.checkbox
                    elif is_numeric_dtype(df[col].dtype):
                        cls = ui.number
                    else:
                        cls = ui.input
                    cls(
                        value=row,
                        on_change=lambda event, r=r, c=c: update(
                            df=df, r=r, c=c, value=event.value
                        ),
                    )
    with splitter.after:
        ui.json_editor(
            {"content": {"json": json}},
            on_select=lambda e: ui.notify(f"Select: {e}"),
            on_change=lambda e: ui.notify(f"Change: {e}"),
        )

ui.run(port=8081)
