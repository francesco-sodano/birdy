#!/bin/bash

az deployment group create --name Birdy --resource-group "rg-birdy-demo" --template-uri https://raw.githubusercontent.com/francesco-sodano/birdy/main/backend/arm-template/azuredeploy.json --parameters https://raw.githubusercontent.com/francesco-sodano/birdy/main/backend/arm-template/azuredeploy.parameters.json