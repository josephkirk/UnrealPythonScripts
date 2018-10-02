import unreal_engine as ue

StaticMesh, Materials, Textures = "StaticMesh", "Materials", "Textures"
def export_selected_asset(savePath=None):
    uasset = ue.get_selected_assets()
    savePath = ue.open_directory_dialog("")
    if not savePath:
        savePath = ue.open_directory_dialog("")
    if savePath:
        ue.export_assets(staticMeshes, savePath)

def export_assets_by_class(className, filterPath=["Game"], savePath=None):
    staticMeshes = [o for o in ue.get_assets_by_class(className)
        if all((filterName in o.get_path_name() for filterName in filterPath))]
    if not savePath:
        savePath = ue.open_directory_dialog("")
    if savePath:
        ue.export_assets(staticMeshes, savePath)

export_assets_by_class(StaticMesh, filterPath=["SharedModel", "Content", "Art"], savePath=r"\\vietsap002\projects\R6\04_WIP\tools\perforce\proxyCheck")