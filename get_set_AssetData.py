import unreal_engine as ue
from pprint import pprint
ass = ue.get_selected_assets()[0]
""" Asset Properties:
    SourceModels
    SectionInfoMap
    OriginalSectionInfoMap
    LODGroup
    bAutoComputeLODScreenSize
    ImportVersion
    MaterialRemapIndexPerImportVersion
    LightmapUVVersion
    MinLOD
    Materials
    StaticMaterials
    LightmapUVDensity
    LightMapResolution
    LightMapCoordinateIndex
    DistanceFieldSelfShadowBias
    bGenerateMeshDistanceField
    BodySetup
    LODForCollision
    bStripComplexCollisionForConsole
    bHasNavigationData
    bSupportUniformlyDistributedSampling
    LpvBiasMultiplier
    bAllowCPUAccess
    AssetImportData
    SourceFilePath
    SourceFileTimestamp
    ThumbnailInfo
    EditorCameraPosition
    bCustomizedCollision
    Sockets
    PositiveBoundsExtension
    NegativeBoundsExtension
    ExtendedBounds
    ElementToIgnoreForTexFactor
    AssetUserData
    NavCollision"""

# get custom LOD
custLODs = ass.SourceModels
lod0 = custLODs[0].get_struct()
"""LOD Properties:
    BuildSettings
    ReductionSettings
    LODDistance
    ScreenSize"""

# get lod buildsetting
lod0buildSetting = lod0.BuildSettings.get_struct()
"""Build Setting Properties:
    bUseMikkTSpace
    bRecomputeNormals
    bRecomputeTangents
    bRemoveDegenerates
    bBuildAdjacencyBuffer
    bBuildReversedIndexBuffer
    bUseHighPrecisionTangentBasis
    bUseFullPrecisionUVs
    bGenerateLightmapUVs
    bGenerateDistanceFieldAsIfTwoSided
    MinLightmapResolution
    SrcLightmapIndex
    DstLightmapIndex
    BuildScale
    BuildScale3D
    DistanceFieldResolutionScale
    DistanceFieldBias
    DistanceFieldReplacementMesh"""