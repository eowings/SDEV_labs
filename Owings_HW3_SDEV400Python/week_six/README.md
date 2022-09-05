# SDEV400 Serverless Framework

Use the [Serverless Framework](https://github.com/serverless/serverless) to deploy a REST API 
built off [Lambda and API Gateway](https://www.serverless.com/framework/docs/providers/aws/guide/intro/)

## Description
This template will document the process of using the 
[Serverless Framework](https://github.com/serverless/serverless) to deploy a REST API 
built off [Lambda and API Gateway](https://www.serverless.com/framework/docs/providers/aws/guide/intro/).
The instructions are based off using a Cloud9IDE EC2 instance within AWS. They assume you have launched
and Amazon Linux 2 based instance (the default OS - any size machine will work).

This is an OPTIONAL approach - there are other ways to accomplish the assignments.

## Prerequisites
The Serverless framework for this demonstration will use a few items in the background that must be
installed on the instance before using Serverless.

From a Terminal prompt within your Cloud9 EC2 instance run the following shell commands:
```bash
sudo yum install docker -y

sudo yum install nodejs -y

sudo curl -o- -L https://slss.io/install | bash

```

### IMPORTANT: You will now need to close the terminal window and open a new one for the changes/install to complete.

In the next step NPM will WARN about not having a packages.json file... ignore the warning, it isn't relevant.
It will look like this
```shell
npm WARN enoent ENOENT: no such file or directory, open '/home/ec2-user/package.json'
npm WARN ec2-user No description
npm WARN ec2-user No repository field.
npm WARN ec2-user No README data
npm WARN ec2-user No license field.
```

In your NEW terminal window, navigate to the project directory (i.e. the folder you just checked out 
/ unzipped this into), run the following command:
```bash
cd helloworld_serverless_template/

sudo npm install --save-dev serverless-wsgi serverless-python-requirements

sls deploy

```

## License
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [https://www.gnu.org/licenses/gpl-3.0](https://www.gnu.org/licenses/gpl-3.0)
