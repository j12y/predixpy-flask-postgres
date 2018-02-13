
# Overview

This is a simple demo of using Cloud Foundry, Flask, and Predix Database as a
Service.

## Requirements

- [ ] You must have at minimum a [Predix Free Tier](signup) account.
- [ ] You must have the [Cloud Foundry CLI](cf) and can run `cf login`
- [ ] You will need to create an instance of Predix Database as a Service in your space (this
  is not a free service)

# Setup

This app will not run locally and must be pushed to the Predix cloud.

**(1) Get the source code.**

```
git clone https://github.com/j12y/predixpy-flask-postgres.git
cd predixpy-flask-postgres
```

**(2) Initialize the service.**

If you don't already have it, install the Predix Python SDK into your
environment.

```
pip install predix
```

Then inspect and run the following script which will provision the service for
you.  It is the same effect as running `cf create-service predix-dbaas`.

```
python create_dbaas.py
```

**(3) Setup the database.**

You must setup the PostgreSQL database with a table described in the file
`schema.sql`.  You can setup the table using a tool like pgStudio or phppgadmin.
You can also use `psql` as described in this tutorial and repository here:

- https://github.com/j12y/predix-gotty-util
- https://medium.com/@j12y/go-host-for-a-shell-in-cloud-foundry-34760e0bec1e

**(4) Push the app.**

You'll want to change the application name to something unique just for you

```
cf push --random-route
```

# Results

With a successful push you should be able to go to a URL such as:

https://predixpy-flask-dbaas-demo.run.aws-usw02-pr.ice.predix.io/

And interact with the PredixPy API to get/set key-values.

---
[signup]: https://www.predix.io/registration
[cf]: https://github.com/cloudfoundry/cli
