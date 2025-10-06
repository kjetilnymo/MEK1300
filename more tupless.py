"""

def q_and_r(x, y):
    q = x // y
    r = x % y

    return (q, r)


(q, r) = (q_and_r(10,7))
          
print("q =", q)
print("r =", r)

def get_min_max(numbers):
    return (min(numbers), max(numbers))

nums =[2, 1, 7, 8, 2]

(low, high) = get_min_max

print(low, high)

#kode ikke ferdig

"""
#Each player has fixed info (Number, Name, position)

team = [
    (7, "Ronaldo", "Forward", [2, 1, 0, 3])
    (10, "Messi", "Forward", [4, 1, 2, 2])
    (1, "Neuer", "GK", [0, 0, 0, 1])
    (11, "Salah", "Forward", [2, 3, 2, 3])
    ]

print("=== Team performance ===")

for player in team:
    player_id = player(0)
    name = player[1]
    position = player[2]
    goals = player[3]

    total_goals = sum(goals)
    print(f"{name} ({position}) scored {total_goals} goal(s) in total.")