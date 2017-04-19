# AWS-python-and-dynamoDB
How to create the tables in dynamodb using python 

Create the directory ./DynamoDBLocal_lib as a root user and go the  created directory 
1) Downloading the zip file dynamodb_local_latest.tar.gz                     
wget http://dynamodb-local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest.tar.gz

2) Unzip the dynamodb_local_latest.tar.gz                             
gunzip dynamodb_local_latest.tar.gz

3) Untar the  dynamodb_local_latest.tar file                                         
tar -xvf  dynamodb_local_latest.tar 

4) Run the Java command                                            
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -help

5) Goto to AWS IAM  create the group 'dynamo_db access'. Provide Complete_dynamodb_access 

6) Create a user with dynamo_db_access and download access ID and Access Key.

5)  Install Boto3:     
pip install boto3

6) Install aws configure:      
yum install aws configure -y
 
7) Set the following IDs:        
aws configure                           
AWS Access Key ID [****]:                           
AWS Secret Access Key [****]:                            
Default region name [us-west-1]: us-west-2                     
Default output format [None]:  json                 

8) Run the following commands
import boto.dynamodb                               
conn = boto.dynamodb.connect_to_region(                  
        'us-west-2',                                     
        aws_access_key_id='<YOUR_AWS_KEY_ID>',                    
        aws_secret_access_key='<YOUR_AWS_SECRET_KEY>')                           
conn.list_tables()                            
The following command should list all the Tables present in the data base                    
