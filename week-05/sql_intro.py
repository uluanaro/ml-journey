import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')

data = pd.DataFrame({
    'id':     [1, 2, 3, 4, 5, 6],
    'name':   ['Anna', 'Boris', 'Vera', 'Dmitry', 'Elena', 'Fedor'],
    'age':    [25, 40, 30, 35, 28, 45],
    'salary': [50000, 80000, 60000, 75000, 55000, 90000],
    'dept':   ['IT', 'Sales', 'IT', 'Sales', 'IT', 'Sales']
})
data.to_sql('employees', conn, index=False, if_exists='replace')

departments = pd.DataFrame({
    'dept':      ['IT', 'Sales', 'HR'],
    'floor':     [3, 5, 2],
    'budget':    [1000000, 2000000, 500000]
})
departments.to_sql('departments', conn, index=False, if_exists='replace')

def q(sql):
    return pd.read_sql(sql, conn)



# print(q("SELECT * FROM employees"))
# print(q("SELECT name, salary "
#         "FROM employees"))
# print(q("SELECT * FROM employees "
#         "WHERE salary > 60000"))
# print(q("SELECT * FROM employees "
#         "ORDER BY age DESC"))
# print(q("SELECT DISTINCT dept FROM employees"))
# print(q("SELECT * FROM employees "
#         "ORDER BY salary DESC "
#         "LIMIT 3"))

# print(q("SELECT dept, COUNT(*) FROM employees "
#         "GROUP BY dept"))
# print(q("SELECT AVG(salary), dept FROM employees "
#         "GROUP BY dept"))
# print(q("SELECT MAX(age), dept FROM employees "
#         "GROUP BY dept"))
# print(q("SELECT dept FROM employees "
#         "GROUP BY dept "
#         "HAVING AVG(salary) > 65000"))
# print(q("SELECT dept, AVG(salary) FROM employees "
#         "WHERE age > 26 "
#         "GROUP BY dept"))
#
#print(q("SELECT employees.name, departments.dept, departments.floor FROM employees "
#         "INNER JOIN departments ON employees.dept = departments.dept"))
# print(q("SELECT employees.name, departments.dept FROM employees "
#         "LEFT JOIN departments ON employees.dept = departments.dept"))
# print(q("SELECT employees.name, departments.dept FROM employees "
#         "RIGHT JOIN departments ON employees.dept = departments.dept"))
#
# print(q("SELECT name, salary FROM employees "
#         "WHERE salary > (SELECT AVG(salary) FROM employees)"))
# print(q("SELECT name FROM employees "
#         "WHERE age > (SELECT AVG(age) FROM employees)"))
# print(q("WITH avg_table AS ("
#         "SELECT AVG(salary) AS avg_salary FROM employees) "
#         "SELECT name, salary FROM employees, avg_table "
#         "WHERE salary > avg_salary"))
#
# print(q("SELECT dept, AVG(salary) FROM employees GROUP BY dept"))
# print(q("SELECT name, dept, salary, "
#        "AVG(salary) OVER (PARTITION BY dept) AS dept_avg "
#         "FROM employees"))
#
print(q("SELECT name, dept, salary,"
        " AVG(salary) OVER (PARTITION BY dept) AS dept_avg "
        "FROM employees "))
print(q("SELECT dept, name, salary, "
        "ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) as row_num "
        "FROM employees"))
print(q("SELECT dept, name, salary, "
        "ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) as row_num, "
        "RANK() OVER (PARTITION BY dept ORDER BY salary DESC) as rk "
        "FROM employees"))
print(q("SELECT name, salary,"
        " LAG(salary) OVER (ORDER BY salary DESC) AS prev_worker "
        "FROM employees"))