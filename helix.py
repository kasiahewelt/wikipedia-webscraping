import pandas as pd
import wikipedia
from wikipedia import PageError

df = pd.read_csv("helix_no_description.csv")

val = []
companies_list = df['self_firmo_name___'].values.tolist()
for company in companies_list:
    try:
        print(wikipedia.summary("%s" % company, auto_suggest=False, redirect=True))
        val.append(wikipedia.summary("%s" % company, auto_suggest=False, redirect=True))
    except PageError as e:
        print(e)


def form_df():
    print(df.T)
    try:
        dicts = {}
        for k, v in zip(companies_list, val):
            dicts[k] = v
        new_df = pd.DataFrame.from_dict(dicts, orient='index')
        print(new_df)
    except PageError:
        pass


if __name__ == '__main__':
    form_df()
