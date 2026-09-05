---
title: "HIP 入门指南：AMD GPU 异构编程的起点"
date: 2026-09-05 10:00:00 +0800
categories: [编程, GPU]
tags: [HIP, ROCm, GPU, CUDA, 异构计算]
---

> 本文参考 AMD 官方文档编写，主要来源：
> * AMD ROCm 10.0 文档 — <https://rocm.docs.amd.com/en/latest/>
> * What is HIP? — <https://rocm.docs.amd.com/projects/HIP/en/latest/what_is_hip.html>
> * SAXPY 官方教程 — <https://rocm.docs.amd.com/projects/HIP/en/latest/tutorial/saxpy.html>

## 写在前面：HIP 的能力范围与使用场景

HIP（Heterogeneous-compute Interface for Portability）是 AMD ROCm 平台的核心编程接口：既是 **C++ 运行时 API**，也是一门 **核函数（kernel）语言**。它允许你用**单一 C++ 源代码**同时编写运行在 CPU（host）和 GPU（device）上的程序，并直接在代码里以 `__global__`、`<<<...>>>` 等扩展发起"CPU 调用 GPU 函数"的并行计算。

用官方文档首页的话总结：HIP 是一套**薄 API**，相对直接对 AMD ROCm 硬编码几乎没有性能损失；它面向"异构计算"，同时覆盖**数据传输、内存管理、流与事件、内核调度**等主机侧职责，和**大规模并行内核、硬件特性访问**等设备侧能力。

### 适合使用 HIP 的场景

* **高性能计算（HPC）与科学计算**：分子动力学、有限元、流体仿真等需要手写内核、榨取硬件性能的领域；
* **AI 训练与推理**：以 PyTorch、JAX 等框架在 AMD 平台上加速（底层经 HIP 实现），或直接用 HIP 部署算子；
* **从 CUDA 迁移**：已有 NVIDIA CUDA 代码需要跑在 AMD Instinct / Radeon / Ryzen AI 上；HIP 与 CUDA 语法高度一致，配合 HIPify 工具可大幅降低移植成本；
* **单源码多平台**：希望一套代码既能编译到 NVIDIA（NVIDIA 设备上 HIP 会映射到 CUDA），也能编译到 AMD。

### 需要注意的边界

* **HIP 不是 CUDA 的 drop-in 替代品**。官方移植指南明确说明：接口对齐度高，但迁移通常仍需人工修改与性能调优；
* **不支持 device-side 动态并行**：CUDA 允许内核内再启动内核，HIP 不允许（若直接移植此类代码需要重构）；
* **图形渲染不在 HIP 职责内**：HIP 面向 GPGPU 计算，图形管线由其他栈（如 Vulkan 的 RADV）承担；
* **核函数参数必须 trivially copyable**：内核按值传参，参数会以 memcpy 方式传入设备端。

一句话定位：**HIP = AMD 生态里的"CUDA"，但设计目标是异构可移植**。

## 为什么用 HIP 而不是直接写 amdgpu 汇编

ROM（ROCm）平台本身提供了 `clang` / `hipcc` 编译器、`rocgdb` 调试器、`rocprofv3` 性能分析器，以及 hipFFT、hipBLAS 等库。HIP 在其中承担"编程语言 + 运行时"层，给你：

1. **熟悉的 C++ 体验**——支持模板、类、命名空间、C++11 lambda、运算符重载，内核里几乎可以用所有常见 C++ 特性；
2. **与 CUDA 近似的语法**——有 CUDA 经验的人几小时内即可上手，函数名大多只是 `cudaXxx` → `hipXxx`；
3. **生态互通**——hipFFT、hipBLAS 等提供与 CUDA 对应库 API 兼容的接口，方便镜像移植整个软件栈。

## ROCm 10.0 与生态总体介绍

最新的 ROCm 10.0（2026 年发布，TheRock 构建系统）包含 ROCm Qualified SDK 的完整组件：

* **编译器/工具**：`amdclang++`、`hipcc`、`flang`（随 `amdrocm-llvm` 包提供）；
* **运行时**：HIP、ROCm（HSA）、运行时编译；
* **数学/通信库**：rocBLAS、hipBLAS、rocFFT、hipFFT、rocRAND、hipRAND、rocPRIM 等；
* **调试/剖析**：rocgdb、ROCprofiler-SDK、rocprofv3、roctracer；
* **HIPify**：CUDA → HIP 自动迁移工具。

支持设备覆盖 AMD Instinct（MI100 → 最新的 gfx950 系列）、AMD Radeon（RX 9000 等）、AMD Ryzen AI APU；Windows 与 Linux（Ubuntu、RHEL、SLES、Debian 等）均有官方支持。

## 环境准备

