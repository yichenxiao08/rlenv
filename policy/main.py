import numpy as np
import mujoco
import mujoco_viewer

model = mujoco.MjModel.from_xml_path("policy/robot.xml")
data = mujoco.MjData(model)

mujoco.mj_resetData(model, data)
mujoco.mj_forward(model, data)

print("torso world pos at start:", data.xpos[1])
print("qpos[2] at start:", data.qpos[2])

viewer = mujoco_viewer.MujocoViewer(model, data)

for _ in range(10000):
    if viewer.is_alive:
        mujoco.mj_step(model, data)
        viewer.render()
        print("velocity:", np.mean(data.qvel[3:9]))
    else:
        break

viewer.close()