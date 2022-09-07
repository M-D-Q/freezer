#!/usr/bin/python3
import cgi

print("Content-Type: text/html")
print("")

form = cgi.FieldStorage()
f_name=form["f_name"].value
s_name=form["s_name"].value

print(f"Welcome {f_name} !\n")
#print("<br><b>First Name</b>",f_name)
#print("<br><b>Second Name</b>",s_name)
#print("<br><br><br><a href=form.htm>Back to Form</a>")