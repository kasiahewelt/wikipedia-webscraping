import pandas as pd
import wikipedia
from wikipedia import PageError


def form_df():
    df = pd.read_csv("helix_no_description.csv")
    companies_list = df['self_firmo_name___'].values.tolist()
    try:
        val = [wikipedia.summary("%s" % company) for company in companies_list]
        dicts = {}
        for k, v in zip(companies_list, val):
            dicts[k] = v
        new_df = pd.DataFrame.from_dict(dicts, orient='index')
        print(new_df)
    except PageError:
        pass


if __name__ == '__main__':
    form_df()
