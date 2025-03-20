# %%
import hhnk_research_tools as hrt


class Project(hrt.Folder):
    def __init__(self, base):
        super().__init__(base, create=False)

        self.input = inputDir(self.base, "input")  # Vullingsgraad\Input
        self.output = outputDir(self.base, "output")  # Vullingsgraad\Input


class inputDir(hrt.Folder):
    """Input directory"""

    def __init__(self, base, name):
        super().__init__(base, name)

        self.add_file("dem", "dem.tif")


class outputDir(hrt.Folder):
    """Input directory"""

    def __init__(self, base, name):
        super().__init__(base, name)

        self.add_file("dem", "dem.tif")
