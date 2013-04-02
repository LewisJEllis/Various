"""
WARNING: THIS IS $11.60/hr TO RUN!

~/.boto should look like this:
[Credentials]
aws_access_key_id = YOURCREDSGOHEREWITHNOQUOTES
aws_secret_access_key = YOURCREDSGOHERE

and you need your AWS keys downloaded to ~/.ec2

Then just invoke this script.
You can check here for what's been reported by everyone running this:
http://lewisjellis.webscript.io/skeinlog?show=true
"""

import boto

ec2_instance_type = 'c1.xlarge' # our AMI uses 8 cores
num_instances = 20
ami_id = 'ami-6865f158' # this is our custom AMI
key = 'xkcd-crackers' #this is your SSH keypair
sec = ['xkcd-crackers'] # this is your security group


conn = boto.connect_ec2()
regions = boto.ec2.regions()
usw2 = regions[2].connect()

def launch_instance():
  return usw2.run_instances(ami_id, 
                            instance_type=ec2_instance_type,
                            security_groups=sec,
                            key_name=key)

def launch_instances(n):
  return [launch_instance() for i in range(0,n)]

instances = launch_instances(num_instances)

for i in instances:
  print(i)

print('Launched ' + str(num_instances) + ' instances!')