import wikipedia
import pandas as pd

# print(wikipedia.summary("Programming"))
# print(wikipedia.search("Apple"))

companies = pd.read_csv("companies.csv")

companies_list = companies['company'].values.tolist()
# print(companies_list)

values = [wikipedia.summary("'%s'" % company) for company in companies_list]


dicts = {}
for k, v in zip(companies_list, values):
    dicts[k] = v
print(dicts)

new_df = pd.DataFrame.from_dict(dicts, orient='index')
print(new_df)
