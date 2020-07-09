from tkinter import ttk


class Treeview(ttk.Treeview):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.heading("#0", text="Versions")

    @property
    def selected_item(self):
        return self.item(self.selection())
    
    def clean(self):
        children = self.get_children()

        if children:
            for child in children:
                self.delete(child)

    def insert_items(self, items, highlight=None):
        assert isinstance(items, (tuple, list))

        for item in items:
            if highlight:
                if item == highlight:
                    item = '> ' + item
                else:
                    item = '  ' + item
             
            self.insert('', 0, text=item)
