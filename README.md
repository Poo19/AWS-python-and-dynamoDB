# AWS-python-and-dynamoDB
How to create the tables in dynamodb using python 

Create the directory ./DynamoDBLocal_lib as a root user and go the  created directory 
1) Downloading the zip file dynamodb_local_latest.tar.gz
wget http://dynamodb-local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest.tar.gz

2) Unzip the dynamodb_local_latest.tar.gz
gunzip dynamodb_local_latest.tar.gz

3) Untar the  dynamodb_local_latest.tar file
tar -xvf gunzip dynamodb_local_latest.tar 

4) Run the Java command 
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -help

5) Goto to AWS IAM  create the group 'dynamo_db access'. Provide Complete_dynamodb_access 

6) Create a user with dynamo_db_access and download access ID and Access Key.

5)  Install Boto3
pip install boto3
