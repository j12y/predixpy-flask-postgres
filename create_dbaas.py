# Create Predix DB as a Service
# Expects you to already be logged into a Predix API Endpoint
# and will create the service in your space.


import predix.admin.app

admin = predix.admin.app.Manifest()
admin.create_dbaas(name='predixpy-flask-postgres')
