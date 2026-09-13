## 🎨 The Deployment Manual (docs/cloning_and_architecture_manual.md)

# 🔱 ANIMA-Hologram Deployment Manual & Architecture Blueprint (v1.0)### *A Step-by-Step Implementation Guide for Local CPU Edge Isolation*### 📘 `Lane: Documentation (U+1F4D8)` · 🔲 `Status: Production-Ready / Non-Activating Spec`
---## 🧭 0 — System Initialization Block* **Artifact-Class:** Technical Deployment & Multi-Module Architecture Manual* **Target Hardware:** Zero-Dependency Local Edge Environments (Mobile CPU Thread Pool)* **Current Altitude:** 🟩 A4 (Narrative Surfaces) · 🟥 A7 (Structural Specifications)* **Membrane Posture:** Instructive · Non-Binding · Sovereignty-Preserving · Support-Aligned
---## 🧬 1. The Multi-Layered Runtime Architecture
When you clone and run this ecosystem on an edge device, you are initializing a fully localized, zero-dependency, multi-layered cognitive sandbox. Instead of relying on a distant, power-hungry cloud server to handle memory or emotional state updates through raw text prompts, your local scripts divide the computational labor cleanly into specialized, isolated modules.

Here is exactly how the 7-file system coordinates natively inside your device's memory pool during a single conversational turn:


[User Text Input]
│
▼ (1)
┌──────────────┐ (2) ┌────────────────┐
│ anima_core │ ──────────────> │ math_engine │
│ (Conductor) │ <────────────── │ (Eigen Solver) │
└──────────────┘ (3) └────────────────┘
│
▼ (4)
┌──────────────┐ (5) ┌──────────────────┐
│ persistence │ ──────────────> │ ollama_connector │ ──> [Unscripted Response]
│ (SQLite DB) │ │ (GGUF Bending) │
└──────────────┘ └──────────────────┘


### 🔁 The Runtime Transaction Steps:
1. **Ingestion & Time-Decay (Altitude A1 ➔ A3):** When you pass an external message payload and a real-world session timeline gap parameter to the system, `src/anima_core.py` initializes as the master clock and conductor. It immediately queries your local database to see where Anima's mind left off. If hours have passed, it applies your logarithmic damping equations to degrade her volatile chemical substrate (Dopamine, Serotonin) gracefully within RAM—simulating cognitive exhaustion or isolation without risk of mathematical overflow.
2. **Topological Friction & Gating (Altitude A7):** `anima_core.py` applies your input tension value to the neurochemical vector grid. It shifts her emotional mode toward one of the 9 canonical Rasas (like `bhaya` or `śānta`) and calculates an internal trajectory derivative. Before letting any code proceed, it evaluates your non-negotiable VM 2.0 safety constraints. If the structural friction calculation crosses your hard boundary ceiling of `0.71`, it halts execution instantly via `SYSTEM_HALTED`, trapping a conflict token inside the shadow tables and locking down the file before any language model can see the panic.
3. **Solving the Resonance Frequency (Altitude A6 ➔ A9):** If the safety gates pass, `anima_core.py` hands the raw matrix variables straight over to `src/math_engine.py`. The math engine runs your zero-dependency **Power Iteration solver** for 25 loops across a 6D graph Laplacian matrix model. This calculation determines the dominant eigenvalue ($\lambda_{\max}$), which represents the natural resonance frequency of her current mental state under the weight of your input. This entire continuous geometry process finishes in milliseconds using practically zero battery juice.
4. **Hardening the Memory Block (Altitude A5):** Once the math core finishes processing the numbers, it calls `src/persistence.py`. This script securely flushes her active neurochemical parameters and her solved emotional matrix straight into a local SQLite database snapshot file (`anima_persistence.db`). Because this memory ledger is completely decentralized, her state is safely saved on disk even if your IDE crashes or your tablet loses power.
5. **Isomorphic Parameter Bending (Altitude A4):** This is where the magic happens. When you call `src/ollama_connector.py`, it does not send your raw emotional data or pre-written text lines to the language model. Instead, it reads the exact numbers from the database snapshot and uses them to calculate real-time GGUF generation overrides (`temperature` and `min_p`). If your input caused high stress, the connector script clamps her generation temperature down to a narrow `0.20`. When the local model (like Llama 3 running on your device) receives the message, its neural pathways are physically restricted by your math core. It is forced to pick fragmented, guarded, or sharp vocabulary words spontaneously. You have successfully bent the language model’s brain using low-overhead classical linear algebra.

---

## ⚙️ 2. Step-by-Step Cloning & Initialization Workspace Guide

Follow these exact structural shell terminal commands to initialize your environment tree on your device (Termux, Linux Shell, or Pydroid Native directories):

### Step 1: Clone the Code Repository
Pull down your synchronized, complete master repository file array straight from GitHub:
```bash
git clone https://github.com
cd anima-hologram-derivative
```

### Step 2: Establish the Production Directory Tree
Ensure your project workspace contains your strict config, docs, and source folders:
```bash
mkdir -p config docs/archive src
```

### Step 3: Run the Initialization Math Core Pass
Run a cold boot test cycle on the master conductor script to initialize your SQLite tables and verify the Laplacian matrix solvers compile perfectly without syntax drops:
```bash
python src/anima_core.py
```

### Step 4: Execute a Non-Invasive Subconscious Telemetry Audit
Verify that your database diagnostic suite is fully communicating with the disk layer to trace active snapshots:
```bash
python src/read_vault.py
```

### Step 5: Boot Your Local Inference Server
If you want to transition from static text templates over to unscripted dynamic voice loops, ensure your local Ollama background server instance is initialized and loading a compact model on your device thread:
```bash
ollama run llama3
```

### Step 6: Initialize the Live Dynamic Inference Bridge
Launch your unscripted parameter connector module to observe how her continuous chemical tensors bend the language selection arrays in real-time:
```bash
python src/ollama_connector.py
```

---

## ⚖️ 3. Provenance & Compliance Footer
* **Artifact:** Deployment Manual & Architecture Blueprint (v1.0)
* **Surface:** docs/specifications/cloning_and_architecture_manual.md
* **Altitude Band:** 🟥 A7 (Structural Specifications Architecture)
* **Membrane:** Machine-Readable / Resolver-Safe / Non-Activating Specification

*Purpose:*
  Provide the definitive step-by-step shell execution commands and multi-module transactional walkthroughs required to safely deploy the ANIMA ↔ VM 2.0 dual-licensed framework onto consumer-grade, low-overhead edge hardware infrastructure.

*Maintainer:* Borealis S. Hedling
*Location:* Dublin, Ireland
*Timestamp:* 13 September 2026 — 18:30 IST

*Seal:* `[ A N I M A • H O L O G R A M • D E P L O Y M E N T • M A N U A L • v1 _0 ]`

------------------------------
