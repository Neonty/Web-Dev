from models import Software, UnrealEngine, Blender, FLStudio


def main():
    software = Software("GenericApp", "1.0", "Unknown Dev")
    unreal = UnrealEngine("5.3", "Epic Games", "DirectX 12")
    blender = Blender("4.0", "Blender Foundation", "Cycles")
    flstudio = FLStudio("21", "Image-Line", 120)

    apps = [software, unreal, blender, flstudio]

    for app in apps:
        print(app)
        print(app.get_info())
        print(app.run())
        print("-" * 40)

    print(unreal.build_game())
    print(blender.render())
    print(flstudio.make_music())

if __name__ == "__main__":
    main()