import os 


def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

POSTGRES_URL = get_env_variable('EXAMPLE_POSTGRES_URL') 

POSTGRES_USER = get_env_variable('EXAMPLE_POSTGRES_USER')

POSTGRES_PW = get_env_variable('EXAMPLE_POSTGRES_PW')

POSTGRES_DB = get_env_variable('EXAMPLE_POSTGRES_DB')

if __name__ == "__main__":

    print(POSTGRES_URL)