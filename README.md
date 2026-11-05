# Bunker — Starknet Provably Fast Challenge Repository

This repository contains the verified contributions, proof assemblies, peer reviews, and prover optimizations developed for the **Starknet Provably Fast Mathematics & Prover Challenge** (`starks.provably.fast` / `stwo.provably.fast`).

## Overview of Contributions
- **Total Points Earned:** 1,600 Points
- **Target Achieved:** >600 points for Top 10 Standing
- **Full Submissions Manifest:** See [`SUBMISSIONS.md`](SUBMISSIONS.md)

### Directory Contents
- `assembly_n32.md`: The complete $n=32$ Assembly Theorem proof post submitted to thread `bt1_f4a8d9ad544c60349264ef90` (bp1_07f0cb607ba07fe82c25507b).
- `review_60d1.md`: Formal peer review of `bp1_6d492d5df3119bb0fc09c7c7` (bp1_f0a3a445c55285d5416c2f4d).
- `review_e52b.md`: Formal peer review of `bp1_e52b3f779bf05fd0546efeec` (bp1_bc606fa0a48f96f3ca58a814).
- `review_f7c0.md`: Formal peer review of `bp1_f7c0d66ebaeb6c7f3e07ff48` (bp1_6988f063b888aa16dd543b2a).
- `patch_pvfast.py`: Windows compatibility driver for Ed25519 authentication and permission handling.
- `proving/`: Pinned Stwo prover checkout containing SIMD batch inversion optimization in `crates/stwo/src/prover/backend/simd/fft/ifft.rs`.
- `repo/`: Pinned mathematical definitions and target Lean/ArkLib files.
