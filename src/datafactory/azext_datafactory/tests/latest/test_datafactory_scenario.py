# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from .. import try_manual, raise_if
from azure.cli.testsdk import ResourceGroupPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


@try_manual
def setup(test, rg):
    pass


# EXAMPLE: Factories_CreateOrUpdate
@try_manual
def step_factories_createorupdate(test, rg):
    test.cmd('az datafactory factory create '
             '--location "East US" '
             '--name "{myFactoryName}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('name', "{myFactoryName}"),
                 test.check('provisioningState', 'Succeeded')
             ])


# EXAMPLE: Factories_Update
@try_manual
def step_factories_update(test, rg):
    test.cmd('az datafactory factory update '
             '--name "{myFactoryName}" '
             '--tags exampleTag="exampleValue" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('name', "{myFactoryName}"),
                 test.check('provisioningState', 'Succeeded'),
                 test.check('tags.exampleTag', 'exampleValue')
             ])


# EXAMPLE: LinkedServices_Create
@try_manual
def step_linkedservices_create(test, rg):
    test.cmd('az datafactory linked-service create '
             '--factory-name "{myFactoryName}" '
             '--properties "{{\\"type\\":\\"AzureStorage\\",\\"typeProperties\\":{{\\"connectionString\\":{{\\"type\\":'
             '\\"SecureString\\",\\"value\\":\\"DefaultEndpointsProtocol=https;AccountName=examplestorageaccount;Accoun'
             'tKey=<storage key>\\"}}}}}}" '
             '--name "{myLinkedService}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('name', "{myLinkedService}"),
                 test.check('properties.type', 'AzureStorage')
             ])


# EXAMPLE: LinkedServices_Update
@try_manual
def step_linkedservices_update(test, rg):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: Datasets_Create
@try_manual
def step_datasets_create(test, rg):
    test.cmd('az datafactory dataset create '
             '--properties "{{\\"type\\":\\"AzureBlob\\",\\"linkedServiceName\\":{{\\"type\\":\\"LinkedServiceReference'
             '\\",\\"referenceName\\":\\"myLinkedService\\"}},\\"parameters\\":{{\\"MyFileName\\":{{\\"type\\":\\"Strin'
             'g\\"}},\\"MyFolderPath\\":{{\\"type\\":\\"String\\"}}}},\\"typeProperties\\":{{\\"format\\":{{\\"type\\":'
             '\\"TextFormat\\"}},\\"fileName\\":{{\\"type\\":\\"Expression\\",\\"value\\":\\"@dataset().MyFileName\\"}}'
             ',\\"folderPath\\":{{\\"type\\":\\"Expression\\",\\"value\\":\\"@dataset().MyFolderPath\\"}}}}}}" '
             '--name "{myDataset}" '
             '--factory-name "{myFactoryName}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('name', "{myDataset}")
             ])


# EXAMPLE: Datasets_Update
@try_manual
def step_datasets_update(test, rg):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: Pipelines_Create
@try_manual
def step_pipelines_create(test, rg):
    test.cmd('az datafactory pipeline create '
             '--factory-name "{myFactoryName}" '
             '--pipeline "{{\\"activities\\":[{{\\"name\\":\\"ExampleForeachActivity\\",\\"type\\":\\"ForEach\\",\\"typ'
             'eProperties\\":{{\\"activities\\":[{{\\"name\\":\\"ExampleCopyActivity\\",\\"type\\":\\"Copy\\",\\"inputs'
             '\\":[{{\\"type\\":\\"DatasetReference\\",\\"parameters\\":{{\\"MyFileName\\":\\"examplecontainer.csv\\",'
             '\\"MyFolderPath\\":\\"examplecontainer\\"}},\\"referenceName\\":\\"myDataset\\"}}],\\"outputs\\":[{{\\"ty'
             'pe\\":\\"DatasetReference\\",\\"parameters\\":{{\\"MyFileName\\":{{\\"type\\":\\"Expression\\",\\"value\\'
             '":\\"@item()\\"}},\\"MyFolderPath\\":\\"examplecontainer\\"}},\\"referenceName\\":\\"myDataset\\"}}],\\"t'
             'ypeProperties\\":{{\\"dataIntegrationUnits\\":32,\\"sink\\":{{\\"type\\":\\"BlobSink\\"}},\\"source\\":{{'
             '\\"type\\":\\"BlobSource\\"}}}}}}],\\"isSequential\\":true,\\"items\\":{{\\"type\\":\\"Expression\\",\\"v'
             'alue\\":\\"@pipeline().parameters.OutputBlobNameList\\"}}}}}}],\\"parameters\\":{{\\"JobId\\":{{\\"type\\'
             '":\\"String\\"}},\\"OutputBlobNameList\\":{{\\"type\\":\\"Array\\"}}}},\\"variables\\":{{\\"TestVariableA'
             'rray\\":{{\\"type\\":\\"Array\\"}}}},\\"runDimensions\\":{{\\"JobId\\":{{\\"type\\":\\"Expression\\",\\"v'
             'alue\\":\\"@pipeline().parameters.JobId\\"}}}}}}" '
             '--name "{myPipeline}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('name', "{myPipeline}")
             ])


