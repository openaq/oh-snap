import boto3

snapshot_name = 'openaqdb-latest'
client = boto3.client('rds')


def handle(event, context):
    client.modify_db_snapshot_attribute(
        DBSnapshotIdentifier=snapshot_name,
        AttributeName='restore',
        ValuesToAdd=[
            'all',
        ]
    )

    return {'status': 'done'}
