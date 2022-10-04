STACK_NAME=PenguinInfrastructureStack

# Synth
synth: variables
	docker-compose run --rm awscdk sh -c 'cdk synth ${STACK_NAME}'
.PHONY: synth

## Deploy
deploy:
	BOT=$(BOT) \
	cdk deploy ${STACK_NAME} \
	--require-approval never
.PHONY: deploy

## Destroy
destroy:
	docker-compose run --rm awscdk sh -c '\
		BOT=$(BOT) \
		cdk destroy ${STACK_NAME} \
		--force'
.PHONY: destroy
