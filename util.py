import re

def string_obj(obj, st):
    """string formating stuff """
    start = st.find("{{")
    end = st.find("}}")
    st = st[0:start] + getattr(obj, st[start+2:end]) + st[end+2:]
    if st.find("{{", end+2) == -1:
        return st
    else:
        return string_obj(obj, st)


def make_form(arr):
    ret = """
<table>
"""    
    for i in arr:
        ret += """
<tr>
    <td>""" + i[0] + """<td>
    <td><input type="text" name=\""""+ i[1] +"""\"></td>
</tr>
"""
    ret += "</table>"
    return ret



"""
class T:
    a = "4"
    b = "5"

t = T()

print stringObj(t,"i have {{a}} time {{b}}")  
"""        

    
