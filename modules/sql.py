from imports import sqlite3, pd
from clean import df
from states import states

conn = sqlite3.connect("covid_cases.db")
c = conn.cursor()

"""CREATE cases TABLE"""
# df.to_sql("cases", conn, index_label="id")

"""VIEW COLUMN NAMES"""
# c.execute("PRAGMA table_info(cases);")

#State Exposures
def get_state_exposures(state_abbr: str) -> int:
    c.execute(
        "SELECT * FROM cases WHERE res_state LIKE :state_abbr",
        {"state_abbr": state_abbr},
    )
    return len(c.fetchall())


for state in states:
    states[state] = get_state_exposures(state)

print(sorted(states.items(), key=lambda x: x[1], reverse=True))

conn.close()
