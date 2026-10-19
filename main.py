from pyscript import document

grade_7 = {"Alice Blue", "Anita Bath"}
grade_8 = {"Ella Vator", "Francisco Portero"}
grade_9 = {"Juanito Lakarin", "Justin Case"}
grade_10 = {"Paige Turner", "Restituto Fruto"}

def add_member(event=None):
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    
    new_member_name = f"{first_name} {last_name}".strip()
    
    master_set = (grade_7 | grade_8 | grade_9 | grade_10 | {new_member_name}) - {""}

    members_list_html = "<br>".join(sorted(master_set))
    total_count = len(master_set)

    output_html = f"<strong>All members:</strong><br>{members_list_html}<br><br><strong>Total members: {total_count}</strong>"

    document.getElementById("output").innerHTML = output_html

add_member()