import json

with open('dashboard.json') as f:
    dashboard = json.load(f)

with open('config.json') as f:
    config = json.load(f)

dashboard_name = config['dashboard_name']
dashboard_uid = config['dashboard_uid']

dashboard['title'] = dashboard_name
dashboard['uid'] = dashboard_uid

targets = config['targets']

panels = []
for i, target in enumerate(targets):
    panel_name = target.strip().replace(".", "_").replace("://", "_")
    panel = {
        "datasource": {
            "type": "prometheus",
            "uid": "c8edec62-84c2-4f31-949d-a8a0da06764f"
        },
        "fieldConfig": {
            "defaults": {
                "color": {
                    "mode": "palette-classic"
                },
                "mappings": [
                    {
                        "options": {
                            "from": 0,
                            "result": {
                                "color": "dark-red",
                                "index": 0
                            },
                            "to": 80
                        },
                        "type": "range"
                    },
                    {
                        "options": {
                            "from": 80,
                            "result": {
                                "color": "dark-orange",
                                "index": 1
                            },
                            "to": 95
                        },
                        "type": "range"
                    },
                    {
                        "options": {
                            "from": 95,
                            "result": {
                                "color": "dark-green",
                                "index": 2
                            },
                            "to": 100
                        },
                        "type": "range"
                    }
                ],
                "thresholds": {
                    "mode": "percentage",
                    "steps": [
                        {
                            "color": "dark-green",
                            "value": None
                        },
                        {
                            "color": "dark-orange",
                            "value": 80
                        }
                    ]
                }
            },
            "overrides": []
        },
        "gridPos": {
           "h": 6,
           "w": 6,  
           "x": (i % 4) * 6,  
           "y": int(i / 4) * 6
        },
        "id": i + 1,
        "options": {
            "orientation": "vertical",
            "reduceOptions": {
                "calcs": [
                    "lastNotNull"
                ],
                "fields": "",
                "values": False
            },
            "showThresholdLabels": False,
            "showThresholdMarkers": False
        },
        "pluginVersion": "9.5.1",
        "targets": [
            {
                "datasource": {
                    "type": "prometheus",
                    "uid": "c8edec62-84c2-4f31-949d-a8a0da06764f"
                },
                "editorMode": "code",
                "expr": f'100 * sum_over_time(probe_success{{instance=~"{target}"}}[$__range]) /   count_over_time(scrape_duration_seconds[$__range])',
                "legendFormat": "__auto",
                "range": True,
                "refId": "A"
            }
        ],
        "title": panel_name,
        "type": "gauge"
    }
    panels.append(panel)

dashboard['panels'] = panels

with open('new_dashboard.json', 'w') as f:
    json.dump(dashboard, f)
