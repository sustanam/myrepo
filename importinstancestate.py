import boto3
import json

# Initialize the AWS metadata client
metadata = boto3.client('ec2', region_name='us-west-2')

# Define a function to retrieve instance metadata
def get_instance_metadata():
    try:
        # Retrieve the instance metadata
        response = metadata.describe_instances(InstanceIds=['i-12345678'])  # Replace with your instance ID
        
        # Extract the instance metadata
        instance_id = response['Reservations'][0]['Instances'][0]['InstanceId']
        instance_type = response['Reservations'][0]['Instances'][0]['InstanceType']
        public_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
        private_ip = response['Reservations'][0]['Instances'][0]['PrivateIpAddress']
        availability_zone = response['Reservations'][0]['Instances'][0]['Placement']['AvailabilityZone']
        
        # Create a dictionary to store the instance metadata
        instance_metadata = {
            'InstanceId': instance_id,
            'InstanceType': instance_type,
            'PublicIpAddress': public_ip,
            'PrivateIpAddress': private_ip,
            'AvailabilityZone': availability_zone
        }
        
        # Return the instance metadata in JSON format
        return json.dumps(instance_metadata, indent=4)
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Call the function to retrieve the instance metadata
instance_metadata_json = get_instance_metadata()

# Print the instance metadata in JSON format
if instance_metadata_json:
    print(instance_metadata_json)
