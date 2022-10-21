import wikipedia
from wikipedia import PageError, DisambiguationError
import streamlit as st
import pandas as pd

st.write("""
# Companies' description web scraping
## using wikipedia package
""")

show_file = st.empty()
file = st.file_uploader("Upload csv file", type=["csv"])

keys = []
val = []

if file:
    st.title('Uploaded Dataset:')
    df = pd.read_csv(file)
    st.dataframe(df.head(10))
    companies_list = df['self_firmo_name___'].values.tolist()
    for company in companies_list:
        try:
            page = wikipedia.page("%s" % company, auto_suggest=False, redirect=True)
            category = page.categories
            if any("Companies" in s for s in category):
                try:
                    keys.append(wikipedia.page("%s" % company, auto_suggest=False, redirect=True).title)
                    val.append(wikipedia.summary("%s" % company, auto_suggest=False, redirect=True))
                except (PageError, AssertionError, DisambiguationError) as e:
                    print(e)
        except (PageError, AssertionError, DisambiguationError, ConnectionError) as e:
            print(e)

    def form_df():
        try:
            dicts = {}
            for k, v in zip(keys, val):
                dicts[k] = v
            new_df = pd.DataFrame.from_dict(dicts, orient='index')
            new_df = new_df.reset_index()
            new_df.columns = ['company', 'description']
            st.header('Results:')
            st.dataframe(new_df)
            st.download_button("Download CSV", new_df.to_csv(), mime='text/csv')
        except PageError:
            pass

    if __name__ == '__main__':
        form_df()
else:
    show_file.info("PLease upload a {} file.".format(''.join(["csv"])))






