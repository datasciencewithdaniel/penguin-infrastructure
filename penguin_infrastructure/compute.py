from aws_cdk import aws_ec2
from . import config


def create_user_data(self):
    self.user_data = aws_ec2.UserData.for_linux()
    self.user_data.add_commands("apt-get update -y")
    self.user_data.add_commands("apt-get upgrade -y")
    self.user_data.add_commands("apt install make -y")
    self.user_data.add_commands("apt install python3-pip -y")
    self.user_data.add_commands(f"export AWS_DEFAULT_REGION={self.AWS_DEFAULT_REGION}")
    self.user_data.add_commands(
        "git clone -b develop --single-branch https://github.com/datasciencewithdaniel/penguin.git"
    )
    self.user_data.add_commands(
        f"cd penguin && sudo python3 -m pip install -r requirements.txt && sudo python3 -m bot.penguin --bot 1 --discord {self.DISCORD_TOKEN} --guild '{self.GUILD_NAME}'"
    )


def create_instance(self):
    instance_type = aws_ec2.InstanceType(config.INSTANCE_TYPE)
    ami_image = aws_ec2.MachineImage().generic_linux(
        {"ap-southeast-2": "ami-09a5c873bc79530d9"}
    )  # .latest_amazon_linux()
    # with open("./penguin_infrastructure/user-data.sh") as file:
    #     user_data = file.read()

    self.instance = aws_ec2.Instance(
        self,
        "ec2-instance",
        instance_name=config.INSTANCE_NAME,
        instance_type=instance_type,
        machine_image=ami_image,
        vpc=self.vpc,
        security_group=self.security_group,
        role=self.bot_role,
        user_data=aws_ec2.UserData.custom(self.user_data.render()),
    )
