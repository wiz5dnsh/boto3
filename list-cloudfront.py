import boto3

cf = boto3.client("cloudfront")

p = cf.get_paginator("list_distributions")

for page in p.paginate():
    dist_list = page.get("DistributionList", {}).get("Items", [])
    for d in dist_list:
        print(d["Id"], d["DomainName"])
