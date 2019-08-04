from tkinter import ttk
import tkinter as tk
import winsound
import datetime as dt
import json
import mlb
import nfl
import compare


class ValueFinder(object):

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('660x660')
        self.root.title('ArbFinder')
        # self.root.iconbitmap('images/Baseball.ico')
        self.nb = ttk.Notebook(self.root)

        results_tab = ttk.Frame(self.nb)
        settings_tab = ttk.Frame(self.nb)
        self.nb.add(results_tab, text="Results")
        self.nb.add(settings_tab, text='Settings')
        self.nb.pack(expand=1, fill='both')

        self.results = tk.Text(results_tab, wrap=tk.WORD)
        self.results.pack(expand=True, fill='both')
        self.results.config(background='grey14', fg='green3')
        self.found = set()
        self.message_value = []

        tk.Label(settings_tab, text="Sports to check:").pack(anchor='w')
        self.settings = json.load(open('settings.json'))
        self.vars = []
        for setting in self.settings:
            if self.settings[setting]:
                var = tk.IntVar(value=1)
            else:
                var = tk.IntVar()
            chk = tk.Checkbutton(settings_tab, text=setting, variable=var)
            chk.pack(side='left', anchor='nw')
            self.vars.append(var)

        tk.Button(settings_tab, command=self.save_selections, text='Save').pack(side='left', anchor='nw')

    def save_selections(self):
        selections = self.state()
        sports = ["NBA", "NCAAB", "MLB", "NHL", "NFL", "NCAAF", "Email"]
        data = dict()
        for sport, selection in zip(sports, selections):
            data.update({sport: selection})

        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)

    def state(self):
        # could make part of save_selections, but considering using this to also check before running instead
        # of relying on JSON read
        return map((lambda v: v.get()), self.vars)

    def add_to_gui(self, values):
        for value in values:
            if value in self.found:
                self.results.insert('end', value)
            else:
                winsound.Beep(440, 500)
                self.results.insert('1.0', value, 'NEW_GAME')
                self.results.tag_config('NEW_GAME', foreground='red', background='yellow')
                self.found.add(value)
                # self.message_value.append(value)
                with open('results.txt', 'a') as results:
                    results.write(f'{dt.datetime.now()}: {value}')

    def update(self):
        self.results.delete('1.0', 'end')
        if self.vars[0].get():
            # NBA
            pass
        if self.vars[1].get():
            # NCAAB
            pass
        if self.vars[2].get():
            # MLB
            run_lines = mlb.get_runlines()
            moneylines = mlb.get_moneylines()
            totals = mlb.get_totals()
            self.add_to_gui(compare.compare_spreads(run_lines))
            self.add_to_gui(compare.compare_ml(moneylines))
            self.add_to_gui(compare.compare_totals(totals))
        if self.vars[3].get():
            # NHL
            pass
        if self.vars[4].get():
            # NFL
            moneylines = nfl.get_money_lines()
            self.add_to_gui(compare.compare_ml(moneylines))
        if self.vars[5].get():
            # NCAAF
            pass
        if self.vars[6].get() and self.message_value:
            # email
            pass
        self.results.insert('1.0', f'Updated: {dt.datetime.now().strftime("%Y/%m/%d %I:%M %p")}\n')
        myApp.root.after(25000, myApp.update)


if __name__ == "__main__":
    myApp = ValueFinder()
    myApp.update()
    myApp.root.mainloop()