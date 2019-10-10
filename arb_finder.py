from tkinter import ttk
import tkinter as tk
import winsound
import datetime as dt
import json
from Sports import mlb, nfl, nhl, nba
import compare


class ValueFinder(object):

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('660x660')
        self.root.title('ArbFinder')
        self.root.iconbitmap('images/dollar.ico')
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

        self.nfl_ml = 'https://classic.sportsbookreview.com/betting-odds/nfl-football/money-line/'
        self.nfl_spreads = 'https://classic.sportsbookreview.com/betting-odds/nfl-football/'
        self.nfl_totals = 'https://classic.sportsbookreview.com/betting-odds/nfl-football/totals/'

        self.ncaaf_ml = 'https://classic.sportsbookreview.com/betting-odds/college-football/money-line/'
        self.ncaaf_spreads = 'https://classic.sportsbookreview.com/betting-odds/college-football/'
        self.ncaaf_totals = 'https://classic.sportsbookreview.com/betting-odds/college-football/totals/'

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
        selections = [var.get() for var in self.vars]
        sports = ["NBA", "NCAAB", "MLB", "NHL", "NFL", "NCAAF", "Email"]
        data = dict()
        for sport, selection in zip(sports, selections):
            data.update({sport: selection})

        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)

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
            moneylines = nba.get_moneylines()
            spreads = nba.get_spreads()
            totals = nba.get_totals()
            self.add_to_gui(compare.compare_spreads(spreads, 'NBA'))
            self.add_to_gui(compare.compare_ml(moneylines, 'NBA'))
            self.add_to_gui(compare.compare_totals(totals, 'NBA'))
        if self.vars[1].get():
            # NCAAB
            pass
        if self.vars[2].get():
            # MLB
            run_lines = mlb.get_runlines()
            moneylines = mlb.get_moneylines()
            totals = mlb.get_totals()
            self.add_to_gui(compare.compare_spreads(run_lines, 'MLB'))
            self.add_to_gui(compare.compare_ml(moneylines, 'MLB'))
            self.add_to_gui(compare.compare_totals(totals, 'MLB'))
        if self.vars[3].get():
            # NHL
            moneylines = nhl.get_moneylines()
            puck_lines = nhl.get_pucklines()
            totals = nhl.get_totals()
            self.add_to_gui(compare.compare_spreads(puck_lines, 'NHL'))
            self.add_to_gui(compare.compare_ml(moneylines, 'NHL'))
            self.add_to_gui(compare.compare_totals(totals, 'NHL'))
        if self.vars[4].get():
            # NFL
            moneylines = nfl.get_money_lines(self.nfl_ml)
            spreads = nfl.get_spreads(self.nfl_spreads)
            totals = nfl.get_totals(self.nfl_totals)
            self.add_to_gui(compare.compare_ml(moneylines, 'NFL'))
            self.add_to_gui(compare.compare_spreads(spreads, 'NFL'))
            self.add_to_gui(compare.compare_totals(totals, 'NFL'))
        if self.vars[5].get():
            # NCAAF
            moneylines = nfl.get_money_lines(self.ncaaf_ml)
            spreads = nfl.get_spreads(self.ncaaf_spreads)
            totals = nfl.get_totals(self.ncaaf_totals)
            self.add_to_gui(compare.compare_ml(moneylines, 'NCAAF'))
            self.add_to_gui(compare.compare_spreads(spreads, 'NCAAF'))
            self.add_to_gui(compare.compare_totals(totals, 'NCAAF'))
        if self.vars[6].get() and self.message_value:
            # email
            pass
        self.results.insert('1.0', f'Updated: {dt.datetime.now().strftime("%Y/%m/%d %I:%M %p")}\n')
        myApp.root.after(25000, myApp.update)


if __name__ == "__main__":
    myApp = ValueFinder()
    myApp.update()
    myApp.root.mainloop()
