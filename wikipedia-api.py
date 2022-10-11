import wikipedia
import pandas as pd
import time

# print(wikipedia.summary("Netfl"))
xx = wikipedia.page("Netlix")
# print(xx.content)
catego = xx.categories

tic = time.perf_counter()
if any("Companies" in s for s in catego):
    companies = pd.read_csv("companies.csv")
    companies_list = companies['company'].values.tolist()

    values = [wikipedia.summary("'%s'" % company) for company in companies_list]
    dicts = {}
    for k, v in zip(companies_list, values):
        dicts[k] = v
    # print(dicts)

    new_df = pd.DataFrame.from_dict(dicts, orient='index')
    new_df = new_df.reset_index()
    new_df.columns = ['company', 'description']
    print(new_df)
toc = time.perf_counter()
print(f"Code executed in {toc - tic:0.4f} seconds")

