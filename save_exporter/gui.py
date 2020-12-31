try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
from tkcalendar import DateEntry

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.labels = []
    
    def add_label(self, text):
        self.label = tk.Label(self, text=text)
        self.label.pack(padx=10, pady=10)
    
    def change_label(self, text, num=0):
        self.labels[num]["text"] = text

class CredentialInput(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.entries = []
    
    def add_entry(self, text):
        label = tk.Label(self, text=text)
        label.pack(padx=10, pady=10)
        self.labels.append(label)

        cal = tk.Entry(self)
        cal.pack(padx=10, pady=10)
        self.entries.append(cal)

class CalendarSelect(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.calendars = []
    
    def add_calendar(self, text):
        label = tk.Label(self, text=text)
        label.pack(padx=10, pady=10)
        self.labels.append(label)

        cal = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2)
        cal.pack(padx=10, pady=10)
        self.calendars.append(cal)

class SaveFetcherGUI(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.pages = [CredentialInput(self), CalendarSelect(self), Page(self)]
        self.page_funcs = []

        self.pages[0].add_entry("Username")
        self.pages[0].add_entry("Password")
        self.pages[1].add_calendar("From Date")
        self.pages[1].add_calendar("To Date")
        self.pages[2].add_label("Currently working...")

        self.current_page = 0
        self.setup_gui()

    def setup_style(self):
        pass

    def setup_gui(self):
        buttonframe = tk.Frame(self)
        container = tk.Frame(self)

        # pack last?
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        for page in self.pages:
            page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        button = tk.Button(buttonframe, text="next page", command=self.next_page)
        button.pack(side="left")
        self.pages[0].lift()

    def next_page(self):
        if self.current_page + 1 < len(self.pages):
            if self.page_funcs[self.current_page]():
                self.current_page += 1
                self.pages[self.current_page].lift()

if __name__ == "__main__":
    root = tk.Tk()
    main = SaveFetcherGUI(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()