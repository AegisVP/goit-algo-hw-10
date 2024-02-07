import pulp as plp

prob = plp.LpProblem("Компанія", plp.LpMaximize)

x1 = plp.LpVariable("Лимонад", 0, None, plp.LpInteger)
x2 = plp.LpVariable("Фруктовий сік", 0, None, plp.LpInteger)

prob += x1 + x2
prob += 2 * x1 + x2 <= 100, 'Вода'
prob += x1 <= 50, 'Цукор'
prob += x1 <= 30, 'Лимонний сік'
prob += 2 * x2 <= 40, 'Фруктове пюре'

prob.solve()

print(f"Status: {plp.LpStatus[prob.status]}")
print("Result:")
print(f"   Лимонад = {plp.value(x1):.0f} од.")
print(f"   Фруктовий сік = {plp.value(x2):.0f} од.")
