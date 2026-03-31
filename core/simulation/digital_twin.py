import random
import time

class DigitalTwinSimulator:
    def __init__(self, facility_id: str):
        self.facility_id = facility_id

    def fetch_live_kpis(self) -> dict:
        """
        Simulates a wide range of live production scenarios using real-time IoT data and monitor KPIs.
        """
        # Generate dummy sensor readings and operational metrics
        return {
            "timestamp": time.time(),
            "machine_utilization_pct": round(random.uniform(65.0, 95.0), 2),
            "production_throughput_units_per_hr": random.randint(120, 200),
            "active_iot_sensors": 42,
            "anomaly_detected": random.choice([True, False, False, False])
        }