import boto3
from time import sleep

snapshot_name = 'openaqdb-latest'
db_name = 'openaqdb'
client = boto3.client('rds')


def handle(event, context):
    # Delete db snapshot if it exists
    try:
        client.delete_db_snapshot(
          DBSnapshotIdentifier=snapshot_name
        )
    except:
        pass

    # # Wait a few seconds to make sure previous db is deleted
    sleep(10)

    # Create new private snapshot
    client.create_db_snapshot(
      DBSnapshotIdentifier=snapshot_name,
      DBInstanceIdentifier=db_name
    )

    return {'status': 'done'}
