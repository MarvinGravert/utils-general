import abc

class Comparable(metaclass=abc.ABCMeta):
    """A mixin that makes instances of the class comparable.

    Requires the subclass to just implement `__le__`.
    """

    def __eq__(self, other):
        return self <= other <= self

    def __ne__(self, other):
        return not self == other

    @abc.abstractmethod
    def __le__(self, other):
        pass  # pragma: no cover

    def __lt__(self, other):
        return self <= other and self != other

    def __ge__(self, other):
        return other.__le__(self)

    def __gt__(self, other):
        return self >= other and self != other

    def is_comparable(self, other):
        """Check whether this object is comparable with another one.

        Args:
            other (object): Object to check comparability with.

        Returns:
            Whether the object is comparable with `other`.
        """
        return self < other or self == other or self > other