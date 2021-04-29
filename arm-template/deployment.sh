#!/bin/bash

az deployment group create --name Birdy --resource-group "rg-demo-birdy" --template-uri https://raw.githubusercontent.com/francesco-sodano/birdy/main/arm-template/azuredeploy.json --parameters https://raw.githubusercontent.com/francesco-sodano/birdy/main/arm-template/azuredeploy.parameters.json --rollback-on-error