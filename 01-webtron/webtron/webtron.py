import boto3
#import sys
import click

#session = boto3.Session(profile_name = "DEV6888")
#s3 = session.resource('s3')
s3 = boto3.resource('s3')


@click.group()
def cli():
    "Webtron deploys websites to AWS"
    pass

@cli.command('list-buckets')
def bucket():
    "List all S3 Buckets"
    for bucket in s3.buckets.all():
        print(bucket)


@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List objects in an S3 bucket"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)

if __name__ == '__main__':
    cli()
