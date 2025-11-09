# 📊 Monitoring Implementation Guide

## Files to Modify for Car Price Prediction App

Based on your application structure, here are the **exact files** you need to modify:

## 📁 **Files to Change**

### **1. Backend App** (`/backend/app.py`)

Add these imports after existing imports:
```python
import time
import psutil
from datetime import datetime
```

Add these global variables after `CORS(app)`:
```python
start_time = time.time()
request_count = 0
prediction_count = 0

@app.before_request
def count_requests():
    global request_count
    request_count += 1
```

Add these monitoring endpoints before `if __name__ == "__main__"`:
```python
@app.route("/dashboard")
def dashboard():
    uptime = time.time() - start_time
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>🔧 Backend API - Monitoring</title>
        <meta http-equiv="refresh" content="5">
        <style>
            body {{ font-family: Arial; margin: 40px; background: #2c3e50; color: white; }}
            .metric {{ background: #34495e; padding: 20px; margin: 10px 0; border-radius: 8px; }}
            .value {{ font-size: 2em; font-weight: bold; color: #3498db; }}
            .label {{ color: #bdc3c7; margin-top: 5px; }}
        </style>
    </head>
    <body>
        <h1>🔧 Backend API Monitoring (Port 5002)</h1>
        <div class="metric">
            <div class="value">{request_count}</div>
            <div class="label">Total API Requests</div>
        </div>
        <div class="metric">
            <div class="value">{prediction_count}</div>
            <div class="label">ML Predictions Made</div>
        </div>
        <div class="metric">
            <div class="value">{cpu_usage:.1f}%</div>
            <div class="label">CPU Usage</div>
        </div>
        <div class="metric">
            <div class="value">{memory_usage:.1f}%</div>
            <div class="label">Memory Usage</div>
        </div>
        <div class="metric">
            <div class="value">{int(uptime//3600)}h {int((uptime%3600)//60)}m</div>
            <div class="label">Uptime</div>
        </div>
    </body>
    </html>
    '''

@app.route("/metrics/json")
def metrics_json():
    uptime = time.time() - start_time
    return jsonify({
        'service': 'backend-api',
        'port': 5002,
        'timestamp': datetime.now().isoformat(),
        'uptime_seconds': uptime,
        'requests_total': request_count,
        'predictions_total': prediction_count,
        'system': {
            'cpu_percent': psutil.cpu_percent(),
            'memory_percent': psutil.virtual_memory().percent
        },
        'status': 'healthy'
    })

@app.route("/health")
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'backend-api',
        'timestamp': datetime.now().isoformat(),
        'model_loaded': modelo is not None
    })
```

Modify prediction endpoints to count predictions:
```python
# In current_value_market() function, add after data validation:
global prediction_count
prediction_count += 1

# In future_prediction() function, add after data validation:
global prediction_count
prediction_count += 1
```

### **2. Frontend App** (`/frontend/app.py`)

Add these imports after existing imports:
```python
import time
import psutil
from datetime import datetime
```

Add these global variables after `app = Flask(__name__)`:
```python
start_time = time.time()
request_count = 0
prediction_requests = 0
publish_requests = 0

@app.before_request
def count_requests():
    global request_count
    request_count += 1
```

Add these monitoring endpoints before `if __name__ == "__main__"`:
```python
@app.route("/dashboard")
def dashboard():
    uptime = time.time() - start_time
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>🌐 Frontend Web - Monitoring</title>
        <meta http-equiv="refresh" content="5">
        <style>
            body {{ font-family: Arial; margin: 40px; background: #8e44ad; color: white; }}
            .metric {{ background: #9b59b6; padding: 20px; margin: 10px 0; border-radius: 8px; }}
            .value {{ font-size: 2em; font-weight: bold; color: #ecf0f1; }}
            .label {{ color: #ecf0f1; margin-top: 5px; }}
        </style>
    </head>
    <body>
        <h1>🌐 Frontend Web Monitoring (Port 3000)</h1>
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
            <div class="value">{cpu_usage:.1f}%</div>
            <div class="label">CPU Usage</div>
        </div>
        <div class="metric">
            <div class="value">{memory_usage:.1f}%</div>
            <div class="label">Memory Usage</div>
        </div>
        <div class="metric">
            <div class="value">{int(uptime//3600)}h {int((uptime%3600)//60)}m</div>
            <div class="label">Uptime</div>
        </div>
    </body>
    </html>
    '''

@app.route("/metrics/json")
def metrics_json():
    uptime = time.time() - start_time
    return {
        'service': 'frontend-web',
        'port': 3000,
        'timestamp': datetime.now().isoformat(),
        'uptime_seconds': uptime,
        'requests_total': request_count,
        'prediction_requests': prediction_requests,
        'publish_requests': publish_requests,
        'system': {
            'cpu_percent': psutil.cpu_percent(),
            'memory_percent': psutil.virtual_memory().percent
        },
        'status': 'healthy'
    }

@app.route("/health")
def health_check():
    return {
        'status': 'healthy',
        'service': 'frontend-web',
        'timestamp': datetime.now().isoformat(),
        'backend_url': BACKEND_URL
    }
```

Modify existing routes to count specific actions:
```python
# In predict() function, add at the beginning:
global prediction_requests
prediction_requests += 1

# In predict_future() function, add at the beginning:
global prediction_requests
prediction_requests += 1

# In publish_vehicle() function, add at the beginning:
global publish_requests
publish_requests += 1
```

### **3. Requirements File** (`requirements.txt`)

Add this line to the end of the file:
```txt
psutil==5.9.0
```

### **4. Ansible Configuration** (`configManagement-carPrice/roles/flask_app/tasks/main.yml`)

Add this task after the "Install Python dependencies" task:
```yaml
- name: Install psutil for system monitoring
  shell: |
    source venv/bin/activate
    pip install psutil==5.9.0
  args:
    chdir: "{{ app_dest }}"
  become: true
```

## 🚀 **Access Your Monitoring**

After deployment, access:

- **Backend Dashboard**: `http://your-ec2-ip:5002/dashboard`
- **Frontend Dashboard**: `http://your-ec2-ip:3000/dashboard`
- **Backend JSON API**: `http://your-ec2-ip:5002/metrics/json`
- **Frontend JSON API**: `http://your-ec2-ip:3000/metrics/json`
- **Health Checks**: `http://your-ec2-ip:5002/health` and `http://your-ec2-ip:3000/health`

## 📊 **What You'll See**

- **Real-time metrics** with auto-refresh every 5 seconds
- **System monitoring**: CPU, Memory, Uptime
- **Application metrics**: Request counts, predictions made
- **Service status**: Health checks for both services
- **Different themes**: Backend (dark blue) and Frontend (purple)

## ⚡ **Summary**

**Total files to modify: 4**
1. `backend/app.py` - Add backend monitoring
2. `frontend/app.py` - Add frontend monitoring
3. `requirements.txt` - Add psutil dependency
4. `configManagement-carPrice/roles/flask_app/tasks/main.yml` - Install psutil via Ansible

**Setup time: 10 minutes**
**Zero infrastructure changes needed**
