#!/usr/bin/python3
print("Content-Type: text/html")
print("")

print("""<form name=f1 method=post action=form-submit.cgi>
<table>
<tr><td>First Name </td><td><input type=text name=f_name><td></tr>
<tr><td>Second Name</td><td> <input type=text name=s_name></td></tr>
 <tr><td><input type=submit value=Submit></td><td> </td></tr>
</table>
</form>""")


