# -*- coding: utf-8 -*-

from equalizer_preset import EqualizerPreset
from preset_manager import PresetManager


if __name__ == "__main__":
    # Creation of various presets
    rock_preset: EqualizerPreset = EqualizerPreset(
        name="Rock Preset",
        genre="Rock", 
        bands=[5, 7, 6, 8, 5, 4, 3, 2, 1, 0, 0, 0]
    )

    jazz_preset: EqualizerPreset = EqualizerPreset(
        name="Jazz Preset", 
        genre="Jazz", 
        bands=[3, 4, 4, 5, 6, 7, 7, 6, 5, 4, 3, 2]
    )

    classical_preset: EqualizerPreset = EqualizerPreset(
        name="Classical Preset", 
        genre="Classical", 
        bands=[2, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 1]
    )

    print("--Initial Presets--")
    print(rock_preset)
    print(jazz_preset)
    print(classical_preset)

    # Creating a manager for storing states
    manager = PresetManager()
    manager.save(rock_preset)  # Saving the initial state of the Rock Preset
    manager.save(jazz_preset)  # Saving the initial state of the Jazz Preset
    manager.save(classical_preset)  # Saving the initial state of the Classical Preset

    # Changing presets
    rock_preset.set_preset([3, 3, 4, 5, 6, 7, 7, 6, 5, 4, 3, 2])
    jazz_preset.set_preset([4, 5, 5, 6, 7, 8, 8, 7, 6, 5, 4, 3])
    classical_preset.set_preset([1, 1, 2, 3, 4, 4, 4, 3, 2, 1, 0, 0])

    print("\n--Modified Presets--")
    print(rock_preset)
    print(jazz_preset)
    print(classical_preset)

    # Restoring the initial state of the presets
    manager.restore(preset=rock_preset, index=0)
    manager.restore(preset=jazz_preset, index=1)
    manager.restore(preset=classical_preset, index=2)

    print("\n--Restored Presets--")
    print(rock_preset)
    print(jazz_preset)
    print(classical_preset)
