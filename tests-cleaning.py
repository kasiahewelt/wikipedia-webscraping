from cleanco import basename
import pandas as pd

df = pd.read_csv("helix_no_description.csv")
business_name = "Some Big Pharma, LLC"
print(basename(business_name))
