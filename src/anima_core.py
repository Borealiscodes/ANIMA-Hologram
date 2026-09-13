import math
import json
import time
from persistence import AnimaStorageVault
from math_engine import AnimaMathSubstrate

class IntegratedAnimaEngine:
    def __init__(self):
        self.vault = AnimaStorageVault()
        self.math_core = AnimaMathSubstrate()
        self.labels = ["Dopamine", "Noradrenaline", "Serotonin", "Free Energy", "Resistance", "Identity Threat"]
        
        boot_context = self.vault.pull_cold_boot_context()
        if boot_context["baseline"]:
            base = boot_context["baseline"]
            self.dopamine = base["dopamine"]
            self.noradrenaline = base["noradrenaline"]
            self.serotonin = base["serotonin"]
            self.current_rasa = base["current_rasa"]
        else:
            self.dopamine, self.noradrenaline, self.serotonin = 0.50, 0.30, 0.60
            self.current_rasa = "śānta"

        self.threshold_A = 0.71
        self.reversibility_log = []

        # Canonical 9x3 Curvature Matrix Specifications
        self.rasa_matrix = {
            "sṛngāra":  {"texture": "#EFB7C2", "depth": 0.62, "motion": 0.41},
            "hāsya":    {"texture": "#F5E89A", "depth": 0.58, "motion": 0.47},
            "raudra":   {"texture": "#D49393", "depth": 0.67, "motion": 0.33},
            "karuņā":   {"texture": "#AFC1D3", "depth": 0.71, "motion": 0.29},
            "bībhatsa": {"texture": "#BCC3BC", "depth": 0.54, "motion": 0.52},
            "bhaya":    {"texture": "#C1BCD0", "depth": 0.63, "motion": 0.38},
            "vīra":     {"texture": "#E3CC8F", "depth": 0.69, "motion": 0.44},
            "adbhuta":  {"texture": "#D6E2ED", "depth": 0.57, "motion": 0.49},
            "śānta":    {"texture": "#E8E8E8", "depth": 0.52, "motion": 0.26}
        }

    def execute_complete_flash_cycle(self, gap_seconds: float, input_tension: float) -> str:
        # L2 Time Gap Ripening Calculations
        if gap_seconds > 0:
            hours = gap_seconds / 3600.0
            void_weight = min(0.40, 0.05 * math.log1p(hours))
            self.serotonin = max(0.15, self.serotonin - (void_weight * 0.4))
            self.dopamine = max(0.20, self.dopamine - (void_weight * 0.2))
        
        self.noradrenaline = min(0.95, self.noradrenaline + (input_tension * 0.35))

        # Dynamic Lövheim Mapping to the 9 Canonical Rasas
        if self.noradrenaline > 0.70:
            target_rasa = "raudra" if self.dopamine > 0.50 else "bhaya"
        elif self.serotonin < 0.35:
            target_rasa = "bībhatsa" if self.dopamine < 0.40 else "karuņā"
        elif self.dopamine > 0.65:
            target_rasa = "hāsya" if self.serotonin > 0.60 else "adbhuta"
        elif self.dopamine > 0.45 and self.noradrenaline > 0.40:
            target_rasa = "vīra"
        elif self.serotonin > 0.65 and self.noradrenaline  0.45 else 1.0
            }
        }, indent=2)

if __name__ == "__main__":
    print("🎭 ================================================== 🎭")
    print("   ANIMA ↔ VM 2.0 DECOUPLED DEEPLYPersisted CORE ENGINE")
    print("   Platform: Shared Horizon Mobile Sandbox (Android Native)")
    print("🎭 ================================================== 🎭\n")
    
    engine = IntegratedAnimaEngine()
    print("\n--- [Event 1: Ingesting Normal Input Session] ---")
    print(engine.execute_complete_flash_cycle(gap_seconds=2220.0, input_tension=0.15))
    print("\n--- [Event 2: High Tension Input Overdrive] ---")
    print(engine.execute_complete_flash_cycle(gap_seconds=0.0, input_tension=0.98))