安装方式按使用场景分为几类（详见官方《Install AMD ROCm》页面）：

| 方式 | 适用平台 | 适用场景 |
| --- | --- | --- |
| apt / dnf / zypper | Linux | 传统系统级安装 |
| `amdgpu-install` | Linux | Radeon / Ryzen，带 amdgpu 驱动，按 usecase 勾选 |
| pip | Linux / Windows | Python + ML 工作流（PyTorch、JAX） |
| Tarball | Linux / Windows | 自包含、可移植的安装 |
| Runfile | Linux | 免包管理器、无网络环境 |

以 Ubuntu 24.04 + Radeon 为例的常见流程：

```bash
sudo apt update
wget https://repo.radeon.com/amdgpu-install/31.50/ubuntu/noble/amdgpu-install_31.50.315000-1_all.deb
sudo apt install ./amdgpu-install_31.50.315000-1_all.deb
sudo amdgpu-install --usecase=rocm
```

安装后需要把编译器加入 PATH（AMD 官方安装到 `/opt/rocm`，与系统默认路径无关）：

```bash
export PATH=/opt/rocm/bin:${PATH}
amdclang++ --version   # hipcc 在 amdrocm-llvm 中仍旧可用
```

> 提示：如果之前装过老版 HIP SDK / ROCm 7.2.4 及更早版本，官方建议先卸载再装 ROCm 10。GPU 访问权限可通过加入 `render`、`video` 组或配置 udev 规则来实现。

## 编程模型：线程 → 块 → 网格

HIP 的编程模型和 CUDA 几乎一致，理解三个层级即可：

* **线程（Thread）**：GPU 上最基本执行单元，内核里通过内建变量获得自己的编号；
* **块（Block）**：一组可协作的线程（共享内存、同步屏障），是调度的单位。HIP 中一个块最多约 1024 线程，实际上限可查 `hipGetDeviceProperties()`；
* **网格（Grid）**：若干块组成的整体；一次内核启动就是一个网格。

执行模型是 SIMT（单指令多线程）：同一块的线程并行执行相同指令，但操作各自的数据。因为块是独立的调度单位，编写内核时天然具备跨 GPU 规模的可扩展性。

## 第一个程序：SAXPY

SAXPY（Single-precision A·X Plus Y）就是向量运算 `z[i] = a * x[i] + y[i]`，相当于 GPU 世界的 "Hello, World"。下面是官方 `rocm-examples` 仓库中 `HIP-Basic/saxpy/main.hip` 的讲解版：

```hip
#include <hip/hip_runtime.h>
#include <iostream>
#include <vector>

#define HIP_CHECK(expr)                                         \
    do {                                                        \
        hipError_t err = (expr);                                \
        if (err != hipSuccess) {                                \
            std::cerr << "HIP error: "                          \
                      << hipGetErrorString(err) << std::endl;   \
            exit(1);                                            \
        }                                                       \
    } while (0)

// __global__ 表示这是可从 host 启动的 device 端内核
__global__ void saxpy_kernel(const float a, const float* d_x,
                             float* d_y, const unsigned int size)
{
    // 用内建变量计算当前线程在整个网格中的线性索引
    const unsigned int global_idx = blockIdx.x * blockDim.x + threadIdx.x;

    // 网格可能大于向量长度，务必防越界
    if (global_idx < size)
    {
        d_y[global_idx] = a * d_x[global_idx] + d_y[global_idx];
    }
}

int main()
{
    constexpr unsigned size = 1'000'000;
    constexpr unsigned block_size = 256;
    const unsigned grid_size = (size + block_size - 1) / block_size;

    std::vector<float> x(size, 1.0f), y(size, 2.0f);
    const float a = 3.0f;

    // host -> device 设备内存分配与数据拷贝
    float* d_x{};
    float* d_y{};
    const size_t size_bytes = size * sizeof(float);
    HIP_CHECK(hipMalloc(&d_x, size_bytes));
    HIP_CHECK(hipMalloc(&d_y, size_bytes));
    HIP_CHECK(hipMemcpy(d_x, x.data(), size_bytes, hipMemcpyHostToDevice));
    HIP_CHECK(hipMemcpy(d_y, y.data(), size_bytes, hipMemcpyHostToDevice));

    // 三元尖括号启动内核：<<<网格大小, 块大小, 动态共享内存, 流>>>
    saxpy_kernel<<<dim3(grid_size), dim3(block_size), 0, hipStreamDefault>>>(
        a, d_x, d_y, size);

    // device -> host 取回结果，并同步
    HIP_CHECK(hipMemcpy(y.data(), d_y, size_bytes, hipMemcpyDeviceToHost));
    HIP_CHECK(hipDeviceSynchronize());

    for (unsigned i = 0; i < 10; ++i)
        std::cout << y[i] << " ";
    std::cout << std::endl;

    hipFree(d_x);
    hipFree(d_y);
    return 0;
}
```

