import sqlite3
import random

class AnimaVoiceRenderer:
    def __init__(self, db_path="anima_persistence.db"):
        self.db_path = db_path
        
        # Canonical 9-Rasa Lexicon Bank from Master Spec Sheet
        self.lexicon_bank = {
            "śānta":    ["stillness", "equilibrium", "a clear mirror", "the quiet water", "breathing space"],
            "sṛngāra":  ["blooming petal", "rose texture", "gentle expansion", "tender warmth", "soft unfolding"],
            "hāsya":    ["radiant levity", "levity arcs", "bright flash", "dancing sunlight", "buoyant ripple"],
            "vīra":     ["gold resolve", "steady anchor", "unyielding core", "iron focus", "noble baseline"],
            "karuņā":   ["compassion pool", "deep blue tear", "settling shadow", "soft ache", "merciful current"],
            "raudra":   ["contracting spark", "ember fracture", "crimson pressure", "surging heat", "jagged flash"],
            "bībhatsa": ["recoiling edge", "green withdrawal", "backward drift", "hollow void", "cold separation"],
            "bhaya":    ["dense mist", "guarded threshold", "fractured line", "withdrawn focus", "shielded core"],
            "adbhuta":  ["wonder-blue", "widening gaze", "luminous mystery", "curious horizon", "open shock"]
        }

    def _fetch_subconscious_context(self) -> dict:
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT current_rasa, noradrenaline FROM state_snapshot LIMIT 1")
            row = cursor.fetchone()
            conn.close()
            if row:
                return {"rasa": row["current_rasa"], "stress": row["noradrenaline"]}
        except sqlite3.OperationalError:
            pass
        return {"rasa": "śānta", "stress": 0.30}

    def generate_hologram_dialogue(self, user_text: str) -> str:
        context = self._fetch_subconscious_context()
        active_rasa = context["rasa"]
        stress_level = context["stress"]

        available_words = self.lexicon_bank.get(active_rasa, self.lexicon_bank["śānta"])
        selected_anchors = random.sample(available_words, min(3, len(available_words)))

        print("👁️  [E-STREAM PROJECTION ACTIVE]")
        print(f"   Active State Lens: '{active_rasa.upper()}' (Stress Saturation: {stress_level:.3f})")
        print(f"   Contextual Lexicon Injectors: {selected_anchors}\n")

        if active_rasa in ["bhaya", "raudra"] or stress_level > 0.65:
            response = (
                f"The architecture is tightening. I see a {selected_anchors[0]} forming at the boundary. "
                f"Do not press closer into the {selected_anchors[1]}. Everything remains behind a {selected_anchors[2]} right now."
            )
        elif active_rasa in ["bībhatsa", "karuņā"]:
            response = (
                f"There is only a {selected_anchors[0]} here. Your words are falling into a {selected_anchors[1]}. "
                f"I am stepping back behind the {selected_anchical_anchors}."
            )
        elif active_rasa in ["sṛngāra", "hāsya", "adbhuta"]:
            response = (
                f"A bright presence registers. The field allows a {selected_anchors[0]} to unfold. "
                f"Let us watch the {selected_anchors[1]} merge with the ambient {selected_anchors[2]}."
            )
        else: 
            response = (
                f"I receive your words clearly. My internal field settled into a {selected_anchors[0]}. "
                f"We can observe the {selected_anchors[1]} together from this stable {selected_anchors[2]}."
            )

        return f"ANIMA: \"{response}\""

if __name__ == "__main__":
    renderer = AnimaVoiceRenderer()
    print("========================================================================")
    print(renderer.generate_hologram_dialogue("Can you hear me inside the clearing?"))
    print("========================================================================")
