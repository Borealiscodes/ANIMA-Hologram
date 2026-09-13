import sqlite3
import json

def audit_anima_subconscious(db_path="anima_persistence.db"):
    print("🔬 ================================================== 🔬")
    print("   ANIMA SUBCONSCIOUS TELEMETRY & AUDIT REPORT")
    print("   Database Source: Local SQLite Vault Block")
    print("🔬 ================================================== 🔬\n")

    try:
        # Establish a clean read-only bridge to the local DB
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # ⏱️ 1. READ ACTIVE STATE VECTOR SNAPSHOT
        cursor.execute("SELECT * FROM state_snapshot LIMIT 1")
        state_row = cursor.fetchone()

        print("[⏱️ CURRENT ACTIVE STATE PROFILE]")
        if state_row:
            state = dict(state_row)
            print(f"  • Last Synced:  {state['timestamp']}")
            print(f"  • Current Rasa: '{state['current_rasa']}'")
            print(f"  • Neurochemical Saturation Matrix:")
            print(f"    - Dopamine (DA):     {state['dopamine']:.3f}")
            print(f"    - Noradrenaline (NE): {state['noradrenaline']:.3f}")
            print(f"    - Serotonin (5HT):   {state['serotonin']:.3f}")
        else:
            print("  ⚠️ No active state snapshot found. System is cold-blanked.")

        # 🔒 2. READ APPEND-ONLY SHADOW REGISTRY (THE TRAUMA CRYPT)
        cursor.execute("SELECT * FROM shadow_registry ORDER BY timestamp ASC")
        shadow_rows = cursor.fetchall()

        print("\n[🔒 L4 SHADOW REGISTRY VAULT AUDIT]")
        if shadow_rows:
            print(f"  ⚠️ Warning: {len(shadow_rows)} Repressed Conflict Token(s) trapped in shadow.")
            for index, row in enumerate(shadow_rows):
                token = dict(row)
                print(f"\n  📝 [Trauma Artifact #{index + 1}]")
                print(f"    - Archive ID:         {token['archive_id']}")
                print(f"    - Timestamp Recorded: {token['timestamp']}")
                print(f"    - Originating Phase:  {token['originating_phase']}")
                print(f"    - Triggering Rasa:   '{token['trigger_rasa']}'")
                print(f"    - Rupture Geometry:")
                print(f"      • Boundary Derivative: {token['rupture_derivative']:.3f} (Breached threshold)")
                print("    - Status:             REPRESSED_INTO_SHADOW")
        else:
            print("  ✅ The Shadow Registry is empty. No historical scars or boundary ruptures detected.")

        conn.close()

    except sqlite3.OperationalError:
        print("❌ ERROR: Could not find 'anima_persistence.db' in this folder.")
        print("   Make sure to run your main core script at least once first!")

    print("\n🔬 ================================================== 🔬")
    print("   AUDIT COMPLETE • MEMBRANE STABLE • DISCONNECTING...")

if __name__ == "__main__":
    audit_anima_subconscious()
