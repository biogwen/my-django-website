
def logic(maturity, team, company, sprint):

    if maturity == 1 or team <= 3 or company < 5:
        methodo = "Kanban"

    elif sprint < 5:
        methodo = "Lean Startup"

    elif team > 12:
        methodo = "Nexus"

    else:
        methodo = "Scrum"

    return methodo

