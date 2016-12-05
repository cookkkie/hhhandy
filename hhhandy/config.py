import re
import os

class Config(object):
    @classmethod
    def from_env(cls):
        config = cls
        config_var_pattern = r'^[A-Z_]*$'
        attrs = filter(lambda v: re.match(config_var_pattern, v), dir(cls))
        for attr in attrs:
            value = os.getenv(attr)
            if value:
                setattr(config, attr, value)

        return config
