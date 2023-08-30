
# pip install azure-identity
# pip install msgraph-sdk

from configparser import SectionProxy
from azure.identity.aio import ClientSecretCredential
from msgraph import GraphServiceClient
from msgraph.generated.users.users_request_builder import UsersRequestBuilder
import requests

class Graph:
    settings: SectionProxy
    client_credential: ClientSecretCredential
    app_client: GraphServiceClient

    def __init__(self, config: SectionProxy):
        self.settings = config
        client_id = self.settings['clientId']
        tenant_id = self.settings['tenantId']
        client_secret = self.settings['clientSecret']

        self.client_credential = ClientSecretCredential(tenant_id, client_id, client_secret)
        self.app_client = GraphServiceClient(self.client_credential) # type: ignore

    async def get_app_only_token(self):
        graph_scope = 'https://graph.microsoft.com/.default'
        access_token = await self.client_credential.get_token(graph_scope)
        return access_token.token

    async def get_users(self):
        query_params = UsersRequestBuilder.UsersRequestBuilderGetQueryParameters(
            # Only request specific properties
            select = ['displayName', 'id', 'mail'],
            # Get at most 25 results
            top = 1,
            # Sort by display name
            orderby= ['displayName']
        )
        request_config = UsersRequestBuilder.UsersRequestBuilderGetRequestConfiguration(
            query_parameters=query_params
        )

        users = await self.app_client.users.get(request_configuration=request_config)
        return users

    # THE PYTHON SDK IS IN PREVIEW. FOR NON-PRODUCTION USE ONLY
    async def make_graph_call(self, params):
        access_token = self.settings['access_token']

        def graph(path, params={}):
            headers = {
                'Authorization': 'Bearer %s' % access_token,
                'Prefer': 'outlook.timezone="Asia/Tokyo", outlook.body-content-type="text"'
            }
            response = requests.get(
                path,
                params=params,
                headers=headers,
            )
            return response

        response = graph("https://graph.microsoft.com/v1.0/users/m@1e0.jp/calendar/calendarView", params)
        return response
