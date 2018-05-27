#!/usr/bin/python

from sys import exit
from argparse import ArgumentParser
from datetime import datetime, timedelta
from operator import itemgetter
from requests import get
from boto3.session import Session


def check_cpu_capacity(cw, instance_id):

    now = datetime.utcnow()
    past = now - timedelta(minutes=30)
    future = now  + timedelta(minutes=10)

    results = cw.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=past,
        EndTime=future,
        Period=300,
        Statistics=['Average'])

    datapoints = results['Datapoints']
    last_datapoint = sorted(datapoints, key=itemgetter('Timestamp'))[-1]
    utilization = last_datapoint['Average']
    load = round((utilization/100.0), 2)
    timestamp = str(last_datapoint['Timestamp'])

    return load

def main():

    parser = ArgumentParser(description='EC2 load checker')
    parser.add_argument(
        '-w', action='store', dest='warn_threshold', type=float, default=0.85)
    parser.add_argument(
        '-c', action='store', dest='crit_threshold', type=float, default=0.95)
    parser.add_argument(
        '-i', '--instance-id', help='Get last instance id', required=True)
    arguments = parser.parse_args()

    session = Session(
        aws_access_key_id='EXAMPLE',
        aws_secret_access_key='EXAMPLE',
        region_name='eu-central-1')
    cw = session.client('cloudwatch')

    instance_id = arguments.instance_id

    load = check_cpu_capacity(cw, instance_id)

    if load < arguments.warn_threshold:
        print load
        exit(0)
    elif load > arguments.crit_threshold:
        exit(2)
    else:
        exit(1)

if __name__ == '__main__':
    main()
