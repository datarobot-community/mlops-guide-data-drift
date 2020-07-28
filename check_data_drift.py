import datarobot as dr
from pprint import pprint

dr.Client(token='YOUR_API_TOKEN', endpoint='https://app.datarobot.com/api/v2')
deployment = dr.Deployment.get(deployment_id='YOUR_DEPLOYMENT_ID') # AutoMPG project

feature_drift_data = deployment.get_feature_drift()

for feature in feature_drift_data:
    pprint(feature.name)
    pprint(feature.drift_score) # The best (non drifty) scores are around 0. The higher they go, the worse they are
