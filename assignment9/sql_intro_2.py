#Task 5: Read Data into a DataFrame

import sqlite3
import pandas as pd



with sqlite3.connect("../db/lesson.db") as conn:
    
    


#2.Read data into a DataFrame. The SQL statement should retrieve the line_item_id, quantity, product_id, product_name, 
# and price from a JOIN of the line_items table and the product table. Hint: Your ON statement would be
#  ON line_items.product_id = products.product_id.

    sql_statement = """ SELECT li.line_item_id, li.quantity, p.product_id, p.product_name, p.price
                        FROM line_items li JOIN products p ON li.product_id = p.product_id """

    df= pd.read_sql_query(sql_statement, conn)
    
    #3.Print the first 5 lines of the resulting DataFrame. Run the program to make sure this much works.
    print(df.head())

    #4.Add a column to the DataFrame called "total"
    df["total"] = df['quantity'] * df['price']
    print(df.head())

    #5.Add groupby() code to group by the product_id. Use an agg() method that specifies 'count' for the 
    # line_item_id column, 'sum' for the total column, and 'first' for the 'product_name'
    grouped_df = df.groupby("product_id").agg({ "line_item_id": "count",   "total": "sum",           
                    "product_name": "first"  })

    print(grouped_df.head())

    #6.Sort the DataFrame by the product_name column.
    grouped_df = grouped_df.sort_values(by= "product_name" )

    #7.Add code to write this DataFrame to a file order_summary.csv
    grouped_df.to_csv('./order_summary.csv', index=False)