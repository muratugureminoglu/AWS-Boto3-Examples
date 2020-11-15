import boto3
ec2 = boto3.resource('ec2')
session = boto3.session.Session()

print ("Region: ",session.region_name)

def instance(tag):
    filter = ec2.instances.filter(Filters=[{'Name': 'tag:Name', 'Values': [tag]},
                        {'Name': 'instance-state-name', 'Values': ['running']}])
    count=0
    for i in filter:
        count += 1
        print ("Instances Id : {}".format(i.id))
    if count != 0:
        print ("Total number of running instances with label {1}: {0}".format(count,tag))
    else:
        print("No instances are running.")

instance('OpenVPN')