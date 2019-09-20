import pandas as pd
calls_df, = pd.read_html ("spb.hh.ru/resume/8de51ecbff0235166a0039ed1f534c67356537")
print(calls_df)
for name, contents in drinks.items()