# EXAMPLE: Pipelines_Update
@try_manual
def step_pipelines_update(test, rg):
    test.cmd('az datafactory pipeline update '
             '--factory-name "{myFactoryName}" '
             '--description "Example description" '
             '--name "{myPipeline}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: Triggers_Create
@try_manual
def step_triggers_create(test, rg):
    test.cmd('az datafactory trigger create '
             '--factory-name "{myFactoryName}" '
             '--resource-group "{rg}" '
             '--properties "{{\\"type\\":\\"ScheduleTrigger\\",\\"pipelines\\":[{{\\"parameters\\":{{\\"OutputBlobNameL'
             'ist\\":[\\"exampleoutput.csv\\"]}},\\"pipelineReference\\":{{\\"type\\":\\"PipelineReference\\",\\"refere'
             'nceName\\":\\"{myPipeline}\\"}}}}],\\"typeProperties\\":{{\\"recurrence\\":{{\\"endTime\\":\\"{myEndTime}'
             '\\",\\"frequency\\":\\"Minute\\",\\"interval\\":4,\\"startTime\\":\\"{myStartTime}\\",\\"timeZone\\":'
             '\\"UTC\\"}}}}}}" '
             '--name "{myTrigger}"',
             checks=[
                 test.check('name', "{myTrigger}")
             ])


# EXAMPLE: Triggers_Update
@try_manual
def step_triggers_update(test, rg):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: IntegrationRuntimes_Create
@try_manual
def step_integrationruntimes_create(test, rg):
    test.cmd('az datafactory integration-runtime managed create '
             '--factory-name "{myFactoryName}" '
             '--description "A selfhosted integration runtime" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: IntegrationRuntimes_Update
@try_manual
def step_integrationruntimes_update(test, rg):
    test.cmd('az datafactory integration-runtime update '
             '--factory-name "{myFactoryName}" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}" '
             '--auto-update "Off" '
             '--update-delay-offset "\\"PT3H\\""',
             checks=[])


# EXAMPLE: IntegrationRuntimes_CreateLinkedIntegrationRuntime
@try_manual
def step_integrationruntimes_createlinkedintegrationruntime(test, rg):
    test.cmd('az datafactory integration-runtime linked-integration-runtime create '
             '--name "bfa92911-9fb6-4fbe-8f23-beae87bc1c83" '
             '--location "West US" '
             '--data-factory-name "e9955d6d-56ea-4be3-841c-52a12c1a9981" '
             '--subscription-id "061774c7-4b5a-4159-a55b-365581830283" '
             '--factory-name "{myFactoryName}" '
             '--integration-runtime-name "{myIntegrationRuntime}" '
             '--resource-group "{rg}" '
             '--subscription-id "12345678-1234-1234-1234-12345678abc"',
             checks=[])


# EXAMPLE: Pipelines_CreateRun
@try_manual
def step_pipelines_createrun(test, rg):
    test.cmd('az datafactory pipeline create-run '
             '--factory-name "{myFactoryName}" '
             '--parameters "{{\\"OutputBlobNameList\\":[\\"exampleoutput.csv\\"]}}" '
             '--name "{myPipeline}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: IntegrationRuntimes_Get
@try_manual
def step_integrationruntimes_get(test, rg):
    test.cmd('az datafactory integration-runtime show '
             '--factory-name "{myFactoryName}" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('name', "{myIntegrationRuntime}")
             ])


# EXAMPLE: RerunTriggers_ListByTrigger
@try_manual
def step_reruntriggers_listbytrigger(test, rg):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: LinkedServices_Get
@try_manual
def step_linkedservices_get(test, rg):
    test.cmd('az datafactory linked-service show '
             '--factory-name "{myFactoryName}" '
             '--name "{myLinkedService}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('name', "{myLinkedService}")
             ])


# EXAMPLE: PipelineRuns_Get
@try_manual
def step_pipelineruns_get(test, rg):
    test.cmd('az datafactory pipeline-run show '
             '--factory-name "{myFactoryName}" '
             '--resource-group "{rg}" '
             '--run-id "{myRunId}"',
             checks=[
                 test.check('runId', "{myRunId}")
             ])


# EXAMPLE: Pipelines_Get
@try_manual
def step_pipelines_get(test, rg):
    test.cmd('az datafactory pipeline show '
             '--factory-name "{myFactoryName}" '
             '--name "{myPipeline}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('name', "{myPipeline}")
             ])


