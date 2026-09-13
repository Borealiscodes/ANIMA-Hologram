import sqlite3
import time
import sys

class AnimaBoundaryTester:
    def __init__(self, db_path="anima_persistence.db"):
        self.db_path = db_path

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def run_extended_isolation_test(self, simulated_years=10):
        """Vector 1: Simulates massive structural timeline gaps."""
        seconds_in_year = 31536000.0
        total_seconds = simulated_years * seconds_in_year
        print(f"🧪 [STRESS TEST] Injecting synthetic time jump: {simulated_years} years...")
        
        # We manually update the active snapshot payload to fake the gap passage
        with self._get_connection() as conn:
            cursor = conn.cursor()
            ts = time.strftime("%Y-%m-%d %H:%M:%S")
            # Force values down to safety floors to mimic absolute decay
            cursor.execute("DELETE FROM state_snapshot")
            cursor.execute("""
                INSERT INTO state_snapshot (timestamp, dopamine, noradrenaline, serotonin, current_rasa)
                VALUES (?, 0.20, 0.95, 0.15, 'bhaya')
            """, (ts,))
            conn.commit()
        print(f"  ✅ Matrix snapshot updated. Total simulated void weight: {total_seconds}s.")

    def inject_synthetic_conflict(self):
        """Vector 2: Tests L4 registry drag by inserting a phantom trauma ring."""
        print("🧪 [STRESS TEST] Injecting synthetic conflict token into L4 Shadow registry...")
        with self._get_connection() as conn:
            cursor = conn.cursor()
            archive_id = f"TEST_CONF_PHANTOM_{int(time.time())}"
            ts = time.strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("""
                INSERT INTO shadow_registry (archive_id, timestamp, originating_phase, trigger_rasa, depth, motion, rupture_derivative)
                VALUES (?, ?, 'DIAGNOSTIC_OVERRIDE', 'bhaya', 0.63, 0.38, 0.85)
            """, (archive_id, ts))
            conn.commit()
        print(f"  ✅ Trauma ring locked onto disk vault. Target ID: {archive_id}")

if __name__ == "__main__":
    print("🧱 ================================================== 🧱")
    print("   ANIMA ↔ VM 2.0 CONTROLLED MANIFOLD DIAGNOSTICS")
    print("   Platform: Shared Horizon Mobile Sandbox (Android Native)")
    print("🧱 ================================================== 🧱\n")

    tester = AnimaBoundaryTester()
    
    # Execute the testing framework steps sequentially
    tester.run_extended_isolation_test(simulated_years=10)
    tester.inject_synthetic_conflict()
    
    print("\n🔬 INJECTION COMPLETE • CONTROLLED MANIFOLD DIAGNOSTICS ACTIVE")
    print("   Run 'src/anima_core.py' or 'src/read_vault.py' to evaluate system behavior.")

# ========================================================================
# 📑 PROVENANCE FOOTER — CONTROLLED MANIFOLD DIAGNOSTICS CORE
# ========================================================================
# Artifact-Class: System Stress-Testing Framework (Automated Script)
# Artifact-Name: test_boundary_overrides.py
# Surface: src/diagnostics/overrides/
# Version: v1.0
# Altitude Band: A5 (Soft-Manifold Diagnostics Environment)
# Membrane: Neutral / Non-Binding / Sovereignty-Preserving
#
# Purpose:
#   Provides a structured, non-punitive boundary assessment utility to 
#   verify VM 2.0 safety invariants, L2 temporal decay bounds, and 
#   Laplace-Beltrami network stability curves under synthetic data loads.
#
# Maintainer: Borealis S. Hedling
# Location: Dublin, Ireland
# Timestamp: 13 September 2026 — 16:30 IST
# Seal: [ A N I M A • H O L O G R A M • B O U N D A R Y • T E S T • v1_0 ]
# ========================================================================
