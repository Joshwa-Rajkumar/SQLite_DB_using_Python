# SQLite_DB_using_Python (College data)

Step 1: Database and Table Creation
I connected to an SQLite database and created a table named practice to store student information. The table included columns for student ID, student name, department, date of joining, and the fee amount. I made sure the table was created only if it didn't already exist, so running the code multiple times wouldn't cause errors.

Step 2: Data Insertion
Next, I prepared a list of student records with their respective departments and fee payments. I inserted this data into the table using a method that can handle multiple entries at once. I ensured that the data matched the table structure exactly to avoid mismatches and errors.

Step 3: Data Aggregation
Once the data was stored, I wrote a query to calculate the total fees collected from each department. I grouped the results by department and sorted them in descending order so the department contributing the most fees appeared at the top.

Step 4: Output Formatting
I printed the results in the console, making sure the department names and fee values were neatly aligned for easy reading. I encountered a few formatting issues initially, but corrected them using consistent spacing and proper float formatting.

Step 5: Pie Chart Visualization
To visualize the fee distribution, I used the matplotlib library to draw a pie chart. Each department was represented as a slice of the chart, showing the percentage of the total fees it contributed. I ensured the chart was well-labeled and displayed in a clean circular format.

Final Output
The program displayed a clear summary in the console, showing each department along with the total fees collected. It also generated a pie chart that gave a visual understanding of how fees were distributed among departments.

What I Learned
Through this project, I learned how to:

Create and manage an SQLite database using Python

Insert and organize data efficiently

Write SQL queries to summarize and group data

Format output for readability

Visualize data using pie charts

This was a useful and practical exercise that helped me understand how to handle real-world data and present it effectively.
