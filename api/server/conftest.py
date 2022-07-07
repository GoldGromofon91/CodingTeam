def pytest_addoption(parser):
    parser.addoption("--server_type", action="store", default="localhost")


def pytest_generate_tests(metafunc):
    option_value = metafunc.config.option.server_type
    if 'server_type' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("server_type", [option_value])
