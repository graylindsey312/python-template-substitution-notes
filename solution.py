from string import Template

def solve(value):
    return Template(value["template"]).substitute(value["values"])
