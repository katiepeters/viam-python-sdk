import abc
from typing import List, Optional

from viam.proto.api.common import WorldState

from ..component_base import ComponentBase


class Gantry(ComponentBase):
    """
    Gantry represents a physical Gantry and can be used for controlling gantries of N axes.

    This acts as an abstract base class for any drivers representing specific 
    gantry implementations. This cannot be used on its own. If the `__init__()` function is
    overriden, it must call the `super().__init__()` function.
    """

    @abc.abstractmethod
    async def get_position(self) -> List[float]:
        """
        Get the position in millimeters.

        Returns:
            List[float]: The position of the axes.
        """
        ...

    @abc.abstractmethod
    async def move_to_position(
        self,
        positions: List[float],
        world_state: Optional[WorldState] = None
    ):
        """
        Move the gantry to a new position.

        Args:
            positions (List[float]): List of positions for the axes to move to,
                in millimeters.
            world_state (Optional[`WorldState`]): Object describing
                obstacles for the gantry to avoid on its way to `positions`.
        """
        ...

    @abc.abstractmethod
    async def get_lengths(self) -> List[float]:
        """
        Get the lengths of the axes of the gantry in millimeters.

        Returns:
            List[float]: The lengths of the axes.
        """
        ...