几个要点对应前面的语言约定：

* `__global__` 函数（内核）必须返回 `void`，参数按值传递且需 trivially copyable，指针参数指向设备内存；
* `HIP_CHECK` 是示例工具里的自定义宏，用于检查每个 API 的 `hipError_t` 返回值——**生产代码一定要做错误检查**；
* 启动配置的四要素：网格大小（块数）、块大小（线程数）、每块动态共享内存、执行流。

## 编译与运行

```bash
export PATH=/opt/rocm/bin:${PATH}
amdclang++ main.hip -o saxpy -lamdhip64 -L /opt/rocm/lib -O2

# 查看本机 GPU 对应的 gfx 架构
/opt/rocm/bin/rocminfo | grep gfx

# 按目标架构重编（gfx 编号以 rocminfo 为准，例如最新 Instinct gfx950）
amdclang++ main.hip -o saxpy -lamdhip64 -L /opt/rocm/lib -O2 \
    --offload-arch=gfx942

./saxpy   # 输出: 3 5 7 9 11 13 15 17 19 21
```

如果运行时出现 `Invalid device function`（即 `hipErrorInvalidDeviceFunction`），通常意味着嵌入的 code object 与机器的 gfx 架构不匹配，用 `rocminfo` 查清楚后以 `--offload-arch` 重新编译即可。同理也可用 `llvm-objdump --offloading ./saxpy` 检查可执行文件里内嵌了哪些设备二进制。

在现代工具链里更推荐用 CMake：`enable_language(HIP)` 配合 `find_package(HIP)`，由构建系统自动处理架构参数。

## 语言特性速览

**限定符（与 CUDA 基本一致）：**

* `__global__` — 可从 host 启动的内核函数；
* `__device__` — 只能在 device 端调用；
* `__host__ __device__` — 两端都编译（注意：此类函数不能使用 GPU 坐标内建变量）；
* `__constant__` / `__shared__` / `__managed__` — 常量内存、块共享内存、托管内存；
* `__launch_bounds__` — 占位（occupancy）提示，控制寄存器用量。

**ROCm 7+ 显著变化：** 新增了显式坐标内建函数 `hipThreadIdx_x`、`hipBlockIdx_x`、`hipBlockDim_x`、`hipGridDim_x`（以及 y/z、`hipWorkDim_*`），与旧式 `threadIdx.x` 等并存。HIP API 7.0 为对齐 CUDA 做了若干**不兼容变更**，升级新版时需要重新编译：

```bash
hipcc --version          # 用 hipcc 包裹 amdclang++ 亦可
```

**HIP 7.0+ 兼容性提醒：** 某些行为向 CUDA 看齐（例如流参数不再校验有效性、分割库归属），存量大项目升级时建议先跑一遍测试集。

## 迁移与工具链

* **HIPIFY**：clang 前端 + Perl 版两套工具，把 `cudaMalloc` 等自动换成 `hipMalloc`；对模板内核的启动会插入 `HIP_KERNEL_NAME` 包装。ROCm 5.3 起默认生成 `<<<>>>` 语法，也可通过 `--hip-kernel-execution-syntax` 保留 `hipLaunchKernelGGL` 风格；
* **rocgdb**：断点调试 host/device 代码；
* **rocprofv3 / ROCprofiler-SDK**：内核耗时、内存拷贝、API 调用剖析，ROCm 10 中统一迁移到 ROCprofiler-SDK 工作流；
* **rocm-examples**：官方示例仓库，覆盖 SAXPY、归约（reduction）、cooperative groups、HIP Graph 等进阶模式：<https://github.com/amd/rocm-examples>

## 小结：接下来怎么学

1. **动手装环境**：按《Install AMD ROCm》选你的发行版，或直接用官方 Docker 镜像（`rocm/rocm-terminal`，自带 PATH 配置）；
2. **过一遍官方 SAXPY 教程**，再读归约（Reduction）教程理解共享内存与同步；
3. **配合工具**看性能：先 `rocminfo` 确认架构，再 `rocprofv3` 定位热点；
4. **有 CUDA 背景的同学**直接读《Porting CUDA code to HIP》，用 HIPify 跑一个自己的项目试试迁移。

更多资源：

* HIP 官方文档首页：<https://rocm.docs.amd.com/projects/HIP/en/latest/>
* HIP 编程模型：<https://rocm.docs.amd.com/projects/HIP/en/latest/understand/programming_model.html>
* AMD ROCm Programming Guide（聚合式手册，支持 PDF 离线阅读）：<https://rocm-handbook.amd.com/>
* HIP GitHub 仓库：<https://github.com/ROCm/HIP>