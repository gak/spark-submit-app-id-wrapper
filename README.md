# spark-submit application id wrapper

## Overview

A wrapper around spark-submit, specifically tested with YARN, to intercept and
extract the appliation id from stderr. Once the application id is detected, it
prints it to stderr, so that your calling script can process it.

## Usage

The log output is at the same time redirected to stdout, so you can still see
what is happening if needed.


The arguments to the app is your spark-submit command, e.g.:
```
# ssaiw spark-submit --master yarn-cluster --class etc etc > /dev/null
application_1448925599375_0050
```

Note the redirect to `/dev/null` to not show the spark-submit logs, and only
display the application id.

# Installation

```
pip install spark-submit-app-id-wrapper
```

# Notes

There is no timeout functionality at the moment.