# EXAMPLE: Datasets_Get
@try_manual
def step_datasets_get(test, rg):
    test.cmd('az datafactory dataset show '
             '--name "{myDataset}" '
             '--factory-name "{myFactoryName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: Triggers_Get
@try_manual
def step_triggers_get(test, rg):
    test.cmd('az datafactory trigger show '
             '--factory-name "{myFactoryName}" '
             '--resource-group "{rg}" '
             '--name "{myTrigger}"',
             checks=[])


# EXAMPLE: IntegrationRuntimes_ListByFactory
@try_manual
def step_integrationruntimes_listbyfactory(test, rg):
    test.cmd('az datafactory integration-runtime list '
             '--factory-name "{myFactoryName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: LinkedServices_ListByFactory
@try_manual
def step_linkedservices_listbyfactory(test, rg):
    test.cmd('az datafactory linked-service list '
             '--factory-name "{myFactoryName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: Pipelines_ListByFactory
@try_manual
def step_pipelines_listbyfactory(test, rg):
    test.cmd('az datafactory pipeline list '
             '--factory-name "{myFactoryName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: Triggers_ListByFactory
@try_manual
def step_triggers_listbyfactory(test, rg):
    test.cmd('az datafactory trigger list '
             '--factory-name "{myFactoryName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: Datasets_ListByFactory
@try_manual
def step_datasets_listbyfactory(test, rg):
    test.cmd('az datafactory dataset list '
             '--factory-name "{myFactoryName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: Factories_Get
@try_manual
def step_factories_get(test, rg):
    test.cmd('az datafactory factory show '
             '--name "{myFactoryName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: Factories_ListByResourceGroup
@try_manual
def step_factories_listbyresourcegroup(test, rg):
    test.cmd('az datafactory factory list '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: Factories_List
@try_manual
def step_factories_list(test, rg):
    test.cmd('az datafactory factory list '
             '-g ""',
             checks=[])


# EXAMPLE: Operations_List
@try_manual
def step_operations_list(test, rg):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: RerunTriggers_Cancel
@try_manual
def step_reruntriggers_cancel(test, rg):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: RerunTriggers_Start
@try_manual
def step_reruntriggers_start(test, rg):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: RerunTriggers_Stop
@try_manual
def step_reruntriggers_stop(test, rg):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: IntegrationRuntimes_RegenerateAuthKey
@try_manual
def step_integrationruntimes_regenerateauthkey(test, rg):
    test.cmd('az datafactory integration-runtime regenerate-auth-key '
             '--factory-name "{myFactoryName}" '
             '--name "{myIntegrationRuntime}" '
             '--key-name "authKey2" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: TriggerRuns_Rerun
@try_manual
def step_triggerruns_rerun(test, rg):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: IntegrationRuntimes_GetConnectionInfo
@try_manual
def step_integrationruntimes_getconnectioninfo(test, rg):
    test.cmd('az datafactory integration-runtime get-connection-info '
             '--factory-name "{myFactoryName}" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: IntegrationRuntimes_SyncCredentials
@try_manual
def step_integrationruntimes_synccredentials(test, rg):
    test.cmd('az datafactory integration-runtime sync-credentials '
             '--factory-name "{myFactoryName}" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: IntegrationRuntimes_GetMonitoringData
@try_manual
def step_integrationruntimes_getmonitoringdata(test, rg):
    test.cmd('az datafactory integration-runtime get-monitoring-data '
             '--factory-name "{myFactoryName}" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('name', "{myIntegrationRuntime}")
             ])


# EXAMPLE: IntegrationRuntimes_ListAuthKeys
@try_manual
def step_integrationruntimes_listauthkeys(test, rg):
    test.cmd('az datafactory integration-runtime list-auth-key '
             '--factory-name "{myFactoryName}" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: IntegrationRuntimes_Upgrade
@try_manual
def step_integrationruntimes_upgrade(test, rg):
    test.cmd('az datafactory integration-runtime remove-link '
             '--factory-name "{myFactoryName}" '
             '--name "{myIntegrationRuntime}" '
             '--linked-factory-name "myFactoryName-linked" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: IntegrationRuntimes_GetStatus
@try_manual
def step_integrationruntimes_getstatus(test, rg):
    test.cmd('az datafactory integration-runtime get-status '
             '--factory-name "{myFactoryName}" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('name', "{myIntegrationRuntime}"),
                 test.check('properties.dataFactoryName', "{myFactoryName}")
             ])


# EXAMPLE: IntegrationRuntimes_Start
@try_manual
def step_integrationruntimes_start(test, rg):
    test.cmd('az datafactory integration-runtime start '
             '--factory-name "{myFactoryName}" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: IntegrationRuntimes_Stop
@try_manual
def step_integrationruntimes_stop(test, rg):
    test.cmd('az datafactory integration-runtime stop '
             '--factory-name "{myFactoryName}" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: Triggers_GetEventSubscriptionStatus
@try_manual
def step_triggers_geteventsubscriptionstatus(test, rg):
    test.cmd('az datafactory trigger get-event-subscription-status '
             '--factory-name "{myFactoryName}" '
             '--resource-group "{rg}" '
             '--name "{myTrigger}"',
             checks=[])


# EXAMPLE: ActivityRuns_QueryByPipelineRun
@try_manual
def step_activityruns_querybypipelinerun(test, rg):
    test.cmd('az datafactory activity-run query-by-pipeline-run '
             '--factory-name "{myFactoryName}" '
             '--last-updated-after "{myStartTime}" '
             '--last-updated-before "{myEndTime}" '
             '--resource-group "{rg}" '
             '--run-id "{myRunId}"',
             checks=[
                 test.check('value[0].pipelineRunId', "{myRunId}")
             ])


# EXAMPLE: Triggers_UnsubscribeFromEvents
@try_manual
def step_triggers_unsubscribefromevents(test, rg):
    test.cmd('az datafactory trigger unsubscribe-from-event '
             '--factory-name "{myFactoryName}" '
             '--resource-group "{rg}" '
             '--name "{myTrigger}"',
             checks=[])


# EXAMPLE: Triggers_SubscribeToEvents
@try_manual
def step_triggers_subscribetoevents(test, rg):
    test.cmd('az datafactory trigger subscribe-to-event '
             '--factory-name "{myFactoryName}" '
             '--resource-group "{rg}" '
             '--name "{myTrigger}"',
             checks=[])


# EXAMPLE: Triggers_Start
@try_manual
def step_triggers_start(test, rg):
    test.cmd('az datafactory trigger start '
             '--factory-name "{myFactoryName}" '
             '--resource-group "{rg}" '
             '--name "{myTrigger}"',
             checks=[])


# EXAMPLE: Triggers_Stop
@try_manual
def step_triggers_stop(test, rg):
    test.cmd('az datafactory trigger stop '
             '--factory-name "{myFactoryName}" '
             '--resource-group "{rg}" '
             '--name "{myTrigger}"',
             checks=[])


# EXAMPLE: Factories_GetGitHubAccessToken
@try_manual
def step_factories_getgithubaccesstoken(test, rg):
    test.cmd('az datafactory factory get-git-hub-access-token '
             '--name "{myFactoryName}" '
             '--git-hub-access-code "some" '
             '--git-hub-access-token-base-url "some" '
             '--git-hub-client-id "some" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: Factories_GetDataPlaneAccess
@try_manual
def step_factories_getdataplaneaccess(test, rg):
    test.cmd('az datafactory factory get-data-plane-access '
             '--name "{myFactoryName}" '
             '--access-resource-path "" '
             '--expire-time "{myEndTime}" '
             '--permissions "r" '
             '--profile-name "DefaultProfile" '
             '--start-time "{myStartTime}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('policy.permissions', 'r')
             ])


# EXAMPLE: PipelineRuns_QueryByFactory
@try_manual
def step_pipelineruns_querybyfactory(test, rg):
    test.cmd('az datafactory pipeline-run query-by-factory '
             '--factory-name "{myFactoryName}" '
             '--filters operand="PipelineName" operator="Equals" values="myPipeline" '
             '--last-updated-after "{myStartTime}" '
             '--last-updated-before "{myEndTime}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: PipelineRuns_Cancel
@try_manual
def step_pipelineruns_cancel(test, rg):
    test.cmd('az datafactory pipeline-run cancel '
             '--factory-name "{myFactoryName}" '
             '--resource-group "{rg}" '
             '--run-id "{myRunId}"',
             checks=[])


# EXAMPLE: TriggerRuns_QueryByFactory
@try_manual
def step_triggerruns_querybyfactory(test, rg):
    test.cmd('az datafactory trigger-run query-by-factory '
             '--factory-name "{myFactoryName}" '
             '--filters operand="TriggerName" operator="Equals" values="myTrigger" '
             '--last-updated-after "{myStartTime}" '
             '--last-updated-before "{myEndTime}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: Factories_ConfigureFactoryRepo
@try_manual
def step_factories_configurefactoryrepo(test, rg):
    test.cmd('az datafactory factory configure-factory-repo '
             '--factory-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.DataFacto'
             'ry/factories/{myFactoryName}" '
             '--factory-vsts-configuration account-name="ADF" collaboration-branch="master" last-commit-id="" '
             'project-name="project" repository-name="repo" root-folder="/" tenant-id="" '
             '--location "East US"',
             checks=[])


# EXAMPLE: IntegrationRuntimes_Delete
@try_manual
def step_integrationruntimes_delete(test, rg):
    test.cmd('az datafactory integration-runtime delete '
             '--factory-name "{myFactoryName}" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: Triggers_Delete
@try_manual
def step_triggers_delete(test, rg):
    test.cmd('az datafactory trigger delete '
             '--factory-name "{myFactoryName}" '
             '--resource-group "{rg}" '
             '--name "{myTrigger}"',
             checks=[])


# EXAMPLE: Pipelines_Delete
@try_manual
def step_pipelines_delete(test, rg):
    test.cmd('az datafactory pipeline delete '
             '--factory-name "{myFactoryName}" '
             '--name "{myPipeline}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: Datasets_Delete
@try_manual
def step_datasets_delete(test, rg):
    test.cmd('az datafactory dataset delete '
             '--name "{myDataset}" '
             '--factory-name "{myFactoryName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: LinkedServices_Delete
@try_manual
def step_linkedservices_delete(test, rg):
    test.cmd('az datafactory linked-service delete '
             '--factory-name "{myFactoryName}" '
             '--name "{myLinkedService}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: Factories_Delete
@try_manual
def step_factories_delete(test, rg):
    test.cmd('az datafactory factory delete '
             '--name "{myFactoryName}" '
             '--resource-group "{rg}"',
             checks=[])


@try_manual
def cleanup(test, rg):
    pass


@try_manual
def call_scenario(test, rg):
    setup(test, rg)
    step_factories_createorupdate(test, rg)
    step_factories_update(test, rg)
    step_linkedservices_create(test, rg)
    step_linkedservices_update(test, rg)
    step_datasets_create(test, rg)
    step_datasets_update(test, rg)
    step_pipelines_create(test, rg)
    step_pipelines_update(test, rg)
    step_triggers_create(test, rg)
    step_triggers_update(test, rg)
    step_integrationruntimes_create(test, rg)
    step_integrationruntimes_update(test, rg)
    step_integrationruntimes_createlinkedintegrationruntime(test, rg)
    step_pipelines_createrun(test, rg)
    step_integrationruntimes_get(test, rg)
    step_reruntriggers_listbytrigger(test, rg)
    step_linkedservices_get(test, rg)
    step_pipelineruns_get(test, rg)
    step_pipelines_get(test, rg)
    step_datasets_get(test, rg)
    step_triggers_get(test, rg)
    step_integrationruntimes_listbyfactory(test, rg)
    step_linkedservices_listbyfactory(test, rg)
    step_pipelines_listbyfactory(test, rg)
    step_triggers_listbyfactory(test, rg)
    step_datasets_listbyfactory(test, rg)
    step_factories_get(test, rg)
    step_factories_listbyresourcegroup(test, rg)
    step_factories_list(test, rg)
    step_operations_list(test, rg)
    step_reruntriggers_cancel(test, rg)
    step_reruntriggers_start(test, rg)
    step_reruntriggers_stop(test, rg)
    step_integrationruntimes_regenerateauthkey(test, rg)
    step_triggerruns_rerun(test, rg)
    step_integrationruntimes_getconnectioninfo(test, rg)
    step_integrationruntimes_synccredentials(test, rg)
    step_integrationruntimes_getmonitoringdata(test, rg)
    step_integrationruntimes_listauthkeys(test, rg)
    step_integrationruntimes_upgrade(test, rg)
    step_integrationruntimes_getstatus(test, rg)
    step_integrationruntimes_start(test, rg)
    step_integrationruntimes_stop(test, rg)
    step_triggers_geteventsubscriptionstatus(test, rg)
    step_activityruns_querybypipelinerun(test, rg)
    step_triggers_unsubscribefromevents(test, rg)
    step_triggers_subscribetoevents(test, rg)
    step_triggers_start(test, rg)
    step_triggers_stop(test, rg)
    step_factories_getgithubaccesstoken(test, rg)
    step_factories_getdataplaneaccess(test, rg)
    step_pipelineruns_querybyfactory(test, rg)
    step_pipelineruns_cancel(test, rg)
    step_triggerruns_querybyfactory(test, rg)
    step_factories_configurefactoryrepo(test, rg)
    step_integrationruntimes_delete(test, rg)
    step_triggers_delete(test, rg)
    step_pipelines_delete(test, rg)
    step_datasets_delete(test, rg)
    step_linkedservices_delete(test, rg)
    step_factories_delete(test, rg)
    cleanup(test, rg)


@try_manual
class DataFactoryManagementClientScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestdatafactory_myResourceGroup'[:7], key='rg', parameter_name='rg')
    def test_datafactory(self, rg):

        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myFactoryName': 'myFactoryName',
            'myIntegrationRuntime': 'myIntegrationRuntime',
            'myLinkedService': 'myLinkedService',
            'myDataset': 'myDataset',
            'myPipeline': 'myPipeline',
            'myTrigger': 'myTrigger',
        })

        call_scenario(self, rg)
        raise_if()