from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock
import json
from Sports import football as fb, not_football as nf
import compare
import datetime as dt


kv = Builder.load_file("main.kv")


class Display(Widget):
    display_window = StringProperty()

    def __init__(self, **kwargs):
        super(Display, self).__init__(**kwargs)
        self.display_window = 'Lets get started'
        self.settings = json.load(open('settings.json'))

        self.nfl_ml = 'https://classic.sportsbookreview.com/betting-odds/nfl-football/money-line/'
        self.nfl_spreads = 'https://classic.sportsbookreview.com/betting-odds/nfl-football/'
        self.nfl_totals = 'https://classic.sportsbookreview.com/betting-odds/nfl-football/totals/'

        self.ncaaf_ml = 'https://classic.sportsbookreview.com/betting-odds/college-football/money-line/'
        self.ncaaf_spreads = 'https://classic.sportsbookreview.com/betting-odds/college-football/'
        self.ncaaf_totals = 'https://classic.sportsbookreview.com/betting-odds/college-football/totals/'

        self.nba_ml = 'https://classic.sportsbookreview.com/betting-odds/nba-basketball/money-line/'
        self.nba_spreads = 'https://classic.sportsbookreview.com/betting-odds/nba-basketball/'
        self.nba_totals = 'https://classic.sportsbookreview.com/betting-odds/nba-basketball/totals/'

        self.ncaab_ml = 'https://classic.sportsbookreview.com/betting-odds/ncaa-basketball/money-line/'
        self.ncaab_spreads = 'https://classic.sportsbookreview.com/betting-odds/ncaa-basketball/'
        self.ncaab_totals = 'https://classic.sportsbookreview.com/betting-odds/ncaa-basketball/totals/'

        self.mlb_ml = 'https://classic.sportsbookreview.com/betting-odds/mlb-baseball/'
        self.mlb_spreads = 'https://classic.sportsbookreview.com/betting-odds/mlb-baseball/pointspread/'
        self.mlb_totals = 'https://classic.sportsbookreview.com/betting-odds/mlb-baseball/totals/'

        self.nhl_ml = 'https://classic.sportsbookreview.com/betting-odds/nhl-hockey/'
        self.nhl_spreads = 'https://classic.sportsbookreview.com/betting-odds/nhl-hockey/pointspread/'
        self.nhl_totals = 'https://classic.sportsbookreview.com/betting-odds/nhl-hockey/totals/'

    def update_settings(self, instance, name, value):
        with open('settings.json', 'r') as file:
            data = json.load(file)

        data[f'{name}'] = value

        with open("settings.json", "w+") as file:
            json.dump(data, file)

    def update(self, t):
        self.display_window = f'Updated: {dt.datetime.now().strftime("%Y/%m/%d %I:%M %p")}\n'
        if self.settings['NFL']:
            moneylines = compare.moneylines(fb.get_money_lines(self.nfl_ml), 'NFL')
            spreads = compare.spreads(fb.get_spreads(self.nfl_spreads), 'NFL')
            totals = compare.totals(fb.get_totals(self.nfl_totals), 'NFL')
            self.display_window += ''.join(moneylines)
            self.display_window += ''.join(spreads)
            self.display_window += ''.join(totals)

        if self.settings['NCAAF']:
            moneylines = compare.moneylines(fb.get_money_lines(self.ncaaf_ml), 'NCAAF')
            spreads = compare.spreads(fb.get_spreads(self.ncaaf_spreads), 'NCAAF')
            totals = compare.totals(fb.get_totals(self.ncaaf_totals), 'NCAAF')
            self.display_window += ''.join(moneylines)
            self.display_window += ''.join(spreads)
            self.display_window += ''.join(totals)

        if self.settings['NBA']:
            moneylines = compare.moneylines(nf.get_moneylines(self.nba_ml, 'nba-basketball'), 'NBA')
            spreads = compare.spreads(nf.get_spreads(self.nba_spreads, 'nba-basketball'), 'NBA')
            totals = compare.totals(nf.get_totals(self.nba_totals, 'nba-basketball'), 'NBA')
            self.display_window += ''.join(moneylines)
            self.display_window += ''.join(spreads)
            self.display_window += ''.join(totals)

        if self.settings['NCAAB']:
            moneylines = compare.moneylines(nf.get_moneylines(self.ncaab_ml, 'ncaa-basketball'), 'NCAAB')
            spreads = compare.spreads(nf.get_spreads(self.ncaab_spreads, 'ncaa-basketball'), 'NCAAB')
            totals = compare.totals(nf.get_totals(self.ncaab_totals, 'ncaa-basketball'), 'NCAAB')
            self.display_window += ''.join(moneylines)
            self.display_window += ''.join(spreads)
            self.display_window += ''.join(totals)

        if self.settings['NHL']:
            moneylines = compare.moneylines(nf.get_moneylines(self.nhl_ml, 'nhl-hockey'), 'NHL')
            spreads = compare.spreads(nf.get_spreads(self.nhl_spreads, 'nhl-hockey'), 'NHL')
            totals = compare.totals(nf.get_totals(self.nhl_totals, 'nhl-hockey'), 'NHL')
            self.display_window += ''.join(moneylines)
            self.display_window += ''.join(spreads)
            self.display_window += ''.join(totals)

        if self.settings['MLB']:
            moneylines = compare.moneylines(nf.get_moneylines(self.nhl_ml, 'mlb-baseball'), 'MLB')
            spreads = compare.spreads(nf.get_spreads(self.nhl_spreads, 'mlb-baseball'), 'MLB')
            totals = compare.totals(nf.get_totals(self.nhl_totals, 'mlb-baseball'), 'MLB')
            self.display_window += ''.join(moneylines)
            self.display_window += ''.join(spreads)
            self.display_window += ''.join(totals)


class ArbApp(App):
    settings = json.load(open('settings.json'))
    nfl_active = settings['NFL']
    ncaaf_active = settings['NCAAF']
    nba_active = settings['NBA']
    ncaab_active = settings['NCAAB']
    nhl_active = settings['NHL']
    mlb_active = settings['MLB']

    def build(self):
        display = Display()
        Clock.schedule_interval(display.update, 30)

        return display


if __name__ == '__main__':
    ArbApp().run()
