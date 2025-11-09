#!/usr/bin/env python3
"""Send continuous data flow to Splunk Observability Cloud for 10 minutes"""

import requests
import time
import random
import math
from datetime import datetime

ORG_TOKEN = "PZuf3J0L2Op_Qj9hpAJzlw"
REALM = "us1"
BASE_URL = f"https://ingest.{REALM}.signalfx.com/v2/datapoint"

def send_metrics_batch():
    """Send a batch of different metrics"""
    headers = {
        "Content-Type": "application/json",
        "X-SF-Token": ORG_TOKEN
    }

    current_time = int(time.time() * 1000)

    # Generate realistic data
    cpu_usage = random.uniform(10, 90)
    memory_usage = random.uniform(30, 85)
    requests_per_sec = random.randint(5, 50)
    response_time = random.uniform(50, 500)
    predictions_made = random.randint(0, 10)
    error_rate = random.uniform(0, 5)

    # Car price specific metrics
    avg_prediction_value = random.uniform(15000, 45000)
    active_users = random.randint(1, 25)
    database_connections = random.randint(2, 15)

    payload = {
        "gauge": [
            {
                "metric": "car_price.system.cpu_percent",
                "value": cpu_usage,
                "dimensions": {
                    "service": "car-price-backend",
                    "host": "server-01",
                    "environment": "demo"
                },
                "timestamp": current_time
            },
            {
                "metric": "car_price.system.memory_percent",
                "value": memory_usage,
                "dimensions": {
                    "service": "car-price-backend",
                    "host": "server-01",
                    "environment": "demo"
                },
                "timestamp": current_time
            },
            {
                "metric": "car_price.api.response_time_ms",
                "value": response_time,
                "dimensions": {
                    "service": "car-price-backend",
                    "endpoint": "predict",
                    "environment": "demo"
                },
                "timestamp": current_time
            },
            {
                "metric": "car_price.business.avg_prediction_value",
                "value": avg_prediction_value,
                "dimensions": {
                    "service": "car-price-backend",
                    "currency": "USD",
                    "environment": "demo"
                },
                "timestamp": current_time
            },
            {
                "metric": "car_price.users.active_count",
                "value": active_users,
                "dimensions": {
                    "service": "car-price-frontend",
                    "environment": "demo"
                },
                "timestamp": current_time
            },
            {
                "metric": "car_price.database.connections",
                "value": database_connections,
                "dimensions": {
                    "service": "car-price-backend",
                    "database": "vehiculos_db",
                    "environment": "demo"
                },
                "timestamp": current_time
            },
            {
                "metric": "car_price.api.error_rate_percent",
                "value": error_rate,
                "dimensions": {
                    "service": "car-price-backend",
                    "environment": "demo"
                },
                "timestamp": current_time
            }
        ],
        "counter": [
            {
                "metric": "car_price.api.requests_total",
                "value": requests_per_sec,
                "dimensions": {
                    "service": "car-price-backend",
                    "method": "GET",
                    "endpoint": "current_value_market",
                    "environment": "demo"
                },
                "timestamp": current_time
            },
            {
                "metric": "car_price.ml.predictions_total",
                "value": predictions_made,
                "dimensions": {
                    "service": "car-price-backend",
                    "model": "xgboost",
                    "environment": "demo"
                },
                "timestamp": current_time
            },
            {
                "metric": "car_price.frontend.page_views",
                "value": random.randint(1, 8),
                "dimensions": {
                    "service": "car-price-frontend",
                    "page": "prediction_form",
                    "environment": "demo"
                },
                "timestamp": current_time
            }
        ]
    }

    try:
        response = requests.post(BASE_URL, json=payload, headers=headers, timeout=5)
        return response.status_code == 200, len(payload["gauge"]) + len(payload["counter"])
    except Exception as e:
        print(f"❌ Error: {e}")
        return False, 0

def run_data_flow():
    """Run continuous data flow for 10 minutes"""
    print("🚀 Starting 10-minute data flow to Splunk Observability Cloud")
    print("=" * 70)
    print(f"📊 Target: {BASE_URL}")
    print(f"⏰ Duration: 10 minutes (600 seconds)")
    print(f"📈 Frequency: Every 1 second")
    print(f"📋 Metrics per batch: 10 different metrics")
    print("=" * 70)

    start_time = time.time()
    end_time = start_time + (10 * 60)  # 10 minutes

    total_batches = 0
    successful_batches = 0
    total_metrics = 0

    while time.time() < end_time:
        current_time = time.time()
        elapsed = current_time - start_time
        remaining = end_time - current_time

        # Send metrics batch
        success, metric_count = send_metrics_batch()
        total_batches += 1
        total_metrics += metric_count

        if success:
            successful_batches += 1
            status = "✅"
        else:
            status = "❌"

        # Progress display
        progress = (elapsed / (10 * 60)) * 100
        print(f"{status} Batch {total_batches:3d} | "
              f"Progress: {progress:5.1f}% | "
              f"Elapsed: {elapsed:6.1f}s | "
              f"Remaining: {remaining:6.1f}s | "
              f"Success: {successful_batches}/{total_batches}")

        # Wait 1 second
        time.sleep(1)

    print("\n" + "=" * 70)
    print("🎉 Data flow completed!")
    print(f"📊 Total batches sent: {total_batches}")
    print(f"✅ Successful batches: {successful_batches}")
    print(f"📈 Total metrics sent: {total_metrics}")
    print(f"📉 Success rate: {(successful_batches/total_batches)*100:.1f}%")
    print("\n🔍 Check your Splunk Observability Cloud dashboard:")
    print("   • Metric Finder → Search for 'car_price'")
    print("   • Dashboards → Create Dashboard → Add charts")
    print("   • Look for these metric patterns:")
    print("     - car_price.system.*")
    print("     - car_price.api.*")
    print("     - car_price.ml.*")
    print("     - car_price.business.*")
    print("     - car_price.users.*")

if __name__ == "__main__":
    try:
        run_data_flow()
    except KeyboardInterrupt:
        print("\n\n⏹️  Data flow stopped by user")
        print("🔍 Check your dashboard for the data that was sent")
