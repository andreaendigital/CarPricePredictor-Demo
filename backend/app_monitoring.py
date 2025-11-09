# Add these imports to backend/app.py (after existing imports)
import time
import psutil
from datetime import datetime

# Add these global variables after CORS setup
start_time = time.time()
request_count = 0
prediction_count = 0


# Add this middleware after CORS setup
@app.before_request
def count_requests():
    global request_count
    request_count += 1


# Add these monitoring endpoints to backend/app.py


@app.route("/dashboard")
def dashboard():
    """Backend monitoring dashboard"""
    uptime = time.time() - start_time
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent

    cpu_color = "#e74c3c" if cpu_usage > 80 else "#f39c12" if cpu_usage > 60 else "#27ae60"
    mem_color = "#e74c3c" if memory_usage > 80 else "#f39c12" if memory_usage > 60 else "#27ae60"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>🚗 Backend API - Monitoring</title>
        <meta http-equiv="refresh" content="5">
        <style>
            body {{ font-family: Arial; margin: 40px; background: #2c3e50; color: white; }}
            .metric {{ background: #34495e; padding: 20px; margin: 10px 0; border-radius: 8px; }}
            .value {{ font-size: 2em; font-weight: bold; }}
            .label {{ color: #bdc3c7; margin-top: 5px; }}
            .header {{ text-align: center; margin-bottom: 30px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🔧 Backend API Monitoring</h1>
            <p>Port 5002 - ML Prediction Service</p>
        </div>

        <div class="metric">
            <div class="value">{request_count}</div>
            <div class="label">Total API Requests</div>
        </div>

        <div class="metric">
            <div class="value">{prediction_count}</div>
            <div class="label">ML Predictions Made</div>
        </div>

        <div class="metric">
            <div class="value" style="color: {cpu_color}">{cpu_usage:.1f}%</div>
            <div class="label">CPU Usage</div>
        </div>

        <div class="metric">
            <div class="value" style="color: {mem_color}">{memory_usage:.1f}%</div>
            <div class="label">Memory Usage</div>
        </div>

        <div class="metric">
            <div class="value">{int(uptime//3600)}h {int((uptime%3600)//60)}m</div>
            <div class="label">Uptime</div>
        </div>

        <p><small>Auto-refresh: 5s | Backend Service Status</small></p>
    </body>
    </html>
    """


@app.route("/metrics/json")
def metrics_json():
    """Backend metrics API"""
    uptime = time.time() - start_time
    return jsonify(
        {
            "service": "backend-api",
            "port": 5002,
            "timestamp": datetime.now().isoformat(),
            "uptime_seconds": uptime,
            "requests_total": request_count,
            "predictions_total": prediction_count,
            "system": {
                "cpu_percent": psutil.cpu_percent(),
                "memory_percent": psutil.virtual_memory().percent,
                "disk_percent": psutil.disk_usage("/").percent,
            },
            "status": "healthy",
        }
    )


@app.route("/health")
def health_check():
    """Backend health check"""
    return jsonify(
        {
            "status": "healthy",
            "service": "backend-api",
            "timestamp": datetime.now().isoformat(),
            "model_loaded": modelo is not None,
        }
    )


# Modify existing prediction endpoints to count predictions
# In current_value_market() function, add after data validation:
# global prediction_count
# prediction_count += 1

# In future_prediction() function, add after data validation:
# global prediction_count
# prediction_count += 1
