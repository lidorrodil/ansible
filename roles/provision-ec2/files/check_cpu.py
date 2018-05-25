#!/usr/bin/python
# https://www.artur-rodrigues.com/tech/2015/08/04/fetching-real-cpu-load-from-within-an-ec2-instance.html


from sys import exit
from argparse import ArgumentParser
from datetime import datetime, timedelta
from operator import itemgetter
from requests import get
from boto3.session import Session


parser = ArgumentParser(description='EC2 load checker')
parser.add_argument(
    '-w', action='store', dest='warn_threshold', type=float, default=0.85)
parser.add_argument(
    '-c', action='store', dest='crit_threshold', type=float, default=0.95)
parser.add_argument(
    '-i', '--instance-id', help='Get last instance id', required=True)
arguments = parser.parse_args()

session = Session(
    aws_access_key_id='example',
    aws_secret_access_key='example',
    region_name='eu-central-1')
cw = session.client('cloudwatch')

instance_id = arguments.instance_id

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
print("{0} load at {1}".format(load, timestamp))

if load < arguments.warn_threshold:
    exit(0)
elif load > arguments.crit_threshold:
    exit(2)
else:
    exit(1)


