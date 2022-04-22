from imports import pd, DataFrame
from API import content


# Raw df
df = pd.DataFrame(content)

# Drop columns
drop_list = [
    "state_fips_code",
    "res_county",
    "county_fips_code",
    "ethnicity",
    "process",
    "case_positive_specimen",
]


df = df.drop(columns=drop_list)
