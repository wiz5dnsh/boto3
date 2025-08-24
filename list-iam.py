import boto3

iam = boto3.client("iam")

for u in iam.list_users()["Users"]:
    print("User:", u["UserName"])

for r in iam.list_roles()["Roles"]:
    print("Role:", r["RoleName"])
