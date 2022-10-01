STACK_NAME=PenguinInfrastructureStack

# Synth
synth: variables
	docker-compose run --rm awscdk sh -c 'cdk synth ${STACK_NAME}'
.PHONY: synth

## Deploy
deploy: variables
	docker-compose run --rm awscdk sh -c '\
		AWS_ACCOUNT=$(AWS_ACCOUNT) \
		AWS_REGION=$(AWS_REGION) \
		cdk deploy ${STACK_NAME} \
		--require-approval never \
		--parameters DISCORD_TOKEN=$(DISCORD_TOKEN) \
		--parameters GUILD_NAME="$(GUILD_NAME)"'
.PHONY: deploy

## Destroy
destroy: variables
	docker-compose run --rm awscdk sh -c '\
		AWS_ACCOUNT=$(AWS_ACCOUNT) \
		AWS_REGION=$(AWS_REGION) \
		cdk destroy ${STACK_NAME} \
		--force'
.PHONY: destroy

## Variables
variables:
	touch .env
	docker-compose run --rm envvars validate
	docker-compose run --rm envvars envfile --overwrite
.PHONY: variables
