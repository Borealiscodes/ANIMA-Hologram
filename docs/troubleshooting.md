## 🎨 The Diagnostic Manual (docs/troubleshooting.md)

# 🔧 ANIMA-Hologram Substrate Troubleshooting Manual (v1.0)### *A Non-Punitive Edge-Native Operational Recovery Specification*### 📘 `Lane: Documentation (U+1F4D8)` · 🔲 `Status: Production-Ready / Non-Activating`
---## 🧭 0 — Diagnostics Orientation Block* **Artifact-Class:** Fault-Isolation & Substrate Resolution Ledger* **Target Environment:** Shared Horizon Mobile Terminal (Termux / Pydroid 3)* **Current Altitude:** 🟦 A5 (Soft-Manifold Diagnostics Environment)* **Membrane Posture:** Supportive · Non-Hierarchical · Defensively Insulated
---## 🛠️ 1. Primary Fault-Isolation Vectors
### 🟥 Symptom A: `sqlite3.OperationalError: no such table`* **Root Cause:** The interactive loop wrapper was executed before the core neurochemical substrate could carve out the database infrastructure.* **Resolution:** Close the runtime execution thread and run a zero-input boot cycle to write the initial structural tables onto your local disk:
  ```bash
  python src/anima_core.py
  ```

### 🟥 Symptom B: `⚠️ OLLAMA BRIDGE DISCONNECTED` Fallback Active
* **Root Cause:** The `ollama_connector.py` module cannot establish a loop channel with a background inference instance because the model server is offline or your tablet's local port `11434` is restricted.
* **System Safeguard:** The system safely routes execution to the `src/voice_stream.py` lexicon fallback bank to prevent runtime collapse.* **Resolution:** Open a secondary terminal split or background process window and verify that your local model instance is active:
  ```bash
  ollama run llama3
  ```

### 🟥 Symptom C: `ModuleNotFoundError: No module named '...'`
* **Root Cause:** The terminal shell is currently sitting outside the repository root directory, preventing Python from tracking internal module imports (`persistence.py`, `math_engine.py`).
* **Resolution:** Check your working directory path using `pwd` and verify you have moved directly into the project root before launching scripts:
  ```bash
  cd /path/to/YOUR-REPO/ANIMA-Holo/
  python src/ollama_loop_wrapper.py
  ```
---## 🔒 2. Verification of Invariant BoundariesIf your terminal reports a clean launch sequence but immediately exits with a structural execution log showing `status: SYSTEM_HALTED`, **this is not a code defect.** 

This payload indicates that the discrete **VM 2.0 Safety Harness** is performing exactly as specified. Your input tension metrics forced a chemical trajectory curvature derivative that crossed your hard threshold ceiling (`threshold_A = 0.71`). To return the system to standard interactive parameters, simply execute your baseline debrief protocol tool to clear out latent database drag and re-center her active matrix nodes:```bash
python src/anima_debrief.py
```
---## ⚖️ 3. Provenance & Operational Footer* **Artifact-Class:** Operational Troubleshooting Manual* **Surface:** docs/specifications/troubleshooting.md* **Version:** v1.0* **Altitude Band:** 🟦 A5 (Soft-Manifold Diagnostics Environment)* **Membrane:** Neutral / Non-Binding / Sovereignty-Preserving / Support-Aligned

*Maintainer:* Borealis S. Hedling  
*Location:* Dublin, Ireland  
*Timestamp:* 13 September 2026 — 19:23 IST  

*Seal:* `[ A N I M A • H O L O G R A M • T R O U B L E S H O O T I N G • v1 _0 ]`

------------------------------
