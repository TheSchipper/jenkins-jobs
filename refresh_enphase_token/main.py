import os
import logging

from hcp_vault_secrets_client.hcp import HcpClient
from enphase_home_api_client.enphase import EnphaseAPIClient

def main():
    """
    1. Fetch Enphase refresh & access tokens from Vault
    2. Refresh Enphase refresh & access token
    3. Publish new Enphase refresh & access tokens to Vault
    """
    # 1. Fetch Enphase refresh & access tokens from Vault
    hcp_client = HcpClient()

    current_refresh_token = hcp_client.get_app_secret("enphase_refresh_token")
    current_access_token = hcp_client.get_app_secret("enphase_access_token")

    os.environ["ENPHASE_REFRESH_TOKEN"] = current_refresh_token
    os.environ["ENPHASE_ACCESS_TOKEN"] = current_access_token

    # 2. Refresh Enphase refresh & access token

    enphase_client = EnphaseAPIClient()

    new_access_token, new_refresh_token = enphase_client.generate_new_enphase_tokens()

    # 3. Publish new Enphase refresh & access tokens to Vault
    hcp_client.create_app_secret("enphase_refresh_token", new_refresh_token)
    hcp_client.create_app_secret("enphase_access_token", new_access_token)

if __name__ == "__main__":
    main()
