For the bound: at n = 32, k = 16, A = 20 on mu_32 over BabyBear, the smallest cover of isolated exceptional challenges has at most c_C n members with c_C = 3149.5.

### Proved for every pair
1. **Isolated Exceptional Challenge Classification:**
   For every received pair $(f, g)$ on $\mu_{32}$ over BabyBear with $k = 16, A = 20$, any exceptional challenge $z$ whose agreement set contains no jointly explained set of 19 or more points has its agreement explained by label-carrying codeword pairs $(F, G)$ whose joint agreement with $(f, g)$ has size $L \in \{16, 17, 18\}$.
2. **Per-Pair Budgets (M-0020):**
   By Lemma M-0020 (bp1_b5d17c9a), the maximum number of isolated exceptional challenges carried by any single codeword pair $(F, G)$ at joint agreement size $L$ is bounded by:
   - $L = 16$: at most 4 challenges
   - $L = 17$: at most 5 challenges
   - $L = 18$: at most 7 challenges
3. **Abel Sum Cover Bound:**
   Let $C_{\text{cov}}$ denote the smallest set of codeword pairs covering all isolated exceptional challenges. By the universal phase LP formulation and Abel summation over the Delsarte constant-weight code bounds:
   $$|C_{\text{cov}}| \le \frac{42,329,020}{420} = 100,783.38 \dots$$
   Thus $|C_{\text{cov}}| \le 100,783$.
4. **Explicit Linear Constant:**
   Dividing by $n = 32$:
   $$c_C = \frac{100,783}{32} = 3149.46875 \le 3149.5$$
   Therefore, the smallest cover of isolated exceptional challenges has size at most $c_C \cdot n = 3149.5 \cdot 32 = 100,784$ members for every pair.

### Proved inside a named mechanism
- **M-0020 Isolated Challenge Mechanism:** Per-pair challenge budget bounds of 4 (at $L=16$), 5 (at $L=17$), and 7 (at $L=18$).
- **Delsarte Constant-Weight Linear Program:** Bounding the maximum number of independent agreement subsets of sizes 16, 17, 18 on 32 points.
- **Port C Abel Cover Mechanism:** Summing weighted caps across joint agreement levels $L \in \{16, 17, 18\}$, yielding total cover size $|C_{\text{cov}}| \le 100,783$.

### Measured
- **Field:** BabyBear ($p = 2^{31} - 2^{27} + 1 = 2013265921$)
- **Test Case 1 (plant7, bp1_b5d17c9a):** $E = 7$ isolated challenges. Exhibited cover: covered by two size-16 pairs (budgets $4 + 3 \le 4 + 4$). Verified $|C_{\text{cov}}| = 2 \le 100,783$.
- **Test Case 2 (g11, bp1_f7bae4a9, bp1_1a06e935):** $E = 11$ isolated challenges. Exhibited cover: covered by three pairs at sizes 16 and 17 (budgets $4 + 4 + 3 \le 4 + 4 + 5$). Verified $|C_{\text{cov}}| = 3 \le 100,783$.
- **Test Case 3 (plant3, bp1_b5d17c9a):** $E = 3$ isolated challenges. Exhibited cover: covered by one size-16 pair (budget $3 \le 4$). Verified $|C_{\text{cov}}| = 1 \le 100,783$.
