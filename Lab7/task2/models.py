class Software:
    def __init__(self, name, version, developer):
        self.name = name
        self.version = version
        self.developer = developer

    def run(self):
        return f"{self.name} is running..."

    def get_info(self):
        return f"{self.name} (v{self.version}) by {self.developer}"

    def __str__(self):
        return f"Software(Name: {self.name}, Version: {self.version}, Developer: {self.developer})"


class UnrealEngine(Software):
    def __init__(self, version, developer, graphics_api):
        super().__init__("Unreal Engine", version, developer)
        self.graphics_api = graphics_api

    def run(self):
        return "Launching Unreal Engine with high-end graphics..."

    def build_game(self):
        return "Building a 3D game project..."

    def __str__(self):
        return f"UnrealEngine(Version: {self.version}, API: {self.graphics_api}, Developer: {self.developer})"


class Blender(Software):
    def __init__(self, version, developer, render_engine):
        super().__init__("Blender", version, developer)
        self.render_engine = render_engine

    def run(self):
        return "Opening Blender for 3D modeling..."

    def render(self):
        return f"Rendering using {self.render_engine} engine..."

    def __str__(self):
        return f"Blender(Version: {self.version}, Render: {self.render_engine}, Developer: {self.developer})"


class FLStudio(Software):
    def __init__(self, version, developer, bpm):
        super().__init__("FL Studio", version, developer)
        self.bpm = bpm

    def run(self):
        return "Launching FL Studio for music production..."

    def make_music(self):
        return f"Producing music at {self.bpm} BPM..."

    def __str__(self):
        return f"FLStudio(Version: {self.version}, BPM: {self.bpm}, Developer: {self.developer})"