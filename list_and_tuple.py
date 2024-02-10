planets = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
]

print(planets)
print(planets[0])
print(planets[-1])
print(planets[0:3])
print(planets[:3])
print(planets[3:])
print(planets[1:-1])
print(planets[-3:])
print(planets[1:-1:2])
print(planets[::-1])
print(planets[::2])
print(planets.index("Earth"))

planets[2] = "Home"

print(planets)
print(len(planets))

dwarf_planets = ["Pluto", "Ceres", "Eris", "Makemake", "Haumea"]

print(planets + dwarf_planets)

for planet in planets:
    print(planet)


for i, planet in enumerate(planets):
    print(f"Planet {i} : {planet}")


planets[2] = "Earth"

planet_nicknames = {
    "Mercury": "The Swift Planet",
    "Venus": "The Evening Star",
    "Earth": "The Blue Planet",
    "Mars": "The Red Planet",
    "Jupiter": "The Gas Giant",
    "Saturn": "The Ringed Planet",
    "Uranus": "The Sideways Planet",
    "Neptune": "The Windy Planet",
}
nicknames = [planet_nicknames[planet] for planet in planets]


print(planet_nicknames)
print(nicknames)

for planet, nickname in zip(planets, nicknames):
    print(f"{planet} : {nickname}")


print("Pluto" in planets)
print("Pluto" in dwarf_planets)

merc, *others, Nep = planets

print(merc)
print(others)
print(Nep)

print(planets)
planets.append("Pluto")
print(planets)

planets.pop()
print(planets)
planets.pop(2)
print(planets)

planets.insert(7, "Pluto")
print(planets)

planets.insert(2, "Earth")
print(planets)

planets.remove("Pluto")
print(planets)


del planets[7]
print(planets)

del planets[2]
print(planets)

del planets[1:3]
print(planets)


planets = planets[0:1] + ["Venus", "Earth", "Mars"] + planets[1:] + ["Neptune"]
print(planets)


InternationalAstronomicalUnionPlanets = tuple(planets)
print(InternationalAstronomicalUnionPlanets)

print(InternationalAstronomicalUnionPlanets[0])
print(InternationalAstronomicalUnionPlanets[-1])
print(InternationalAstronomicalUnionPlanets[0:3])
print(InternationalAstronomicalUnionPlanets[:3])
print(InternationalAstronomicalUnionPlanets[3:])
print(InternationalAstronomicalUnionPlanets[1:-1])
print(InternationalAstronomicalUnionPlanets[-3:])
print(InternationalAstronomicalUnionPlanets[1:-1:2])
print(InternationalAstronomicalUnionPlanets[::-1])
print(InternationalAstronomicalUnionPlanets[::2])
print(InternationalAstronomicalUnionPlanets.index("Earth"))
