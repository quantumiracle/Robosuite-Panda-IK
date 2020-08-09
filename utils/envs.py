import robosuite
import gym


def make_env(env_name, seed, environment_arguments = {}):
    def _thunk():
        env = robosuite.make(env_name, **environment_arguments)
        print(env)
        # env.seed(seed) # TODO error: env has no seed
        return env

    return _thunk

