import sys
from pulumi import automation as auto

if __name__ == '__main__':
    user = sys.argv[1]
    iam_module = auto.create_or_select_stack(work_dir="pulumi-modules/aws/prod/global/iam-users", stack_name="poc", project_name="awsusers")
    iam_module.set_config(key="new_user", value=auto.ConfigValue(value=user, secret=False))
    iam_module.refresh(on_output=print)
    iam_module.up(on_output=print)
