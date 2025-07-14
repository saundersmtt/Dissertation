
# Chapter 1 – Introduction

## 1.1 Scientific Motivation

- Lipid bilayers are essential components of biological membranes.
- Simulations of ion–lipid systems show structural changes not observed experimentally.
- Force fields for lipids and ions are often developed independently.
- Mixing rules (e.g., Lorentz–Berthelot) introduce significant energetic errors, especially for ion–lipid interactions.
- Need for parameterization methods that reproduce experimental structure and local interaction energetics.

## 1.2 Ion–Lipid Interaction Challenges

- Specific ion effects at membrane interfaces are complex and highly dependent on hydration and coordination.
- Classical force fields are non-polarizable, missing many-body cooperative effects.
- Adsorption behavior of ions (Na⁺, Li⁺, Mg²⁺) is dependent on their electric field and hydration shell rigidity.

## 1.3 Dissertation Objectives

- Develop and validate a method to optimize ion–lipid interaction parameters using quantum mechanical cluster data.
- Characterize ion adsorption behavior based on degree of dehydration.
- Refine Mg²⁺–lipid parameters to reproduce structural perturbations in bilayers more accurately.

## 1.4 Organization of Dissertation

- **Chapter 2**: Development of a high-dimensional optimization framework (*MB–NB-fix*) to refine Na⁺–lipid interactions. Demonstrates improved agreement with experimental SAXS/SANS data.
- **Chapter 3**: Classification of ion adsorption modes (steric, imperfect, perfect) for Na⁺, Li⁺, and Mg²⁺ based on dehydration extent. Links adsorption behavior to electrostatic field strength.
- **Chapter 4**: Development of refined Mg²⁺ models with full sixfold coordination in target clusters. Shows how imperfect adsorption leads to bilayer thickening and ordering.
- **Chapter 5**: Conclusions and outlook. Discusses implications for mixed force fields and future inclusion of polarization and protein-lipid systems.

## 1.5 Terminology and Conventions

- “Steric adsorption”: Ion remains fully hydrated, no direct binding to lipids.
- “Imperfect adsorption”: Partial dehydration with some lipid coordination.
- “Perfect adsorption”: Full dehydration and direct binding to lipid oxygens.
- “Hydration boundary”: Region near bilayer where water loses bulk-like behavior.
- “MB–NB-fix”: Many-body non-bonded fix parameterization method using QM cluster data and ParOpt optimization.

## 1.6 References

*References for background literature may be added here or included in a global bibliography.*
