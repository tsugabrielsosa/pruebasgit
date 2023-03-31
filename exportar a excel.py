import pandas as pd
list1 = ["GABRIEL","ALEJANDRO","JONATHAN","MARJULY"]
list2 = [41,44,38,37]
col1 = "NOMBRE"
col2 = "EDAD"

data = pd.DataFrame({col1:list1,col2:list2})
data.to_excel('c:\\ejerciciospython\\sample_data.xlsx', sheet_name='sheet1', index=False)