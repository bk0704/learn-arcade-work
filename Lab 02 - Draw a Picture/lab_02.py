# A program to practice drawing with arcade
# In this program I will draw the palestinian flag
from typing import List

import arcade

# Open up a window
arcade.open_window(800, 400, "Palestine")

# set the background colour to white
arcade.set_background_color(arcade.color.WHITE)

# Start rendering the drawings
arcade.start_render()

# Draw a green rectangle
arcade.draw_lrbt_rectangle_filled(0, 800, 0, 133, (0, 151, 54))

# Draw a black triangle
arcade.draw_lrbt_rectangle_filled(0, 800, 266, 400, arcade.color.BLACK)

# Draw a red triangle
arcade.draw_triangle_filled(0, 0, 0, 400, 267, 200, (238, 42, 53))

# Finish rendering the drawings
arcade.finish_render()

# Keep the window open until the user closes it
arcade.run()
