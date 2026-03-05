from collections import namedtuple
Color = namedtuple ("Color", ["name", "R", "G", "B"])
color_name = input()
red_channel = int(input())
green_channel = int(input())
blue_channel = int(input())

color1 = Color(color_name, red_channel, green_channel, blue_channel)

print(f"Color name: {color1.name}, R: {color1.R}, G: {color1.G}, B: {color1.B}")

