import gurobipy as grb


def aufgabe_1_1():
    m = grb.Model()

    x = m.addVars(range(2), lb=.0, name="x")

    m.addConstr(x[0] <= 6)
    m.addConstr(.25 * x[0] + x[1] <= 6)
    m.addConstr(3 * x[0] + 2 * x[1] <= 22)

    m.setObjective(5 * x[0] + 4 * x[1], grb.GRB.MAXIMIZE)

    m.optimize()

    print("Produziere {} Fässer Speiseeis und {} kg Butter.".format(x[0].x, x[1].x))


def aufgabe_1_2():
    m = grb.Model()

    p = m.addVars(range(4), vtype=grb.GRB.BINARY, name="x")

    m.addConstr(12 * p[0] + 10 * p[1] + 5 * p[2] + 8 * p[3] <= 20)

    m.setObjective(3 * p[0] + 5 * p[1] + 4 * p[2] + 2 * p[3], grb.GRB.MAXIMIZE)

    m.optimize()

    for i in range(4):
        if p[i].x > .5:
            print("Projekt {} wird gefördert.")
        else:
            print("Projekt {} wird nicht gefördert.")


def aufgabe_1_3():
    m = grb.Model()

    x = m.addVars({1.5, 2}, range(380), vtype=grb.GRB.INTEGER, name="x")

    m.addConstr(2 * sum(x[2, l] for l in range(380)) == sum(x[1.5, l] for l in range(380)))
    m.addConstrs(1.5 * x[1.5, l] + 2 * x[2, l] <= 6.5 for l in range(300))
    m.addConstrs(1.5 * x[1.5, l] + 2 * x[2, l] <= 5.5 for l in range(300, 380))

    m.setObjective(sum(x[2, l] for l in range(380)), grb.GRB.MAXIMIZE)

    m.optimize()

    for l in range(380):
        print("Schneide aus Leiste {} {} Leisten der Länge 1.5m "
              "und {} Leisten der Länge 2m.".format(l, x[1.5, l].x, x[2, l].x))


def aufgabe_1_4():
    m = grb.Model

    standorte = range(5)
    werkzeuge = range(5)

    d = [[0, 2, 4, 3, 5]]

    pass


if __name__ == "__main__":
    aufgabe_1_1()
