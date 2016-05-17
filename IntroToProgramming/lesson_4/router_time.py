
round_trip = 0.075 #s
distance = 5000000.0 #m
speed_of_light = 200000000.0 #m/s

# d = vt
# d/v = t

print distance / speed_of_light
print round_trip - (distance / speed_of_light)

