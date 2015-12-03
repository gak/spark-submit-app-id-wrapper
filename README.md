# spark-submit application id wrapper

A wrapper around spark-submit, specifically tested with YARN, to intercept and
extract the appliation id from stderr. Once the application id is detected, it
prints it to stderr, so that your calling script can process it.

The arguments to the app is your spark-submit command, e.g.:

```
# ssaiw spark-submit --master yarn-cluster --class etc etc
application_1448925599375_0050
```

There is no timeout functionality at the moment.
