# Cyclomatic complexity calculation
# Given: E = 17 edges, N = 13 nodes, P = 1 (connected graph), predicate nodes = 5

E, N, P = 17, 13, 1
vg_formula = E - N + 2 * P
vg_predicate = 5 + 1  # predicate nodes + 1

print("V(G) using E - N + 2P =", vg_formula)
print("V(G) using predicate nodes + 1 =", vg_predicate)
