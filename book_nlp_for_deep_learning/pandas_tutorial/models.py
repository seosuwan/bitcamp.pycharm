import pandas
import pandas as pd


class OlympicMedals(object):
    pass

    def read_wiki(self) -> object:
        df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table')
        print(df)
        return df