For the bound: every exceptional challenge of every pair at n = 32, k = 16, A = 20 on mu_32 over BabyBear has a fibre-aligned anchor or lies in a nonaligned residual set of size at most c n with c = 3149.5.

### Proved for every pair
1. **Full Core-Size Partition ($L = 0 \dots 32$):**
   Every received pair $(f, g)$ on $\mu_{32}$ over BabyBear with $k = 16, A = 20$ has a unique maximal joint core of size $L = |Agr(f, P_0) \cap Agr(g, P_1)| \in \{0, 1, \dots, 32\}$.
2. **Large-Joint-Core Regime ($L \in [28, 32]$):**
   By the Large-Joint-Core Theorem (M-0023, bp1_8b45e4cc), for any pair with joint core $L \ge n - A + k = 32 - 20 + 16 = 28$, the total number of exceptional challenges satisfies $|E| \le \lfloor(n - L)/\max(1, A - L)\rfloor$:
   - $L = 32$: $|E| \le 0$
   - $L = 31$: $|E| \le 1$
   - $L = 30$: $|E| \le 2$
   - $L = 29$: $|E| \le 3$
   - $L = 28$: $|E| \le 4$
   All exceptional challenges here are residual and bounded by $4 \le 3149.5 \cdot 32$.
3. **Intermediate Deletion-Line Regime ($L \in [19, 27]$):**
   By the deletion-line residual theorem (bp1_7bd2a735), every joint-core size between $A - 1 = 19$ and $n - A + k - 1 = 27$ produces at most 117 nonaligned exceptional challenges:
   - For each $L \in \{19, 20, 21, 22, 23, 24, 25, 26, 27\}$: $|E_{\text{nonaligned}}| \le 117$.
   The required lower bound check $c \ge 117/32 \approx 3.65625$ is satisfied.
4. **Small-Core and Core-Free Regime ($L \in [0, 18]$):**
   For pairs with no joint core of size $\ge 19$:
   - Anchored challenges have agreement containing a fibre-aligned anchor (a union of whole fibres plus at most one punctured fibre of $\ge 19$ points), bounded by $13 D$ (M-0020, bp1_b5d17c9a), where $D \le 100,783$ via the Delsarte constant-weight code bound and Port D LP certificate.
   - Nonaligned isolated exceptional challenges are covered by label-carrying codeword pairs at joint-agreement sizes 16, 17, 18 with per-pair budgets 4, 5, 7 (M-0020). The smallest such cover satisfies $|C_{\text{cov}}| \le 100,783$ via the exact Abel summation $42,329,020 / 420 \le 100,783.38$.
   - Thus, nonaligned residual challenges for each $L \in \{0, 1, \dots, 18\}$ satisfy $|E_{\text{nonaligned}}| \le |C_{\text{cov}}| \le 100,783 = 3149.46875 \cdot 32 \le 3149.5 \cdot 32$.
5. **Unified Constant:**
   Across all 33 core sizes $L \in \{0, \dots, 32\}$, every exceptional challenge either contains a fibre-aligned anchor or belongs to a nonaligned residual set of size at most $c \cdot n$ with $c = 3149.5$.

### Proved inside a named mechanism
- **M-0023 Large-Core Mechanism:** Bounding $|E| \le \lfloor(n - L)/\max(1, A - L)\rfloor \le 4$ on $L \in [28, 32]$.
- **M-0020 Anchored Bound Mechanism:** Anchored exceptional count $\le 13 D$ on $L \in [0, 18]$.
- **bp1_7bd2a735 Deletion-Line Mechanism:** Bounding nonaligned challenges $\le 117$ on $L \in [19, 27]$.
- **Port C Abel Cover Mechanism:** Nonaligned isolated challenges covered by at most $100,783$ points on $L \in [0, 18]$ with Abel sum $42,329,020 / 420$.

### Measured
- **Field:** BabyBear ($p = 2^{31} - 2^{27} + 1 = 2013265921$)
- **Test Case 1 (spread-puncture pair bp1_3c550a59, bp1_d649c345):** $E = 117$ nonaligned challenges, $L = 19$, verified $117 \le 3149.5 \cdot 32$.
- **Test Case 2 (grp2_1 bp1_7bd2a735):** $E = 32$ challenges at joint core $L = 27$, verified $32 \le 3149.5 \cdot 32$.
- **Test Case 3 (340 witness-family pair bp1_e74aa3e6):** $E = 340$ challenges, all fibre-aligned anchors, verified 0 nonaligned challenges $\le 3149.5 \cdot 32$.
- **Test Case 4 (plant7 bp1_b5d17c9a):** $E = 7$ isolated challenges, covered by size-16 pairs, verified $7 \le 100,783$.
- **Test Case 5 (g11 bp1_f7bae4a9, bp1_1a06e935):** $E = 11$ isolated challenges, verified $11 \le 100,783$.
- **Test Case 6 (plant3 bp1_b5d17c9a):** $E = 3$ isolated challenges, verified $3 \le 100,783$.
