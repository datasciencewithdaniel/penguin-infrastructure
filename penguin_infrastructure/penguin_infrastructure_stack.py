from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2
)
from constructs import Construct

class PenguinInfrastructureStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.instance_name = 'PenguinBotDev'
        self.instance_type = 't2.micro'
        # self.ami_name = 'amazon/ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-20220609'
        self.vpc_name = 'vpc-2dc0394b'

        instance_type = aws_ec2.InstanceType(self.instance_type)
        # ami_image = aws_ec2.MachineImage().lookup(name=self.ami_name)
        ami_image = aws_ec2.MachineImage().latest_amazon_linux()
        
        vpc = aws_ec2.Vpc.from_lookup(self, 'vpc', vpc_id=self.vpc_name)
        sec_group = aws_ec2.SecurityGroup(self, 'ec2-sec-group', vpc=vpc, allow_all_outbound=True)

        sec_group.add_ingress_rule(
            peer=aws_ec2.Peer.ipv4('0.0.0.0/0'),
            description='inbound SSH',
            connection=aws_ec2.Port.tcp(22)
        )

        instance = aws_ec2.Instance(
            self, 'ec2-instance',
            instance_name=self.instance_name,
            instance_type=instance_type,
            machine_image=ami_image,
            vpc=vpc,
            security_group=sec_group
        )
