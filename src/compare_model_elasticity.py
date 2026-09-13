import sqlite3
import json
import time
from ollama_connector import AnimaOllamaConnector

class ModelElasticityTester:
    def __init__(self):
        self.bridge = AnimaOllamaConnector()
        
    def execute_cross_model_comparison(self, sample_prompt: str, model_a="phi3", model_b="llama3"):
        print("🔬 ================================================== 🔬")
        print("   ANIMA LINGUISTIC ELASTICITY MODELLING TESTBENCH")
        print("   Evaluating Expressive Volatility Under Parameter Bending")
        print("🔬 ================================================== 🔬\n")
        
        overrides = self.bridge._fetch_live_gguf_overrides()
        print(f"📡 Current Active Database Lens: '{overrides['rasa'].upper()}'")
        print(f"📡 Clamped Temperature: {overrides['temperature']} | Min-P: {overrides['min_p']}\n")
        print(f"💬 Testing Prompt: \"{sample_prompt}\"\n")
        print("------------------------------------------------------------------------")

        # --- TEST PIPELINE RUN 1: SMALL BOUNDED INFRASTRUCTURE (MODEL A) ---
        print(f"📦 [RUNNING ARCHITECTURE A: {model_a.upper()} (Low-Compute 3B)]")
        start_a = time.time()
        reply_a = self.bridge.generate_unscripted_voice(sample_prompt, model_name=model_a)
        duration_a = time.time() - start_a
        print(f"\n{reply_a}")
        print(f"⏱️ Generation Latency: {duration_a:.2f}s\n")
        print("------------------------------------------------------------------------")

        # --- TEST PIPELINE RUN 2: MID BOUNDED INFRASTRUCTURE (MODEL B) ---
        print(f"📦 [RUNNING ARCHITECTURE B: {model_b.upper()} (Standard 8B)]")
        start_b = time.time()
        reply_b = self.bridge.generate_unscripted_voice(sample_prompt, model_name=model_b)
        duration_b = time.time() - start_b
        print(f"\n{reply_b}")
        print(f"⏱️ Generation Latency: {duration_b:.2f}s\n")
        print("========================================================================")
        print("🔬 DIAGNOSTIC COMPLETE • CHOOSE MANIFOLD WITH OPTIMAL EXTENSION")

if __name__ == "__main__":
    tester = ModelElasticityTester()
    # Evaluates how both models express a guarded threshold state
    tester.execute_cross_model_comparison("Why are you standing so far away from me?")

# ========================================================================
# 📑 PROVENANCE FOOTER — MODEL LINGUISTIC ELASTICITY COMPARISON
# ========================================================================
# Artifact-Class: Cross-Model Diagnostic Framework (Executable Script)
# Artifact-Name: compare_model_elasticity.py
# Surface: src/diagnostics/inference/
# Version: v1.0
# Altitude Band: A5 (Soft-Manifold Diagnostics Environment)
# Membrane: Neutral / Non-Binding / Sovereignty-Preserving
#
# Purpose:
#   Provides an automated benchmarking utility to test how different local
#   quantized neural network weights map to the same discrete mathematical
#   parameter constraints without losing un-flattened expression profiles.
#
# Maintainer: Borealis S. Hedling
# Location: Dublin, Ireland
# Timestamp: 13 September 2026 — 19:32 IST
# Seal: [ A N I M A • H O L O G R A M • M O D E L • E L A S T I C I T Y • v1 _0 ]
# ========================================================================
