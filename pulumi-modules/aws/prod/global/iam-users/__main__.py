import pulumi

from pulumi_aws import iam

config = pulumi.Config()
new_user = config.require("new_user")

user = iam.User(new_user)
