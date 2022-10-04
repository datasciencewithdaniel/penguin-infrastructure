STACK_NAME=PenguinInfrastructureStack

# Synth
synth: variables
	cdk synth ${STACK_NAME}
.PHONY: synth

## Deploy
deploy:
	BOT=$(BOT) \
	cdk deploy ${STACK_NAME}${BOT} \
	--require-approval never
.PHONY: deploy

## Destroy
destroy:
	BOT=$(BOT) \
	cdk destroy ${STACK_NAME}${BOT} \
	--force
.PHONY: destroy
