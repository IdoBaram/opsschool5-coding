import click
import boto3
from tabulate import tabulate


@click.group()
@click.option('--tags', '-t', type=str, help='Query resources by tags')
@click.option('--cloud', '-c', type=click.Choice(['aws', 'gcp', 'azure'],
                                                 case_sensitive=False), help='Cloud provider to '
                                                                             'query  [default: aws]', default='aws')
@click.pass_context
def cloudctl(ctx, *args, **kwargs):
    """ Cloud Manager cli """


@cloudctl.group()
@click.pass_context
def get(ctx):
    """ get action """


@get.command()
@click.pass_context
def instances(ctx):
    boto_client = boto3.client('ec2')
    instance_response = boto_client.describe_instances()
    get_instances_table = []
    for reservation in instance_response['Reservations']:
        for instance in reservation['Instances']:
            for tags in instance['Tags']:
                if tags['Key'] == 'Name':
                    get_instances_table.append([instance['InstanceId'], tags['Value'],
                                                instance['State']['Name'], instance['PublicDnsName']])
    print(tabulate(get_instances_table, headers=['InstanceId', 'Name', 'State', 'name (PublicDnsName)']))


@cloudctl.group()
@click.pass_context
def stop(ctx):
    """ stop action """
    print(ctx)


def start():
    cloudctl(obj={})


if __name__ == "__main__":
    start()
