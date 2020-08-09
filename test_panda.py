import numpy as np
import robosuite as suite

# create environment instance
env = suite.make("PandaLift", has_renderer=True)

# reset the environment
env.reset()

for i in range(1000):
    action = np.random.randn(env.dof)  # sample random action
    obs, reward, done, info = env.step(action)  # take action in the environment
    env.render()  # render on display
