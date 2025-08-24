import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")
response = ec2.describe_instances()
instances = [i for r in response["Reservations"] for i in r["Instances"]]

for instance in instances:
    
    name = next((t["Value"] for t in instance.get("Tags", []) if t["Key"] == "Name"), "N/A")
    
    print(instance["InstanceId"], name, instance["InstanceType"], instance["State"]["Name"])
