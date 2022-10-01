STACK_NAME=PenguinInfrastructureStack

# Synth
synth: variables
	cdk synth ${STACK_NAME}
.PHONY: synth

## Deploy
deploy:
	cdk deploy ${STACK_NAME} \
		--require-approval never \
.PHONY: deploy

## Destroy
destroy:
	cdk destroy ${STACK_NAME} \
		--force
.PHONY: destroy

## Variables
# variables:
# 	touch .env
# 	docker-compose run --rm envvars validate
# 	docker-compose run --rm envvars envfile --overwrite
# .PHONY: variables
