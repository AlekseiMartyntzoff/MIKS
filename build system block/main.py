# -*- coding: utf-8 -*-

from ComputerBuilder import ComputerBuilder

builder = ComputerBuilder()
builder.motherboard = "ASUS"
builder.processor = "Intel Core i9"
builder.memory = "32GB DDR4"
builder.storage = "1TB SSD"
builder.graphics_card = "AMD Radeon 640X"
builder.sound_card = "Realtek HD Audio"
builder.dvd_drive = "LG DVD-RW"

computer = builder.build()
print(computer)
