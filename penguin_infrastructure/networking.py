from aws_cdk import aws_ec2
from . import config


def create_vpc(self):
    self.vpc = aws_ec2.Vpc(
        self, config.VPC_NAME, cidr=config.VPC_CIDR, vpc_name=config.VPC_NAME
    )


def create_security_group(self):
    self.security_group = aws_ec2.SecurityGroup(
        self,
        config.SECURITY_GROUP_NAME,
        vpc=self.vpc,
        allow_all_outbound=True,
        security_group_name=config.SECURITY_GROUP_NAME,
    )
    self.security_group.add_ingress_rule(
        peer=aws_ec2.Peer.ipv4("0.0.0.0/0"),
        description="inbound SSH",
        connection=aws_ec2.Port.tcp(22),
    )
