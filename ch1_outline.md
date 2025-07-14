# Chapter 1 Outline: Introduction and Methods

## 1.1 Membranes as Complex Interfaces
- Lipid bilayers are dynamic, responsive interfaces.
- System behavior emerges from water–lipid–ion interactions.
- Even small changes in one component cascade through the system.

## 1.2 Why Mg²⁺?
- Biologically essential but chemically stubborn.
- Strong hydration, slow exchange, low ligand substitution.
- Sparse experimental benchmarks → simulation is necessary.
- Existing force fields fail to capture its subtle behavior.

## 1.3 Why Li⁺ and Na⁺?
- Li⁺ is used therapeutically, hypothesized to mimic Mg²⁺.
- Chemically weaker, more chaotropic, easier to model.
- Na⁺ is a useful reference ion: abundant and well-studied.
- Together, they contextualize Mg²⁺ selectivity and complexity.

## 1.4 Broader Context: Energy Storage Applications
- Li⁺, Na⁺, and Mg²⁺ are all candidates in battery research.
- Ion solvation and coordination behavior is key to electrolyte design.
- Improved force fields have relevance beyond biology.
- Parameterization methods here can inform cross-disciplinary models.

## 1.5 Modeling Strategies and Limitations
- Classical MD enables large systems, but uses approximate potentials.
- Standard Lorentz–Berthelot mixing rules fail for divalent ions.
- DFT provides accurate ion–ligand energetics for small clusters.
- Parameter optimization can bridge these methods.

## 1.6 Scope of This Dissertation
- Develop optimized ion–lipid LJ parameters for Mg²⁺, Na⁺, Li⁺.
- Benchmark against DFT substitution energies and geometries.
- Validate parameters against simulation observables:
  SAXS, electrostatics, hydration, and order parameters.
- Build models that are realistic, validated, and transferable.

---

## 1.7 Comparing Simulations with Experimental Observables

### 1.7.1 Small-Angle X-ray and Neutron Scattering (SAXS/SANS)
- Compute electron density and form factors from simulations.
- Compare peak-to-peak distance (D_HH) to experimental data.
- Validate bilayer structure and thickness.

### 1.7.2 Electrostatics and Gouy–Chapman Theory
- Compute ψ(z) by integrating 1D charge density.
- Use hydration boundary to define effective bilayer surface.
- Fit PB theory parameters (ψ_s, κ, ρ₀) and compare to simulation.

### 1.7.3 Order Parameters
- Calculate S_CD for lipid tails and headgroups.
- Use P₂(z) for water O–H bonds to analyze orientation.
- Define hydration boundary as zero-crossing in P₂(z).
- Compute quadrupolar splitting Δν for water comparison to NMR.

### 1.7.4 Water Dynamics and Diffusion
- Compute MSD and lateral diffusion in different spatial regions.
- Analyze orientational autocorrelation, fit with 3-time constants.
- Correlate water mobility with local ordering and ion binding.
- Note: Diffusion only analyzed for water in Chapter 2.

### 1.7.5 Substitution Energy Matching
- Define ΔE_sub using DFT: ligand substitution in Mg²⁺(H₂O)₆ clusters.
- Target clusters represent ester and phosphate binding sites.
- Compare optimized MD parameters to DFT for energies and distances.

### 1.7.6 Parameter Optimization
- Use ParOpt and Nelder–Mead to fit σ_ij and ε_ij for ion–lipid LJ terms.
- Optimize using error in substitution energies and ion–ligand distances.
- Compare performance to default Lorentz–Berthelot rules.
- Mg²⁺ 2024 vs Mg²⁺ 2025 parameters discussed in detail.


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


