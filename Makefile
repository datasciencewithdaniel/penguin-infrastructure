STACK_NAME=PenguinInfrastructureStack1

# Synth
synth: variables
	cdk synth ${STACK_NAME}
.PHONY: synth

## Deploy
deploy:
	cdk deploy ${STACK_NAME} \
		--require-approval never \
		--parameters DISCORD_TOKEN=$(DISCORD_TOKEN) \
		--parameters GUILD_NAME=$(GUILD_NAME)
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
