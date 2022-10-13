import pandas as pd
import wikipedia
from wikipedia import PageError, DisambiguationError
import time

df = pd.read_csv("helix_no_description.csv")
tic = time.perf_counter()

val = []
companies_list = df['self_firmo_name___'].values.tolist()
for company in companies_list:
    try:
        print(wikipedia.summary("%s" % company, auto_suggest=False, redirect=True))
        val.append(wikipedia.summary("%s" % company, auto_suggest=False, redirect=True))
    except (PageError, AssertionError, DisambiguationError) as e:
        print(e)


def form_df():
    try:
        dicts = {}
        for k, v in zip(val, val):
            dicts[k] = v
        new_df = pd.DataFrame.from_dict(dicts, orient='index')
        new_df = new_df.reset_index()
        print(new_df)
    except PageError:
        pass


toc = time.perf_counter()
print(f"Code executed in {toc - tic:0.4f} seconds")

if __name__ == '__main__':
    form_df()
