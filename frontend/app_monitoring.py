# Add these imports to frontend/app.py (after existing imports)
import time
import psutil
from datetime import datetime

# Add these global variables after app = Flask(__name__)
start_time = time.time()
request_count = 0
prediction_requests = 0
publish_requests = 0


# Add this middleware after app creation
@app.before_request
def count_requests():
    global request_count
    request_count += 1


# Add these monitoring endpoints to frontend/app.py


@app.route("/dashboard")
def dashboard():
    """Frontend monitoring dashboard"""
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
        <title>🌐 Frontend Web - Monitoring</title>
        <meta http-equiv="refresh" content="5">
        <style>
            body {{ font-family: Arial; margin: 40px; background: #8e44ad; color: white; }}
            .metric {{ background: #9b59b6; padding: 20px; margin: 10px 0; border-radius: 8px; }}
            .value {{ font-size: 2em; font-weight: bold; }}
            .label {{ color: #ecf0f1; margin-top: 5px; }}
            .header {{ text-align: center; margin-bottom: 30px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🌐 Frontend Web Monitoring</h1>
            <p>Port 3000 - User Interface Service</p>
        </div>

        <div class="metric">
            <div class="value">{request_count}</div>
            <div class="label">Total Web Requests</div>
        </div>

        <div class="metric">
            <div class="value">{prediction_requests}</div>
            <div class="label">Prediction Requests</div>
        </div>

        <div class="metric">
            <div class="value">{publish_requests}</div>
            <div class="label">Publish Requests</div>
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

        <p><small>Auto-refresh: 5s | Frontend Service Status</small></p>
    </body>
    </html>
    """


@app.route("/metrics/json")
def metrics_json():
    """Frontend metrics API"""
    uptime = time.time() - start_time
    return {
        "service": "frontend-web",
        "port": 3000,
        "timestamp": datetime.now().isoformat(),
        "uptime_seconds": uptime,
        "requests_total": request_count,
        "prediction_requests": prediction_requests,
        "publish_requests": publish_requests,
        "system": {
            "cpu_percent": psutil.cpu_percent(),
            "memory_percent": psutil.virtual_memory().percent,
            "disk_percent": psutil.disk_usage("/").percent,
        },
        "status": "healthy",
    }


@app.route("/health")
def health_check():
    """Frontend health check"""
    return {
        "status": "healthy",
        "service": "frontend-web",
        "timestamp": datetime.now().isoformat(),
        "backend_url": BACKEND_URL,
    }


# Modify existing routes to count specific actions
# In predict() function, add at the beginning:
# global prediction_requests
# prediction_requests += 1

# In predict_future() function, add at the beginning:
# global prediction_requests
# prediction_requests += 1

# In publish_vehicle() function, add at the beginning:
# global publish_requests
# publish_requests += 1
