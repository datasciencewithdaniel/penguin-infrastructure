# Synth
synth: variables
	STACK_NAME=$(STACK) \
	cdk synth ${STACK}
.PHONY: synth

## Deploy
deploy:
	STACK_NAME=$(STACK) \
	BOT=$(BOT) \
	cdk deploy ${STACK}${BOT} \
	--require-approval never
.PHONY: deploy

## Destroy
destroy:
	STACK_NAME=$(STACK) \
	BOT=$(BOT) \
	cdk destroy ${STACK}${BOT} \
	--force
.PHONY: destroy

## Deploy
deploy-serverless:
	STACK_NAME=$(STACK) \
	cdk deploy ${STACK} \
	--require-approval never
.PHONY: deploy-serverless
