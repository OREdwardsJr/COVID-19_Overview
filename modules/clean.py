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


def drop_cols(cols: list, df_input: DataFrame) -> DataFrame:
    for col in cols:
        df_input = df_input.drop(columns=col)
    return df_input


df = drop_cols(drop_list, df)