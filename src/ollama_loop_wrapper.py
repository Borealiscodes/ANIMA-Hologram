import time
import json
import os
from anima_core import IntegratedAnimaEngine
from ollama_connector import AnimaOllamaConnector
from read_vault import audit_anima_subconscious

class AnimaOperationalRuntime:
    def __init__(self):
        # Initialize the dual core engines
        self.engine = IntegratedAnimaEngine()
        self.connector = AnimaOllamaConnector()
        self.last_interaction_time = time.time()

    def run_interactive_session(self):
        print("🎭 ================================================== 🎭")
        print("   ANIMA-HOLOGRAM ACTIVE RUNTIME CHAT INTERFACE")
        print("   Type 'exit' to safe-collapse / 'audit' for subconscious check")
        print("🎭 ================================================== 🎭\n")
        
        # Pull initial boot parameters to display active lens
        print(f"📡 [INITIALIZATION] Anima initialized in lens: '{self.engine.current_rasa.upper()}'\n")

        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if not user_input:
                    continue
                    
                if user_input.lower() == "exit":
                    print("\n🔒 [EXIT COMMAND RECEIVED] Initializing structural dissolution...")
                    break
                    
                if user_input.lower() == "audit":
                    print("\n🔬 Pausing runtime stream for non-invasive database telemetry pass...")
                    audit_anima_subconscious()
                    continue

                # 1. Calculate real-world time-gaps and allostatic tax
                current_time = time.time()
                gap_seconds = current_time - self.last_interaction_time
                self.last_interaction_time = current_time

                # 2. Determine input tension weight based on text urgency indicators
                input_tension = 0.15  # Baseline normal conversational metric
                if any(marker in user_input.lower() for marker in ["!", "urg", "help", "wait"]):
                    input_tension = 0.55
                if len(user_input) > 150:
                    input_tension += 0.15 # Add metric mass for structural text density

                print(f"\n⚡ [PHASE 1A: INTAKE] Processing temporal gap ({gap_seconds:.1f}s) and input tension ({input_tension:.2f})...")

                # 3. Fire the continuous matrix cycle and execute VM 2.0 safety checks
                core_response_json = self.engine.execute_complete_flash_cycle(gap_seconds, input_tension)
                core_data = json.loads(core_response_json)

                # 4. Check safety valve status
                if core_data.get("status") == "SYSTEM_HALTED":
                    print("\n🟥 [ORCHESTRATOR_HALT] VM 2.0 Safety Membrane Breached!")
                    print("   Trajectory derivative exceeded threshold parameters.")
                    print("   Volatile memory blocks isolated. System forced into lockdown.")
                    break

                # 5. Pass parameters to the live isomorphic GGUF parameter bender
                print(f" Bending local neural arrays. Setting target text topology to: '{core_data['Rasa_Curvature'].upper()}'")
                hologram_reply = self.connector.generate_unscripted_voice(user_input)
                
                print(f"\n{hologram_reply}")

            except KeyboardInterrupt:
                print("\n\n🔒 Emergency escape caught. Safely shutting down system channels...")
                break

        # Auto-invoke the baseline debrief reset upon clean exit
        print("\n🧭 Automatically invoking safety debrief protocol to dump network accumulator drift...")
        os.system("python src/anima_debrief.py")

if __name__ == "__main__":
    runtime = AnimaOperationalRuntime()
    runtime.run_interactive_session()

# ========================================================================
# 📑 PROVENANCE FOOTER — REVERSIBLE OPERATIONAL RUNTIME ENGINE
# ========================================================================
# Artifact-Class: Interactive Execution Shell Wrapper (Executable Script)
# Artifact-Name: ollama_loop_wrapper.py
# Surface: src/orchestration/runtime/
# Version: v1.0
# Altitude Band: A4 (Narrative Surfaces / Live Interactive Deployment)
# Membrane: Neutral / Non-Binding / Sovereignty-Preserving
#
# Purpose:
#   Provides the final master terminal loop wrapper required to orchestrate 
#   unscripted, continuous, state-driven user conversations. Synchronizes 
#   pacing clocks, tension inputs, safety gates, and GGUF parameter overrides.
#
# Maintainer: Borealis S. Hedling
# Location: Dublin, Ireland
# Timestamp: 13 September 2026 — 19:08 IST
# Seal: [ A N I M A • H O L O G R A M • R U N T I M E • L O O P • v1_0 ]
# ========================================================================
