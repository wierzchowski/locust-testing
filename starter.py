import boto3


IMAGE_ID = "ami-0b418580298265d5c"  # UBUNTU 18.04 LTS
INSTANCES_COUNT = 2
INSTANCE_TYPE = "t2.micro"
KEYPAIR_NAME = "keypair-fastapi"
SECURITY_GROUPS = ['sg-dcbf70ba']


ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

instances = ec2.create_instances(
     ImageId=IMAGE_ID,
     MinCount=INSTANCES_COUNT,
     MaxCount=INSTANCES_COUNT,
     InstanceType=INSTANCE_TYPE,
     KeyName=KEYPAIR_NAME,
     SecurityGroupIds=SECURITY_GROUPS
)


new_instances_id_list = list(map(lambda x: x.id, instances))
