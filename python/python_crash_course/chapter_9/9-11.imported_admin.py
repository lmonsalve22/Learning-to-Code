""" Start with your work from Exercise 9-8 (page 178).
Store the classes User , Privileges , and Admin in one module. 
Create a separate file, make an Admin instance, and call 
show_privileges() to show that everything is working correctly """

from admin import Users, Privileges, Admin

james = Admin('james', 'noria', 'jamesnoria@gmail.com', 'jamesnoria')
james.describe_user()
james.privileges.privileges=['can do whatever He wants']
james.privileges.show_privileges()