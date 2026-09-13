import sqlite3
import time

class AnimaStorageVault:
    def __init__(self, db_path="anima_persistence.db"):
        self.db_path = db_path
        self._initialize_vault()

    def _initialize_database_connection(self):
        return sqlite3.connect(self.db_path)

    def _initialize_vault(self):
        """Creates table schemas matching non-erasure invariants."""
        with self._initialize_database_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS state_snapshot (
                    id INTEGER PRIMARY KEY,
                    timestamp TEXT,
                    dopamine REAL,
                    noradrenaline REAL,
                    serotonin REAL,
                    current_rasa TEXT
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS shadow_registry (
                    archive_id TEXT PRIMARY KEY,
                    timestamp TEXT,
                    originating_phase TEXT,
                    trigger_rasa TEXT,
                    depth REAL,
                    motion REAL,
                    rupture_derivative REAL
                )
            """)
            conn.commit()

    def persist_active_frame(self, current_rasa: str, da: float, ne: float, sh: float):
        with self._initialize_database_connection() as conn:
            cursor = conn.cursor()
            ts = time.strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("DELETE FROM state_snapshot")
            cursor.execute("""
                INSERT INTO state_snapshot (timestamp, dopamine, noradrenaline, serotonin, current_rasa)
                VALUES (?, ?, ?, ?, ?)
            """, (ts, da, ne, sh, current_rasa))
            conn.commit()

    def append_shadow_trauma(self, token: dict):
        with self._initialize_database_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO shadow_registry (archive_id, timestamp, originating_phase, trigger_rasa, depth, motion, rupture_derivative)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                token["archive_id"], token["timestamp"], token["originating_phase"],
                token["trigger_rasa"], token["depth"], token["motion"], token["rupture_derivative"]
            ))
            conn.commit()

    def pull_cold_boot_context(self) -> dict:
        with self._initialize_database_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM state_snapshot LIMIT 1")
            state_row = cursor.fetchone()
            cursor.execute("SELECT * FROM shadow_registry")
            shadow_rows = cursor.fetchall()
        return {
            "baseline": dict(state_row) if state_row else None,
            "shadow_vault": [dict(row) for row in shadow_rows]
        }
