Oh Snap!
===

This is an internal tool to create manual [Amazon RDS](https://aws.amazon.com/rds/) snapshots and make them publicly available. With this snapshot, anyone can have access to the full database that powers [OpenAQ](https://openaq.org). This is the preferred mechanism for dealing with the full dataset as it's many millions of records (~25 million as of 10/9/2016).

You can see how to restore from a snapshot [here](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RestoreFromSnapshot.html), the ARN for the daily-updated database is `arn:aws:rds:us-east-1:470049585876:snapshot:openaqdb-latest`.

In addition to these two functions (one to create snapshot and one to update availability to public), there are a few other steps if you want to reproduce this system in your own project.

1. Create an [AWS SNS] topic.
1. In your RDS instance, create an Event that sends out notifications on snapshot creation to the SNS topic you just created.
1. Attach this repository's Lambda `update` function to the SNS topic.

Now when a new snapshot is created, your updated function will be run.

Note that as set up, our `update` function will get called many more times than necessary, but it won't hurt anything as it just tries to set the `openaqdb-latest` snapshot to be publicly available.

![](http://i.giphy.com/3o6ozC2VM9R0XSMNKo.gif)