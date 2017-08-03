from sdc.crypto.token_helper import encode_jwt, encrypt_jwe


def encrypt(json, secret_store, key_purpose):
    """This encrypts the supplied json and returns a jwe token.

    :param str json: The json to be encrypted.
    :param secret_store: The secret store.
    :param str key_purpose: Context for the key.
    :return: A jwe token.

    """
    jwt_key = secret_store.get_key_for_purpose_and_type(key_purpose, "private")

    payload = encode_jwt(json, jwt_key.kid, secret_store, key_purpose)

    jwe_key = secret_store.get_key_for_purpose_and_type(key_purpose, "public")

    return encrypt_jwe(payload, jwe_key.kid, secret_store, key_purpose)
