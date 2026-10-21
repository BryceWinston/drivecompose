# 75 篇文献接入与实验迁入记录

后续更新：英文实验三张来源图已补入；当前 PDF 和渲染核对以 [图片修复记录](experiment-figure-fix-20261021.md) 为准，下方保留文献接入时的编译记录。

日期：2026-10-21。输入为 `docs/DriveCompose_75篇顶会参考文献.docx`。

75 条输入文献全部并入当前书目。其中 9 条与原 18 条书目重复，沿用原键并更新元数据；新增 66 条，保留文档之外的 9 条项目近邻工作，共 84 条。所有 75 条均在中英文正文中实际引用，未使用 `nocite` 批量挂列。

引用安排：Waymo 与 nuScenes 放在引言的驾驶数据背景；ViT 与 Attention 放在方法的图像编码段；DiT 和 Flow Matching 保留在条件生成段。其余按辐射表示、城市场景与控制、通用前馈重建、驾驶推断、规范资产、生成式补全和可控视频生成组织在相关工作中。两个 HUGS 按“人体”与“城市场景”区分。TokenGS 明确作为像素解耦的既有工作，本文差异仍是可组合规范潜变量上的条件生成与持久复用。

书目以官方 BibTeX、官方 HTML 元数据及原 DOCX 为依据。69 条通过原链接直接确认题名；6 条因浏览器验证、403 或连接失败，转用作者 arXiv、作者项目页或官方会议索引核对。来源、提取方式和每条引用位置详见同名 JSON。原 STORM 作者顺序按正式 ICLR 记录更新；Flow Matching 更新为 ICLR 2023，保留旧引用键以免破坏外部实验文件。官方 BibTeX 缺失的页码等字段由已提供的 DOCX 补齐。本轮没有重新核验各论文的实验结果。

用户明确暂不限制篇幅，因此保留完整引言和方法，不以缩字、压行距或删技术细节满足页数。中英文新增引用与论述逐段对应，并做了自然表达检查；原有公式与方法数值不变。

## 实验来源

实验以 `E:/Users/changan/Downloads/edge/MOSAIC__Motion_Aware_Multi_Object_Feed_Forward_4D_Reconstruction_for_Driving_Scenes` 为准，仅复制 `sec/4_experiments.tex` 和 `zh/4_experiments_zh.tex`。复制后与该目录逐字节一致。三张实验依赖图也与来源一致，无需替换。此次指定目录的内容恰好与复制前相同，所以 Git 不会显示实验内容差异。

中英文实验各自保留来源版本，由后续实验负责人修改，本轮不改协议、数值、旧名称或图表。两份来源文件并不是互译稿，验收条件是与指定来源一致。详见 `experiment-import-20261021.json`。

## Git 状态

此前的 `a2cdacc` 已在用户中断命令前完成提交和推送。本轮以该提交为基线，全部新修改保留在工作区，等待用户确认后再提交或推送；没有重写远程历史。

本轮备份、下载缓存和临时渲染位于项目外 `pre-research/_archive/drivecompose/20261021-reference-integration/`。当前 PDF 入口仍是 `paper/build/en/main.pdf` 与 `paper/build/zh/main_zh.pdf`。

## 逐条引用位置

下表沿用 DOCX 原编号；正式论文中的编号由 BibTeX 排序自动生成。中文对应段落使用相同引用键。

