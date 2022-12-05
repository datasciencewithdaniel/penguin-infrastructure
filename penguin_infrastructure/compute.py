from aws_cdk import aws_ec2
from . import config


def create_user_data(self):
    self.user_data = aws_ec2.UserData.for_linux()
    self.user_data.add_commands("apt-get update -y")
    self.user_data.add_commands("apt-get upgrade -y")
    self.user_data.add_commands("apt install make -y")
    self.user_data.add_commands("apt install python3-pip -y")
    self.user_data.add_commands(
        "apt install -y ca-certificates curl gnupg lsb-release -y"
    )
    self.user_data.add_commands(
        "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg"
    )
    self.user_data.add_commands(
        'echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null'
    )
    self.user_data.add_commands("apt-get update -y")
    self.user_data.add_commands("apt install docker-ce docker-ce-cli containerd.io -y")
    self.user_data.add_commands(
        'curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose'
    )
    self.user_data.add_commands("chmod +x /usr/local/bin/docker-compose")
    self.user_data.add_commands(
        "git clone -b main --single-branch https://github.com/datasciencewithdaniel/penguin.git /home/penguin"
    )
    self.user_data.add_commands(
        f'cd /home/penguin && make {self.COMMAND} DISCORD_TOKEN={self.DISCORD_TOKEN} GUILD_NAME="{self.GUILD_NAME}" AWS_ACCOUNT_DSWD={self.AWS_ACCOUNT_DSWD}'
    )


def create_instance(self):
    instance_type = aws_ec2.InstanceType(config.INSTANCE_TYPE)
    ami_image = aws_ec2.MachineImage().generic_linux(
        {self.AWS_DEFAULT_REGION: config.INSTANCE_AMI}
    )

    self.instance = aws_ec2.Instance(
        self,
        "ec2-instance",
        instance_name=f"{config.INSTANCE_NAME}{self.BOT}",
        instance_type=instance_type,
        machine_image=ami_image,
        vpc=self.vpc,
        security_group=self.security_group,
        role=self.bot_role,
        # user_data=aws_ec2.UserData.custom(self.user_data.render()),
    )
