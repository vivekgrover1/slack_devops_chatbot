#!/usr/bin/python

from errbot import BotPlugin, botcmd, arg_botcmd
import boto3


class AWS(BotPlugin):
    """
    AWS plugin
    """
    
    def _connect(self,region):
        access_key=""
        secret_key=""
        self.ec2 = boto3.resource("ec2", region_name=region,aws_access_key_id=access_key,aws_secret_access_key=secret_key)
        return self.ec2

    def _get_instance_by_id(self, id):
        return self.ec2.Instance(id)


    @arg_botcmd('region_name', type=str)
    def aws_list_instances(self, msg, region_name=None):
        """
        List all AWS instances.
        """
        driver=self._connect(region_name)
        instances = driver.instances.all()
        yield  """**IP**	| **State**	| **ID**	| **Instance Type**"""
        for i in instances:
            yield "{ip} | {state} | {id} | {type}".format(
                ip=i.public_ip_address,
                state=i.state['Name'],
                id=i.id,
                type=i.instance_type)

    @arg_botcmd('instance_id', type=str)
    @arg_botcmd('region_name', type=str)
    def aws_stop(self, msg, instance_id=None, region_name=None):
        """
        Stop instance by id.
        """
        id = instance_id
        driver=self._connect(region_name)
        instance = self._get_instance_by_id(id)
        response = ""
        i = driver.instances.filter(InstanceIds=[id]).stop()
        reponse = "Instance {0} stopped".format(instance)
        return reponse

    
    @arg_botcmd('instance_id', type=str)
    @arg_botcmd('region_name', type=str)
    def aws_start(self, msg, instance_id=None, region_name=None):
        """
        Start instance by id.
        """
        id = instance_id
        driver=self._connect(region_name)
        instance = self._get_instance_by_id(id)
        response = ""
        i = driver.instances.filter(InstanceIds=[id]).start()
        response = "Instance {0} started".format(instance)
        return response
 
    @arg_botcmd('status', type=str)
    @arg_botcmd('region_name', type=str)
    def list_instances_by_status(self, msg,status=None,region_name=None):
        """
        Lists instances by status.

        Args:
           status (str): aws status such as 'running', 'stopped'
        """
        driver=self._connect(region_name)
        instances = driver.instances.filter(Filters=[
            {"Name": "instance-state-name",
             "Values": [status]}
            ])
        yield  """**IP**        | **State**     | **ID**        | **Instance Type**"""
        for i in instances:
            yield "{ip} | {state} | {id} | {type}".format(
                ip=i.public_ip_address,
                state=i.state['Name'],
                id=i.id,
                type=i.instance_type)


    @arg_botcmd('region_name', type=str)
    def aws_provision_instance(self,msg,region_name=None):
        driver=self._connect(region_name)
        new = driver.create_instances(
            ImageId='ami-5b673c34',
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro'
        )
        return self.send_card(
                    title='Aws instances is created',
                    in_reply_to=msg,
                    body="Action aws instance provisioning completed\n\nID:{0}\nInstance will be ready for ssh after 50-60 seconds.".format(new),
                    color="green"
                )

    def aws_terminate(self, id):
        i = self.ec2.instances.filter(InstanceIds=[id]).terminate()

