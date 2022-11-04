# You need to import the keycloak-client: sudo pip3 install keycloak-client
from keycloak import KeycloakOpenID

# Allow to get an identification token in order to use IAGOS REST services.
# You need to provide you email and you password of you IAGOS/AERIS account.
# You can get this information at this address: https://sso.aeris-data.fr/auth/realms/aeris/account
# It's possible your password hasn't been itinitialized if you've only connected by ORCID or EduGAIN. In that case you'll have to define it.
def getToken():
    keycloak_openid = KeycloakOpenID(server_url="https://sso.aeris-data.fr/auth/",
                    client_id="aeris-public",
                    realm_name="aeris",
                    verify=True)
    token = keycloak_openid.token("USER_EMAIL", "USER_PASSWORD")
    return token