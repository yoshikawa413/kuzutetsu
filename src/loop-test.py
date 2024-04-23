import dataclasses
import itertools
from typing import Callable

BATCH_SIZE_MAX = 100


def processing_in_batches_of_max_size(targets: list[str], func: Callable):
    return list(
        itertools.chain(
            *[
                func(targets[i : i + BATCH_SIZE_MAX])
                for i in range(0, len(targets), BATCH_SIZE_MAX)
            ]
        )
    )


@dataclasses.dataclass(init=False)
class Hoge(object):
    def __init__(self, **kwargs):
        names = set([f.name for f in dataclasses.fields(self)])
        [setattr(self, k, v) for k, v in kwargs.items() if k in names]


@dataclasses.dataclass(init=False)
class Hoge2(Hoge):
    aaa: str = None


@dataclasses.dataclass
class Hoge3(object):
    aaa: str = None
    bbb: str = None


if __name__ == "__main__":
    large_list = [str(_) for _ in range(1500)]

    result = processing_in_batches_of_max_size(large_list, lambda _: _[0:2])

    print(f"{result=}")

    hoge = Hoge(aaa="a", bbb="b", ccc="c")
    print(f"{dataclasses.asdict(hoge)=}")

    hoge = Hoge(aaa="a")
    print(f"{dataclasses.asdict(hoge)=}")

    hoge = Hoge(**{"bbb": "b"})
    print(f"{dataclasses.asdict(hoge)=}")

    hoge = Hoge2(**{"bbb": "b"})
    print(f"{dataclasses.asdict(hoge)=}")

    hoge = Hoge2(aaa="a")
    print(f"{dataclasses.asdict(hoge)=}")

    hoge = Hoge2(**{"aaa": "a", "ccc": "c"})
    print(f"{dataclasses.asdict(hoge)=}")
