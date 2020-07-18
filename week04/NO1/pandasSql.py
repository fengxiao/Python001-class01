import pandas as pd
import numpy as np

# 聚合
ageandsalarys = [{'id': 100,'type':'a', 'age': 15, 'salary': 2000, 'month': 140},
         {'id': 200,'type':'b',  'age': 20, 'salary': 2100, 'month': 215},
         {'id': 300,'type':'a',  'age': 30,  'salary': 900,  'month': 95 },
         {'id': 400,'type':'a',  'age': 40,  'salary': 1100,  'month': 120 },
         {'id': 500,'type':'a',  'age': 34,  'salary': 2000,  'month': 120 },
         {'id': 600,'type':'a',  'age': 60,  'salary': 2000,  'month': 120 },
         {'id': 700,'type':'c',  'age': 20,  'salary': 1100,  'month': 120 },
         {'id': 800,'type':'c',  'age': 20,  'salary': 1100,  'month': 120 },
         {'id': 900,'type':'c',  'age': 60,  'salary': 1100,  'month': 120 },
         {'id': 1000,'type':'c',  'age': 40,  'salary': 1100,  'month': 120 },
         {'id': 1100,'type':'c',  'age': 40,  'salary': 1100,  'month': 120 },
         {'id': 1200,'type':'c',  'age': 40,  'salary': 1100,  'month': 120 },
         {'id': 1300,'type':'c',  'age': 40,  'salary': 1100,  'month': 120 },
         {'id': 1400,'type':'c',  'age': 60,  'salary': 1100,  'month': 120 }]

employees = [{'id': 100,'name':'a1', 'age': 15},
         {'id': 200,'name':'b2',  'age': 20},
         {'id': 300,'name':'a3',  'age': 30},
         {'id': 400,'name':'a4',  'age': 40},
         {'id': 500,'name':'a5',  'age': 34},
         {'id': 600,'name':'a6',  'age': 60},
         {'id': 700,'name':'c7',  'age': 20},
         {'id': 800,'name':'c8',  'age': 20},
         {'id': 900,'name':'c9',  'age': 60},
         {'id': 1000,'name':'c10',  'age': 40},
         {'id': 1100,'name':'c11',  'age': 40},
         {'id': 1200,'name':'c12',  'age': 40},
         {'id': 1300,'name':'c13',  'age': 40},
         {'id': 1400,'name':'c14',  'age': 60},
         {'id': 1500,'name':'c15',  'age': 65}]

df_salary = pd.DataFrame(ageandsalarys)
df_employee = pd.DataFrame(employees)

# 1. SELECT * FROM data;
df_salary.iloc[:, :]

# 2. SELECT * FROM data LIMIT 10;
df_salary.head(10)

# 3. SELECT id FROM data; //id 是 data 表的特定一列
df_salary['id']
df_salary['id'].head(10)

# 4. SELECT COUNT(id) FROM data;
df_salary.aggregate( {'id':'count'})

# 5.SELECT * FROM data WHERE id < 1000 AND age > 30;
df_salary[(df_salary['id']<1000) & (df_salary['age']>30)]
df_salary[(df_salary['id']<200) | (df_salary['age']>50)]

# 6. SELECT type,COUNT(DISTINCT salary) FROM table1 GROUP BY type;
# https://msd.misuland.com/pd/3107373619924173594
df_salary.drop_duplicates(subset=['type','salary'], keep='first', inplace=False).groupby('type').aggregate( {'salary':'count'})

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
pd.merge(df_employee, df_salary, on= 'id', how='inner')
pd.merge(df_employee, df_salary, on= 'id', how='left')

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
pd.concat([df_employee, df_salary])

# 9. DELETE FROM table1 WHERE id=10;
# https://www.cnblogs.com/wodexk/p/10316674.html
df_employee.drop(labels = (df_employee[df_employee['id'] == 1500].index), axis = 0)
df_employee.drop(labels = (df_employee[df_employee['id'] > 1000].index), axis = 0)


# 10. ALTER TABLE table1 DROP COLUMN column_name;
df_salary.drop(labels='type',axis=1)





