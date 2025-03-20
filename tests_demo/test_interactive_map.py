# %%
from python_workflow_demo.scripts.interactive_map import make_interactive_map
from python_workflow_demo.scripts.project import Project


def test_interactive_map():
    p = Project(r"D:\github\wvangerwen\demo_data")
    gdf = p.input.panden.load().head()
    output_path = p.output.interactive_map.path
    make_interactive_map(gdf, output_path)

    assert output_path.exists()


def test_true():
    assert True
