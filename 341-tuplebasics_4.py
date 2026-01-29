from collections import namedtuple

Color = namedtuple("Color", ["name", "R", "G", "B"])

color_name = input()
red_channel = int(input())
green_channel = int(input())
blue_channel = int(input())

#""" Your code goes here """
#Color is a named tuple with fields: name, R, G, and B. Create color_data as a Color tuple, and initialize color_data with color_name, red_channel, green_channel, and blue_channel as the fields.
color_data = Color(color_name, red_channel, green_channel, blue_channel)

print(f"Color name: {color_data.name}, R: {color_data.R}, G: {color_data.G}, B: {color_data.B}")
