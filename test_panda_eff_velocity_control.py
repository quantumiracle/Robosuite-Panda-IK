import numpy as np
from utils.envs import make_env
from ik_module import EEFXVelocityControl
from modified_envs.panda_lift_ik import PandaLiftIK
from mujoco_py import MujocoException


# create environment instance
env_params = {
            'use_camera_obs': False,
            'use_object_obs': True,
            'reward_shaping': True,
            'use_indicator_object': False,
            'has_renderer': True,
            'has_offscreen_renderer': False,
            'render_collision_mesh': False,
            'render_visual_mesh': True,
            'control_freq': 10.,
            'horizon': 60,
            'ignore_done': True,  # TODO supposed to be False
            'camera_name': "frontview",
            'camera_height': 256,
            'camera_width': 256,
}
env = make_env("PandaLiftIK", 1, env_params)()  # name, seed, parameters
# print(env.init_right_hand_orn)

wrapper_args = {
    'dof': 3,  # if 2: x-y; if 3: x-y-z
    'max_action': 0.1
}
env = EEFXVelocityControl(env, **wrapper_args)  # make environment from forward kinematics to inverse kinematics

# reset the environment
env.reset()

for i in range(1000):
    # action = np.random.randn(wrapper_args['dof'])  # sample random action
    action = 0.005*np.array([0,0,1])
    # action = np.zeros(3)
    print(action)
    try:
        obs, reward, done, info = env.step(action)  # take action in the environment
    except MujocoException:  # capture the unsolved IK cases
        print('MujocoException')
    if env_params['has_renderer']:
        env.render()  # render on display
