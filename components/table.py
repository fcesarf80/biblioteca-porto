from tkinter import ttk


class Table(ttk.Treeview):

    def __init__(
        self,
        master,
        columns,
        x,
        y,
        width,
        height
    ):

        column_ids = [
            column[0]
            for column in columns
        ]

        style = ttk.Style()

        style.theme_use("clam")

        style.configure(
            "Table.Treeview",
            borderwidth=0,
            relief="flat",
            highlightthickness=0,
            background="white",
            fieldbackground="white"
        )

        style.configure(
            "Table.Treeview.Heading",
            relief="flat",
            borderwidth=0
        )

        super().__init__(
            master,
            columns=column_ids,
            show="",
            style="Table.Treeview"
        )

        style.layout(
            "Table.Treeview",
            [
                (
                    "Treeview.treearea",
                    {"sticky": "nswe"}
                )
            ]
        )

        self.place(
            x=x,
            y=y,
            width=width,
            height=height
        )

        for name, column_width, anchor in columns:

            self.heading(
                name,
                text=name,
                anchor=anchor
            )

            self.column(
                name,
                width=column_width,
                minwidth=column_width,
                stretch=False,
                anchor=anchor
            )

    def clear(self):

        for item in self.get_children():

            self.delete(item)

    def add_row(
        self,
        values
    ):

        self.insert(
            "",
            "end",
            values=values
        )