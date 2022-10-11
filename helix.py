import pandas as pd
import wikipedia
from wikipedia import PageError

df = pd.read_csv("helix_no_description.csv")

# companies = df['self_firmo_name___']
# print(df)
# print(companies)
print(df.T)
companies_list = df['self_firmo_name___'].values.tolist()
val = [wikipedia.summary("%s" % company, auto_suggest=False, redirect=True) for company in companies_list]


def form_df():
    try:
        dicts = {}
        for k, v in zip(companies_list, val):
            dicts[k] = v
        # print(dicts)

        new_df = pd.DataFrame.from_dict(dicts, orient='index')
        print(new_df)
        return True
    except PageError:
        return False


if __name__ == '__main__':
    form_df()
