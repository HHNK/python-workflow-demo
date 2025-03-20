# %% Code test
import geopandas as gpd
import hhnk_research_tools as hrt
from project import Project


def test_interactive_map(p):
    gdf = p.input.panden.load()
    datacolumn = "bouwjaar"
    colormap_name = "viridis"
    colormap_steps = None
    output_path = p.output.interactive_map.path
    title = "Interactive map test"
    legend_label = "Testlabels"
    tooltip_columns = ["gid", "bouwjaar"]
    tooltip_aliases = ["gid", "bouwjaar"]
    quantiles = [0, 0.1, 0.5, 0.8, 1]

    # quantiles = np.arange(0, 1.1, 0.1)

    v = hrt.create_interactive_map(
        gdf=gdf,
        datacolumn=datacolumn,
        output_path=output_path,
        title=title,
        legend_label=legend_label,
        tooltip_columns=tooltip_columns,
        tooltip_aliases=tooltip_aliases,
        colormap_name=colormap_name,
        colormap_steps=colormap_steps,
        quantiles=quantiles,
    )

    assert output_path.exists()


# %%
if __name__ == "__main__":
    p = Project(r"D:\github\wvangerwen\demo_data")
    test_interactive_map(p)

    # Open in browser
    import webbrowser

    webbrowser.open(p.output.interactive_map.path)
