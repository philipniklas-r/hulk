import abc
import mujoco
import queue
from _typeshed import Incomplete
from typing import Callable

PERCENT_REALTIME: Incomplete
MAX_SYNC_MISALIGN: float
SIM_REFRESH_FRACTION: float
CallbackType: Incomplete
LoaderType: Incomplete
KeyCallbackType = Callable[[int], None]

class Handle:
    def __init__(self, sim: _Simulate, cam: mujoco.MjvCamera, opt: mujoco.MjvOption, pert: mujoco.MjvPerturb, user_scn: mujoco.MjvScene | None) -> None: ...
    @property
    def cam(self): ...
    @property
    def opt(self): ...
    @property
    def perturb(self): ...
    @property
    def user_scn(self): ...
    @property
    def m(self): ...
    @property
    def d(self): ...
    def close(self) -> None: ...
    def is_running(self) -> bool: ...
    def lock(self): ...
    def sync(self) -> None: ...
    def update_hfield(self, hfieldid: int): ...
    def update_mesh(self, meshid: int): ...
    def update_texture(self, texid: int): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...

class _MjPythonBase(metaclass=abc.ABCMeta):
    def launch_on_ui_thread(self, model: mujoco.MjModel, data: mujoco.MjData, handle_return: queue.Queue[Handle] | None, key_callback: KeyCallbackType | None): ...

def launch(model: mujoco.MjModel | None = None, data: mujoco.MjData | None = None, *, loader: LoaderType | None = None, show_left_ui: bool = True, show_right_ui: bool = True) -> None: ...
def launch_from_path(path: str) -> None: ...
def launch_passive(model: mujoco.MjModel, data: mujoco.MjData, *, key_callback: KeyCallbackType | None = None, show_left_ui: bool = True, show_right_ui: bool = True) -> Handle: ...
