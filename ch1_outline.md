## 1.X Substitution Energy-Based Parameter Optimization of Ion–Lipid Cross Terms

### A. Motivation for Custom Cross-Term Parameterization
- Standard force fields treat ions and lipids independently.
- Ion–lipid cross terms are usually estimated using mixing rules (e.g., Lorentz–Berthelot).
- These rules systematically underestimate ion–lipid binding energies.
- Result: inaccurate ion adsorption and bilayer structure in MD simulations.
- Goal: parameterize Lennard-Jones cross terms explicitly using quantum mechanical (QM) benchmarks.

---

### B. Substitution Energy as a Target Metric
- Substitution energy = the energy change when replacing water ligands with lipid-mimicking ligands.
- Chosen because it:
  - Is chemically interpretable.
  - Relates to ion dehydration behavior at interfaces.
  - Provides a consistent framework across ion–ligand systems.

**General substitution reaction:**
``Ion(H₂O)_n + mX → Ion(H₂O)_{n−m}X_m + mH₂O``

**Substitution energy formula:**
``ΔE_sub = E_mixed + mE_H₂O − E_water + mE_X``

Where:
- `E_mixed` = energy of cluster with mixed ligands
- `E_water` = energy of fully hydrated ion
- `E_X`, `E_H₂O` = energy of isolated ligands/waters

---

### C. Cluster Design for Each Ion

#### Na⁺ and Li⁺
- Ligands: methyl acetate (MeAc), diethyl phosphate (DePh)
- Cluster sizes: 1–4 ligands
- Model: **Full substitution**
  - All waters replaced with ligands
- Justification: These ions can partially or fully dehydrate at bilayer interfaces.

#### Mg²⁺ (2024 parameters – Chapter 3)
- Same ligands and cluster design as Na⁺/Li⁺
- Model: **Full substitution**
- Rationale: Maintains consistency across ions
- Limitation: Does not reflect Mg²⁺'s resistance to dehydration

#### Mg²⁺ (2025 parameters – Chapter 4)
- Cluster always has **6 oxygen ligands** total
- Composition: 1–4 lipid ligands, remaining filled with H₂O
- Model: **Partial substitution**
- Justification:
  - Mg²⁺ retains hydration at interfaces
  - Captures realistic competitive binding between water and lipid groups

---

### D. Parameter Optimization Procedure
- Optimization software: **ParOpt**
- Algorithm: **Nelder–Mead simplex**
- Objectives:
  - Minimize error in substitution energy
  - Minimize RMSD in cluster geometries
- Process:
  1. **Random simplex** initialization – broad search (400 simplexes)
  2. **Around-point** refinement – local search (400 simplexes)
- Constraints applied to σ and ε to avoid unphysical values
- Especially important for Mg²⁺ to avoid overbinding

---

### E. Summary Table

| Ion           | Ligands            | Max Ligands | Coordination Rule        | Substitution Model         | Notes                                                             |
|---------------|--------------------|-------------|---------------------------|-----------------------------|-------------------------------------------------------------------|
| Na⁺           | MeAc, DePh         | Up to 4     | Variable (≤4 ligands)     | Full substitution           | All waters replaced with ligands                                  |
| Li⁺           | MeAc, DePh         | Up to 4     | Variable (≤4 ligands)     | Full substitution           | Reflects moderate dehydration                                     |
| Mg²⁺ (2024)   | MeAc, DePh         | Up to 4     | Variable (≤4 ligands)     | Full substitution           | Used for consistency with Na⁺/Li⁺, but lacks hydration realism     |
| Mg²⁺ (2025)   | MeAc, DePh, H₂O    | Up to 4     | Fixed: 6 total oxygen     | Partial substitution (mixed) | Preserves hydration shell, better reflects Mg²⁺ coordination      |

---

### F. Closing Paragraph (to draft later)
- Reiterate why substitution-based optimization is chosen
- Emphasize improvement over mixing rules
- Show how different ion chemistries required different modeling choices
- Note that validation against bilayer simulations follows in Chapters 2–4