| DOCX 编号 | BibTeX 键 | 文献 | 英文引用位置 | 核对来源 |
| --- | --- | --- | --- | --- |
| 1 | `barron2021mipnerf` | Mip-NeRF: A Multiscale Representation for Anti-Aliasing Neural Radiance Fields | sec/2_related_work.tex:5 | [来源](https://openaccess.thecvf.com/content/ICCV2021/html/Barron_Mip-NeRF_A_Multiscale_Representation_for_Anti-Aliasing_Neural_Radiance_Fields_ICCV_2021_paper.html) |
| 2 | `black2023bedlam` | BEDLAM: A Synthetic Dataset of Bodies Exhibiting Detailed Lifelike Animated Motion | sec/2_related_work.tex:17 | [来源](https://openaccess.thecvf.com/content/CVPR2023/html/Black_BEDLAM_A_Synthetic_Dataset_of_Bodies_Exhibiting_Detailed_Lifelike_Animated_CVPR_2023_paper.html) |
| 3 | `caesar2020nuscenes` | nuScenes: A Multimodal Dataset for Autonomous Driving | sec/1_introduction.tex:4 | [来源](https://openaccess.thecvf.com/content_CVPR_2020/html/Caesar_nuScenes_A_Multimodal_Dataset_for_Autonomous_Driving_CVPR_2020_paper.html) |
| 4 | `charatan2024pixelsplat` | pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction | sec/2_related_work.tex:11 | [来源](https://openaccess.thecvf.com/content/CVPR2024/html/Charatan_pixelSplat_3D_Gaussian_Splats_from_Image_Pairs_for_Scalable_Generalizable_CVPR_2024_paper.html) |
| 5 | `chen2025dggt` | DGGT: Feedforward 4D Reconstruction of Dynamic Driving Scenes using Unposed Images | sec/1_introduction.tex:6；sec/2_related_work.tex:14；sec/4_experiments.tex:19 | [来源](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_DGGT_Feedforward_4D_Reconstruction_of_Dynamic_Driving_Scenes_using_Unposed_CVPR_2026_paper.html) |
| 6 | `chen2024mvsplat` | MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images | sec/2_related_work.tex:11 | [来源](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3187_ECCV_2024_paper.php) |
| 7 | `chen2025omnire` | OmniRe: Omni Urban Scene Reconstruction | sec/1_introduction.tex:8；sec/2_related_work.tex:8 | [来源](https://proceedings.iclr.cc/paper_files/paper/3018-/bibtex) |
| 8 | `deitke2023objaverse` | Objaverse: A Universe of Annotated 3D Objects | sec/2_related_work.tex:20 | [来源](https://openaccess.thecvf.com/content/CVPR2023/html/Deitke_Objaverse_A_Universe_of_Annotated_3D_Objects_CVPR_2023_paper.html) |
| 9 | `dosovitskiy2021vit` | An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale | sec/3_method.tex:36 | [来源](https://arxiv.org/abs/2010.11929) |
| 10 | `gao2024cat3d` | CAT3D: Create Anything in 3D with Multi-View Diffusion Models | sec/2_related_work.tex:20 | [来源](https://proceedings.neurips.cc/paper_files/paper/2024/hash/89e4433fec4b99f1d859db57af1e0a0f-Abstract-Conference.html) |
| 11 | `gao2024magicdrive` | MagicDrive: Street View Generation with Diverse 3D Geometry Control | sec/2_related_work.tex:23 | [来源](https://proceedings.iclr.cc/paper_files/paper/5297-/bibtex) |
| 12 | `gao2025magicdrivev2` | MagicDrive-V2: High-Resolution Long Video Generation for Autonomous Driving with Adaptive Control | sec/2_related_work.tex:23 | [来源](https://openaccess.thecvf.com/content/ICCV2025/html/Gao_MagicDrive-V2_High-Resolution_Long_Video_Generation_for_Autonomous_Driving_with_Adaptive_ICCV_2025_paper.html) |
| 13 | `gao2024vista` | Vista: A Generalizable Driving World Model with High Fidelity and Versatile Controllability | sec/2_related_work.tex:23 | [来源](https://proceedings.neurips.cc/paper_files/paper/27221-/bibtex) |
| 14 | `goel2023humans4d` | Humans in 4D: Reconstructing and Tracking Humans with Transformers | sec/2_related_work.tex:17 | [来源](https://openaccess.thecvf.com/content/ICCV2023/html/Goel_Humans_in_4D_Reconstructing_and_Tracking_Humans_with_Transformers_ICCV_2023_paper.html) |
| 15 | `guo2023vid2avatar` | Vid2Avatar: 3D Avatar Reconstruction From Videos in the Wild via Self-Supervised Scene Decomposition | sec/2_related_work.tex:17 | [来源](https://openaccess.thecvf.com/content/CVPR2023/html/Guo_Vid2Avatar_3D_Avatar_Reconstruction_From_Videos_in_the_Wild_via_CVPR_2023_paper.html) |
| 16 | `hess2025splatad` | SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving | sec/2_related_work.tex:8 | [来源](https://openaccess.thecvf.com/content/CVPR2025/html/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.html) |
| 17 | `hong2024lrm` | LRM: Large Reconstruction Model for Single Image to 3D | sec/2_related_work.tex:11 | [来源](https://proceedings.iclr.cc/paper_files/paper/5272-/bibtex) |
| 18 | `hu2024gaussianavatar` | GaussianAvatar: Towards Realistic Human Avatar Modeling from a Single Video via Animatable 3D Gaussians | sec/2_related_work.tex:17 | [来源](https://openaccess.thecvf.com/content/CVPR2024/html/Hu_GaussianAvatar_Towards_Realistic_Human_Avatar_Modeling_from_a_Single_Video_CVPR_2024_paper.html) |
| 19 | `hu2024gauhuman` | GauHuman: Articulated Gaussian Splatting from Monocular Human Videos | sec/2_related_work.tex:17 | [来源](https://openaccess.thecvf.com/content/CVPR2024/html/Hu_GauHuman_Articulated_Gaussian_Splatting_from_Monocular_Human_Videos_CVPR_2024_paper.html) |
| 20 | `kerbl2023gaussians` | 3D Gaussian Splatting for Real-Time Radiance Field Rendering | sec/2_related_work.tex:5；sec/3_method.tex:18 | [来源](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) |
| 21 | `kirillov2023sam` | Segment Anything | sec/2_related_work.tex:17 | [来源](https://openaccess.thecvf.com/content/ICCV2023/html/Kirillov_Segment_Anything_ICCV_2023_paper.html) |
| 22 | `kocabas2024hugs` | HUGS: Human Gaussian Splats | sec/2_related_work.tex:17 | [来源](https://openaccess.thecvf.com/content/CVPR2024/html/Kocabas_HUGS_Human_Gaussian_Splats_CVPR_2024_paper.html) |
| 23 | `leroy2024mast3r` | Grounding Image Matching in 3D with MASt3R | sec/2_related_work.tex:11 | [来源](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9080_ECCV_2024_paper.php) |
| 24 | `lipman2022flowmatching` | Flow Matching for Generative Modeling | sec/3_method.tex:100 | [来源](https://openreview.net/pdf?id=PqvMRDCJT9t) |
| 25 | `liu2023zero123` | Zero-1-to-3: Zero-shot One Image to 3D Object | sec/2_related_work.tex:20 | [来源](https://openaccess.thecvf.com/content/ICCV2023/html/Liu_Zero-1-to-3_Zero-shot_One_Image_to_3D_Object_ICCV_2023_paper.html) |
| 26 | `loper2015smpl` | SMPL: A Skinned Multi-Person Linear Model | sec/2_related_work.tex:17 | [来源](https://smpl.is.tue.mpg.de/) |
| 27 | `lu2025urbancad` | UrbanCAD: Towards Highly Controllable and Photorealistic 3D Vehicles for Urban Scene Simulation | sec/2_related_work.tex:17 | [来源](https://openaccess.thecvf.com/content/CVPR2025/html/Lu_UrbanCAD_Towards_Highly_Controllable_and_Photorealistic_3D_Vehicles_for_Urban_CVPR_2025_paper.html) |
| 28 | `martinbrualla2021nerfw` | NeRF in the Wild: Neural Radiance Fields for Unconstrained Photo Collections | sec/2_related_work.tex:5 | [来源](https://openaccess.thecvf.com/content/CVPR2021/html/Martin-Brualla_NeRF_in_the_Wild_Neural_Radiance_Fields_for_Unconstrained_Photo_CVPR_2021_paper.html) |
| 29 | `miao2025evolsplat` | EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis | sec/2_related_work.tex:8 | [来源](https://openaccess.thecvf.com/content/CVPR2025/html/Miao_EVolSplat_Efficient_Volume-based_Gaussian_Splatting_for_Urban_View_Synthesis_CVPR_2025_paper.html) |
| 30 | `mildenhall2020nerf` | NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis | sec/2_related_work.tex:5 | [来源](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/1473_ECCV_2020_paper.php) |
| 31 | `moenne2024gaussianraytracing` | 3D Gaussian Ray Tracing: Fast Tracing of Particle Scenes | sec/2_related_work.tex:5 | [来源](https://research.nvidia.com/labs/toronto-ai/3DGRT/) |
| 32 | `ost2021neuralgraphs` | Neural Scene Graphs for Dynamic Scenes | sec/2_related_work.tex:8 | [来源](https://openaccess.thecvf.com/content/CVPR2021/html/Ost_Neural_Scene_Graphs_for_Dynamic_Scenes_CVPR_2021_paper.html) |
| 33 | `pavlakos2019smplx` | Expressive Body Capture: 3D Hands, Face, and Body From a Single Image | sec/2_related_work.tex:17 | [来源](https://openaccess.thecvf.com/content_CVPR_2019/html/Pavlakos_Expressive_Body_Capture_3D_Hands_Face_and_Body_From_a_CVPR_2019_paper.html) |
| 34 | `peebles2023dit` | Scalable Diffusion Models with Transformers | sec/3_method.tex:100 | [来源](https://openaccess.thecvf.com/content/ICCV2023/html/Peebles_Scalable_Diffusion_Models_with_Transformers_ICCV_2023_paper.html) |
| 35 | `poole2023dreamfusion` | DreamFusion: Text-to-3D using 2D Diffusion | sec/2_related_work.tex:20 | [来源](https://dreamfusion3d.github.io/) |
| 36 | `pumarola2021dnerf` | D-NeRF: Neural Radiance Fields for Dynamic Scenes | sec/2_related_work.tex:5 | [来源](https://openaccess.thecvf.com/content/CVPR2021/html/Pumarola_D-NeRF_Neural_Radiance_Fields_for_Dynamic_Scenes_CVPR_2021_paper.html) |
| 37 | `qian2024avatar` | 3DGS-Avatar: Animatable Avatars via Deformable 3D Gaussian Splatting | sec/2_related_work.tex:17 | [来源](https://openaccess.thecvf.com/content/CVPR2024/html/Qian_3DGS-Avatar_Animatable_Avatars_via_Deformable_3D_Gaussian_Splatting_CVPR_2024_paper.html) |
| 38 | `qiu2025lhm` | LHM: Large Animatable Human Reconstruction Model for Single Image to 3D in Seconds | sec/2_related_work.tex:17 | [来源](https://openaccess.thecvf.com/content/ICCV2025/html/Qiu_LHM_Large_Animatable_Human_Reconstruction_Model_for_Single_Image_to_ICCV_2025_paper.html) |
| 39 | `rematas2022urban` | Urban Radiance Fields | sec/2_related_work.tex:8 | [来源](https://openaccess.thecvf.com/content/CVPR2022/html/Rematas_Urban_Radiance_Fields_CVPR_2022_paper.html) |
| 40 | `ren2026tokengs` | TokenGS: Decoupling 3D Gaussian Prediction from Pixels with Learnable Tokens | sec/2_related_work.tex:11 | [来源](https://openaccess.thecvf.com/content/CVPR2026/html/Ren_TokenGS_Decoupling_3D_Gaussian_Prediction_from_Pixels_with_Learnable_Tokens_CVPR_2026_paper.html) |
| 41 | `ren2025gen3c` | GEN3C: 3D-Informed World-Consistent Video Generation with Precise Camera Control | sec/2_related_work.tex:23 | [来源](https://openaccess.thecvf.com/content/CVPR2025/html/Ren_GEN3C_3D-Informed_World-Consistent_Video_Generation_with_Precise_Camera_Control_CVPR_2025_paper.html) |
| 42 | `shi2024mvdream` | MVDream: Multi-view Diffusion for 3D Generation | sec/2_related_work.tex:20 | [来源](https://proceedings.iclr.cc/paper_files/paper/4919-/bibtex) |
| 43 | `shin2024canonicalfusion` | CanonicalFusion: Generating Drivable 3D Human Avatars from Multiple Images | sec/2_related_work.tex:17 | [来源](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3322_ECCV_2024_paper.php) |
| 44 | `shin2024wham` | WHAM: Reconstructing World-grounded Humans with Accurate 3D Motion | sec/2_related_work.tex:17 | [来源](https://openaccess.thecvf.com/content/CVPR2024/html/Shin_WHAM_Reconstructing_World-grounded_Humans_with_Accurate_3D_Motion_CVPR_2024_paper.html) |
| 45 | `sun2020waymo` | Scalability in Perception for Autonomous Driving: Waymo Open Dataset | sec/1_introduction.tex:4 | [来源](https://openaccess.thecvf.com/content_CVPR_2020/html/Sun_Scalability_in_Perception_for_Autonomous_Driving_Waymo_Open_Dataset_CVPR_2020_paper.html) |
| 46 | `tancik2022blocknerf` | Block-NeRF: Scalable Large Scene Neural View Synthesis | sec/2_related_work.tex:8 | [来源](https://openaccess.thecvf.com/content/CVPR2022/html/Tancik_Block-NeRF_Scalable_Large_Scene_Neural_View_Synthesis_CVPR_2022_paper.html) |
| 47 | `tang2024lgm` | LGM: Large Multi-View Gaussian Model for High-Resolution 3D Content Creation | sec/2_related_work.tex:11 | [来源](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/465_ECCV_2024_paper.php) |
| 48 | `tian2025drivingforward` | DrivingForward: Feed-forward 3D Gaussian Splatting for Driving Scene Reconstruction from Flexible Surround-view Input | sec/2_related_work.tex:14 | [来源](https://ojs.aaai.org/index.php/AAAI/article/view/32793) |
| 49 | `tonderski2024neurad` | NeuRAD: Neural Rendering for Autonomous Driving | sec/2_related_work.tex:8 | [来源](https://openaccess.thecvf.com/content/CVPR2024/html/Tonderski_NeuRAD_Neural_Rendering_for_Autonomous_Driving_CVPR_2024_paper.html) |
| 50 | `vaswani2017attention` | Attention is All you Need | sec/3_method.tex:36 | [来源](https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Bibtex.bib) |
| 51 | `wang2025vggt` | VGGT: Visual Geometry Grounded Transformer | sec/2_related_work.tex:11 | [来源](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html) |
| 52 | `wang2025cut3r` | Continuous 3D Perception Model with Persistent State | sec/2_related_work.tex:11 | [来源](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Continuous_3D_Perception_Model_with_Persistent_State_CVPR_2025_paper.html) |
| 53 | `wang2025fresa` | FRESA: Feedforward Reconstruction of Personalized Skinned Avatars from Few Images | sec/2_related_work.tex:17 | [来源](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_FRESA_Feedforward_Reconstruction_of_Personalized_Skinned_Avatars_from_Few_Images_CVPR_2025_paper.html) |
| 54 | `wang2024dust3r` | DUSt3R: Geometric 3D Vision Made Easy | sec/2_related_work.tex:11 | [来源](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_DUSt3R_Geometric_3D_Vision_Made_Easy_CVPR_2024_paper.html) |
| 55 | `wang2024drivedreamer` | DriveDreamer: Towards Real-world-driven World Models for Autonomous Driving | sec/2_related_work.tex:23 | [来源](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6416_ECCV_2024_paper.php) |
| 56 | `weng2022humannerf` | HumanNeRF: Free-Viewpoint Rendering of Moving People From Monocular Video | sec/2_related_work.tex:17 | [来源](https://openaccess.thecvf.com/content/CVPR2022/html/Weng_HumanNeRF_Free-Viewpoint_Rendering_of_Moving_People_From_Monocular_Video_CVPR_2022_paper.html) |
| 57 | `wu2025difix3d` | DIFIX3D+: Improving 3D Reconstructions with Single-Step Diffusion Models | sec/2_related_work.tex:23 | [来源](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_DIFIX3D_Improving_3D_Reconstructions_with_Single-Step_Diffusion_Models_CVPR_2025_paper.html) |
| 58 | `wu2025gut` | 3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting | sec/2_related_work.tex:5 | [来源](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_3DGUT_Enabling_Distorted_Cameras_and_Secondary_Rays_in_Gaussian_Splatting_CVPR_2025_paper.html) |
| 59 | `xiang2025trellis` | Structured 3D Latents for Scalable and Versatile 3D Generation | sec/2_related_work.tex:20 | [来源](https://openaccess.thecvf.com/content/CVPR2025/html/Xiang_Structured_3D_Latents_for_Scalable_and_Versatile_3D_Generation_CVPR_2025_paper.html) |
| 60 | `xiang2026trellis2` | Native and Compact Structured Latents for 3D Generation | sec/2_related_work.tex:20 | [来源](https://openaccess.thecvf.com/content/CVPR2026/html/Xiang_Native_and_Compact_Structured_Latents_for_3D_Generation_CVPR_2026_paper.html) |
| 61 | `xu2025depthsplat` | DepthSplat: Connecting Gaussian Splatting and Depth | sec/2_related_work.tex:11 | [来源](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_DepthSplat_Connecting_Gaussian_Splatting_and_Depth_CVPR_2025_paper.html) |
| 62 | `yan2024street` | Street Gaussians: Modeling Dynamic Urban Scenes with Gaussian Splatting | sec/1_introduction.tex:8；sec/2_related_work.tex:8 | [来源](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9243_ECCV_2024_paper.php) |
| 63 | `streetcrafter` | StreetCrafter: Street View Synthesis with Controllable Video Diffusion Models | sec/1_introduction.tex:8；sec/2_related_work.tex:23 | [来源](https://openaccess.thecvf.com/content/CVPR2025/html/Yan_StreetCrafter_Street_View_Synthesis_with_Controllable_Video_Diffusion_Models_CVPR_2025_paper.html) |
| 64 | `yang2025fast3r` | Fast3R: Towards 3D Reconstruction of 1000+ Images in One Forward Pass | sec/2_related_work.tex:11 | [来源](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Fast3R_Towards_3D_Reconstruction_of_1000_Images_in_One_Forward_CVPR_2025_paper.html) |
| 65 | `yang2024emernerf` | EmerNeRF: Emergent Spatial-Temporal Scene Decomposition via Self-Supervision | sec/2_related_work.tex:8 | [来源](https://proceedings.iclr.cc/paper_files/paper/4992-/bibtex) |
| 66 | `yang2025storm` | STORM: Spatio-TempOral Reconstruction Model For Large-Scale Outdoor Scenes | sec/1_introduction.tex:6；sec/2_related_work.tex:14；sec/4_experiments.tex:16；sec/4_experiments.tex:19 | [来源](https://proceedings.iclr.cc/paper_files/paper/1321-/bibtex) |
| 67 | `yang2023unisim` | UniSim: A Neural Closed-Loop Sensor Simulator | sec/2_related_work.tex:8 | [来源](https://openaccess.thecvf.com/content/CVPR2023/html/Yang_UniSim_A_Neural_Closed-Loop_Sensor_Simulator_CVPR_2023_paper.html) |
| 68 | `yang2025genassets` | GenAssets: Generating in-the-wild 3D Assets in Latent Space | sec/1_introduction.tex:8；sec/2_related_work.tex:20 | [来源](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_GenAssets_Generating_in-the-wild_3D_Assets_in_Latent_Space_CVPR_2025_paper.html) |
| 69 | `yang2024deformablegs` | Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction | sec/2_related_work.tex:5 | [来源](https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Deformable_3D_Gaussians_for_High-Fidelity_Monocular_Dynamic_Scene_Reconstruction_CVPR_2024_paper.html) |
| 70 | `yu2024mipsplatting` | Mip-Splatting: Alias-free 3D Gaussian Splatting | sec/2_related_work.tex:5 | [来源](https://openaccess.thecvf.com/content/CVPR2024/html/Yu_Mip-Splatting_Alias-free_3D_Gaussian_Splatting_CVPR_2024_paper.html) |
| 71 | `zhang2024gslrm` | GS-LRM: Large Reconstruction Model for 3D Gaussian Splatting | sec/2_related_work.tex:11 | [来源](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3212_ECCV_2024_paper.php) |
| 72 | `zhang2018lpips` | The Unreasonable Effectiveness of Deep Features as a Perceptual Metric | sec/2_related_work.tex:23 | [来源](https://openaccess.thecvf.com/content_cvpr_2018/html/Zhang_The_Unreasonable_Effectiveness_CVPR_2018_paper.html) |
| 73 | `zhou2024holistichugs` | HUGS: Holistic Urban 3D Scene Understanding via Gaussian Splatting | sec/2_related_work.tex:8 | [来源](https://openaccess.thecvf.com/content/CVPR2024/html/Zhou_HUGS_Holistic_Urban_3D_Scene_Understanding_via_Gaussian_Splatting_CVPR_2024_paper.html) |
| 74 | `zhou2024drivinggaussian` | DrivingGaussian: Composite Gaussian Splatting for Surrounding Dynamic Autonomous Driving Scenes | sec/2_related_work.tex:8 | [来源](https://openaccess.thecvf.com/content/CVPR2024/html/Zhou_DrivingGaussian_Composite_Gaussian_Splatting_for_Surrounding_Dynamic_Autonomous_Driving_Scenes_CVPR_2024_paper.html) |
| 75 | `zhuang2025idol` | IDOL: Instant Photorealistic 3D Human Creation from a Single Image | sec/2_related_work.tex:17 | [来源](https://openaccess.thecvf.com/content/CVPR2025/html/Zhuang_IDOL_Instant_Photorealistic_3D_Human_Creation_from_a_Single_Image_CVPR_2025_paper.html) |

## 最终核验

- 两版 PDF 均为 13 页，各含 84 条参考文献；编译退出码均为 0，最终日志无未解析引用、交叉引用或 overfull 警告。
- 75 条输入文献在中英文中均有实际引用；非实验部分的引用顺序、章节层级、标签和数学内容核对通过。
- 既有 34 项检查通过，15 个显示数学环境保持一致。
- 两份实验 TeX 和三张依赖图与用户指定来源逐字节一致。
- 查看两版全部 26 页缩略图，并逐页查看英文第 3、13 页和中文第 2 页；没有发现文字裁切或重叠。实验浮动表图安排保持原样，暂不按页数调整。
- Git HEAD 保持 `a2cdacc`，暂存区为空；本轮没有提交、推送或改写历史。
