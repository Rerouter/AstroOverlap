# /*
#  * Start time: 2022-05-28T01:54:36.131Z UTC
#  * Execution time: 02:18:58.1
#  */
# var P = new Script;
# P.filePath = "$PXI_SRCDIR/scripts/AdP/MosaicByCoordinates.js";
# P.md5sum = "760e36a3d669cd89f0e1d2183f5064ba";
# P.parameters = [ // id, value
#    ["engine_files", "D:/Laptop Offload/Carina/Edited/2022-05-01_23-38-25__-10.00_120.00s_0005_d_WCS.00_120.00s_0005_d_20220514222841.xisf|D:/Laptop Offload/Carina/Edited/2022-05-01_23-44-00__-10.00_120.00s_0006_d_WCS.00_120.00s_0006_d_20220514222952.xisf|D:/Laptop Offload/Carina/Edited/2022-05-01_23-46-17__-10.00_120.00s_0007_d_WCS.00_120.00s_0007_d_20220514223103.xisf|D:/Laptop Offload/Carina/Edited/2022-05-01_23-48-21__-10.00_120.00s_0008_d_WCS.00_120.00s_0008_d_20220514223212.xisf|D:/Laptop Offload/Carina/Edited/2022-05-01_23-50-25__-10.00_120.00s_0009_d_WCS.00_120.00s_0009_d_20220514223321.xisf|D:/Laptop Offload/Carina/Edited/2022-05-01_23-53-45__-10.00_120.00s_0005_d_WCS.00_120.00s_0005_d_20220514223440.xisf|D:/Laptop Offload/Carina/Edited/2022-05-01_23-55-48__-10.00_120.00s_0006_d_WCS.00_120.00s_0006_d_20220514223556.xisf|D:/Laptop Offload/Carina/Edited/2022-05-01_23-57-53__-10.00_120.00s_0007_d_WCS.00_120.00s_0007_d_20220514223713.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-00-17__-10.00_120.00s_0008_d_WCS.00_120.00s_0008_d_20220514223829.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-02-21__-10.00_120.00s_0009_d_WCS.00_120.00s_0009_d_20220514223944.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-05-12__-10.00_120.00s_0000_d_WCS.00_120.00s_0000_d_20220514224105.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-07-36__-10.00_120.00s_0001_d_WCS.00_120.00s_0001_d_20220514224227.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-09-40__-10.00_120.00s_0002_d_WCS.00_120.00s_0002_d_20220514224349.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-11-44__-10.00_120.00s_0003_d_WCS.00_120.00s_0003_d_20220514224511.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-14-05__-10.00_120.00s_0004_d_WCS.00_120.00s_0004_d_20220514224625.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-16-54__-10.00_120.00s_0000_d_WCS.00_120.00s_0000_d_20220514224746.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-18-58__-10.00_120.00s_0001_d_WCS.00_120.00s_0001_d_20220514224904.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-21-32__-10.00_120.00s_0002_d_WCS.00_120.00s_0002_d_20220514225018.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-23-36__-10.00_120.00s_0003_d_WCS.00_120.00s_0003_d_20220514225136.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-25-40__-10.00_120.00s_0004_d_WCS.00_120.00s_0004_d_20220514225253.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-28-50__-10.00_120.00s_0000_d_WCS.00_120.00s_0000_d_20220514225418.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-30-54__-10.00_120.00s_0001_d_WCS.00_120.00s_0001_d_20220514225535.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-32-58__-10.00_120.00s_0002_d_WCS.00_120.00s_0002_d_20220514225651.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-35-34__-10.00_120.00s_0003_d_WCS.00_120.00s_0003_d_20220514225809.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-37-38__-10.00_120.00s_0004_d_WCS.00_120.00s_0004_d_20220514225927.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-40-26__-10.00_120.00s_0000_d_WCS.00_120.00s_0000_d_20220514230058.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-42-53__-10.00_120.00s_0001_d_WCS.00_120.00s_0001_d_20220514230226.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-44-56__-10.00_120.00s_0002_d_WCS.00_120.00s_0002_d_20220514230349.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-47-00__-10.00_120.00s_0003_d_WCS.00_120.00s_0003_d_20220514230514.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-49-37__-10.00_120.00s_0004_d_WCS.00_120.00s_0004_d_20220514230640.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-54-31__-10.00_120.00s_0001_d_WCS.00_120.00s_0001_d_20220514230807.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-56-55__-10.00_120.00s_0002_d_WCS.00_120.00s_0002_d_20220514230924.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_00-59-00__-10.00_120.00s_0003_d_WCS.00_120.00s_0003_d_20220514231051.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-01-03__-10.00_120.00s_0004_d_WCS.00_120.00s_0004_d_20220514231212.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-04-08__-10.00_120.00s_0000_d_WCS.00_120.00s_0000_d_20220514231334.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-06-12__-10.00_120.00s_0001_d_WCS.00_120.00s_0001_d_20220514231453.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-08-16__-10.00_120.00s_0002_d_WCS.00_120.00s_0002_d_20220514231610.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-10-35__-9.90_120.00s_0003_d_WCS.90_120.00s_0003_d_20220514231727.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-12-38__-10.00_120.00s_0004_d_WCS.00_120.00s_0004_d_20220514231845.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-18-07__-10.00_120.00s_0011_d_WCS.00_120.00s_0011_d_20220514231958.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-20-11__-10.00_120.00s_0012_d_WCS.00_120.00s_0012_d_20220514232110.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-22-14__-10.00_120.00s_0013_d_WCS.00_120.00s_0013_d_20220514232220.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-24-36__-10.00_120.00s_0014_d_WCS.00_120.00s_0014_d_20220514232334.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-29-28__-10.00_120.00s_0011_d_WCS.00_120.00s_0011_d_20220514232454.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-31-52__-10.00_120.00s_0012_d_WCS.00_120.00s_0012_d_20220514232611.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-33-56__-9.90_120.00s_0013_d_WCS.90_120.00s_0013_d_20220514232729.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-35-59__-10.00_120.00s_0014_d_WCS.00_120.00s_0014_d_20220514232848.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-41-21__-10.00_120.00s_0006_d_WCS.00_120.00s_0006_d_20220514233013.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-43-25__-10.00_120.00s_0007_d_WCS.00_120.00s_0007_d_20220514233137.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-45-47__-10.00_120.00s_0008_d_WCS.00_120.00s_0008_d_20220514233258.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-47-51__-10.00_120.00s_0009_d_WCS.00_120.00s_0009_d_20220514233420.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-51-08__-10.00_120.00s_0005_d_WCS.00_120.00s_0005_d_20220514233541.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-53-44__-10.00_120.00s_0006_d_WCS.00_120.00s_0006_d_20220514233655.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-55-48__-10.00_120.00s_0007_d_WCS.00_120.00s_0007_d_20220514233808.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_01-57-52__-10.00_120.00s_0008_d_WCS.00_120.00s_0008_d_20220514233923.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_02-00-25__-10.00_120.00s_0009_d_WCS.00_120.00s_0009_d_20220514234037.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_02-03-13__-10.00_120.00s_0005_d_WCS.00_120.00s_0005_d_20220514234154.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_02-07-58__-10.00_120.00s_0007_d_WCS.00_120.00s_0007_d_20220514234316.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_02-10-01__-10.00_120.00s_0008_d_WCS.00_120.00s_0008_d_20220514234442.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_02-12-05__-9.90_120.00s_0009_d_WCS.90_120.00s_0009_d_20220514234602.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_22-10-47__-9.90_15.00s_0000_d_WCS.90_15.00s_0000_d_20220514234722.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_22-22-14__-10.00_15.00s_0000_d_WCS.00_15.00s_0000_d_20220514234842.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_22-35-32__-9.90_15.00s_0000_d_WCS.90_15.00s_0000_d_20220514235009.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_22-46-59__-9.90_15.00s_0000_d_WCS.90_15.00s_0000_d_20220514235130.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_22-58-29__-10.00_15.00s_0000_d_WCS.00_15.00s_0000_d_20220514235251.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_22_48_26__10_00_600_00s_0000_d_WCS_00_600_00s_0000_d_ABE.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_22_59_57__10_00_600_00s_0000_d_WCS_00_600_00s_0000_d_ABE.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_23-10-01__-10.00_15.00s_0000_d_WCS.00_15.00s_0000_d_20220514235418.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_23-21-26__-9.90_15.00s_0000_d_WCS.90_15.00s_0000_d_20220514235530.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_23-44-27__-10.00_15.00s_0000_d_WCS.00_15.00s_0000_d_20220515000002.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_23-57-01__-10.00_15.00s_0000_d_WCS.00_15.00s_0000_d_20220515000115.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_23_11_23__10_00_600_00s_0000_d_WCS_00_600_00s_0000_d_ABE.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_23_22_53__10_00_600_00s_0000_d_WCS_00_600_00s_0000_d_ABE.xisf|D:/Laptop Offload/Carina/Edited/2022-05-02_23_58_34__10_00_600_00s_0000_d_WCS_00_600_00s_0000_d_ABE.xisf|D:/Laptop Offload/Carina/Edited/2022-05-03_00_10_09__10_00_600_00s_0000_d_WCS_00_600_00s_0000_d_ABE.xisf"],
#    ["engine_centerCoordsAuto", "false"],
#    ["engine_centerRA", "160.47825833333334"],
#    ["engine_centerDec", "-59.888466666666666"],
#    ["engine_resolutionAuto", "false"],
#    ["engine_resolution", "0.00012849583333333334"],
#    ["engine_rotationAuto", "false"],
#    ["engine_rotation", "-90"],
#    ["engine_projectionAuto", "false"],
#    ["engine_projection", "0"], // row 10
#    ["engine_projectionOriginMode", "0"],
#    ["engine_projectionOriginRA", "160"],
#    ["engine_projectionOriginDec", "-59"],
#    ["engine_dimensionsAuto", "false"],
#    ["engine_width", "42624"],
#    ["engine_height", "36770"],
#    ["engine_qualityHQ", "true"],
#    ["engine_pixelInterpolation", "8"],
#    ["engine_clampingThreshold", "0.3"],
#    ["engine_suffix", "_registered"], // row 20
#    ["engine_overwrite", "false"],
#    ["engine_errorPolicy", "2"],
#    ["engine_outputDir", "G:/Reprojected"],
#    ["isGlobalTarget", "true"],
#    ["isViewTarget", "false"]
# ];
