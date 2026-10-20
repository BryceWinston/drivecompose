# Figure caption

**Overview of DriveCompose.** (a) Multi-camera observations are encoded into typed canonical supports for background and sky, rigid vehicles, and articulated humans. (b) Parallel local query groups exchange information through shared global memory. Conditional flow completes unknown codes while preserving observed codes and suppressing free space at every integration step. (c) Typed Gaussian heads decode candidate content, which is checked against observed images and an observed-only decoded reference before acceptance as a fixed world. This accepted content and externally supplied state separately enter composition and rendering, enabling different views and actor poses within the same world. Blue, orange, gray and hatching indicate observed, completed, unknown and free support, respectively. Scene imagery is illustrative.

本版将全局记忆交互与三路解码画成组级关系。外部策略 / 动力学提供状态，观测反馈细节在详细流程图中展开。
