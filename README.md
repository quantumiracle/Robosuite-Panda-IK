# Surreal Robotics Suite Panda Robot with IK control

This project is built on top of [Surreal Robotics Suite (Robosuite)](<https://github.com/StanfordVL/robosuite>) and [our previous work](<https://github.com/eugval/sim2real_dynamics_simulation>). You need to install necessary packages in both above projects. This project enables Panda robot with inverse kinematics control.



There are also some modifications in scripts within Robosuite, where the updated scripts are in folder `./extra_modules_replacing_robosuite`:

* `__init__.py`: replace `robosuite/robosuite/models/tasks/__init__.py`;
* `placement_sampler.py`: replace `robosuite/robosuite/models/tasks/placement_sampler.py`;
* `base.py`: replace `robosuite/robosuite/environments/base.py`;
* `panda.py`: replace `robosuite/robosuite/environments/panda.py`;
* `panda_gripper.py`: replace `robosuite/robosuite/models/grippers/panda_gripper.py`.

## Quick Start

```python
python test_panda_eff_velocity_control.py
```





### Author

Zihan Ding