# Synth
synth: variables
	STACK_NAME=$(STACK_NAME) \
	cdk synth ${STACK_NAME}
.PHONY: synth

## Deploy
deploy:
	STACK_NAME=$(STACK_NAME) \
	BOT=$(BOT) \
	cdk deploy ${STACK_NAME}${BOT} \
	--require-approval never
.PHONY: deploy

## Destroy
destroy:
	STACK_NAME=$(STACK_NAME) \
	BOT=$(BOT) \
	cdk destroy ${STACK_NAME}${BOT} \
	--force
.PHONY: destroy

## Deploy
deploy-serverless:
	STACK_NAME=$(STACK_NAME) \
	cdk deploy ${STACK_NAME} \
	--require-approval never
.PHONY: deploy-serverless
