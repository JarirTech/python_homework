import sqlite3

#Task 1: Complex JOINs with Aggregation

#Find the total price of each of the first 5 orders.  There are several steps.  
# You need to join the orders table with the line_items table and the products table.  
# You need to GROUP_BY the order_id.  You need to select the order_id and the SUM of the product
#  price times the line_item quantity.  Then, you ORDER BY order_id and LIMIT 5.  You don't need a 
# subquery. Print out the order_id and the total price for each of the rows returned.
# Find the total price of each of the first 5 orders
#join order table with line_items and product table group_by order_id
#You need to select the order_id and the SUM of the product price times the line_item quantity.


#customer table: cust_id(primary key), customer_name
#order table: cust_id (foreign key), order_id
#line_items table: order_id, product_id
#product table: product_id
conn = sqlite3.connect("../db/lesson.db",isolation_level='IMMEDIATE')
conn.execute("PRAGMA foreign_keys = 1")

cursor = conn.cursor()


query1 = (""" SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    LIMIT 5 """)
cursor.execute(query1)
# Print out the order_id and the total price for each of the rows returned.
for row in cursor.fetchall():
    print(row)

#----------------------------------------------------------------------------------------------
#Task 2: Understanding Subqueries


#For each customer, find the average price of their orders.
#with a subquery. You compute the price of each order as in part 1, but you return the customer_id
#  and the total_price. You need to return the total price using AS total_price, and you need to 
# return the customer_id with AS customer_id_b

# we need to Return the customer name and the average_total_price.
query2 = (""" SELECT c.customer_name, AVG(sub.total_price) AS average_total_price
    FROM customers c
    LEFT JOIN (SELECT o.customer_id AS customer_id_b, SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id) sub ON c.customer_id = sub.customer_id_b
    GROUP BY c.customer_id """)

cursor.execute(query2)
#print out the result.
for row in cursor.fetchall():
    print(row)

#------------------------------------------------------------------------------------------------

#Task 3: An Insert Transaction Based on Data

#new order for the customer named Perez and Sons 
# wants 10 of each of the 5 least expensive products. 


# retrieve the customer_id, another 
try:
    cursor.execute( "SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'" )

    customer_id = cursor.fetchone()[0]

    #retrieve the product_ids of the 5 least expensive products using ORDER BY
    cursor.execute( """ SELECT product_id FROM products ORDER BY price LIMIT 5 """)
    product_ids = cursor.fetchall()

    #retrieve the employee_id

    cursor.execute( """ SELECT employee_id FROM employees 
                WHERE first_name = 'Miranda' AND last_name = 'Harris' """)
    employee_id = cursor.fetchone()[0]

    #create the order record
    cursor.execute( """ INSERT INTO orders (customer_id, employee_id) VALUES (?, ?)
                RETURNING order_id """,(customer_id, employee_id))
    order_id = cursor.fetchone()[0]

    # 5 line_item records 
    for (product_id,) in product_ids:
        cursor.execute( """ INSERT INTO line_items (order_id, product_id, quantity)
                    VALUES (?, ?, 10) """, (order_id, product_id))


    conn.commit()
except Exception as e:
    conn.rollback()
    raise e

# using a SELECT with a JOIN, print out the list of line_item_ids for the order along 
# with the quantity and product name for each.

cursor.execute( """ SELECT li.line_item_id, li.quantity, p.product_name
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id
        WHERE li.order_id = ? """, (order_id,) )

for row in cursor.fetchall():
    print(row)

#------------------------------------------------------------------------------------

#Task 4: Aggregation with HAVING
#Find all employees associated with more than 5 orders.
#  using first_name, last_name, and count of orders
#do a JOIN on the employees and orders tables, and then use GROUP BY, COUNT, and HAVING.

query4= (""" SELECT  e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count 
        FROM employees e 
        JOIN orders o ON e.employee_id = o.employee_id
        GROUP BY e.employee_id
        HAVING COUNT(o.order_id) > 5 """)

cursor.execute(query4)
for row in cursor.fetchall():
    print(row)
conn.close()