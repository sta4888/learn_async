import asyncio
from A_coro import main


def make_empty_py_files():
    for i in range(2, 18):
        with open(f"molchanov/step{i}.py", "w") as f:
            f.write('')


if __name__ == '__main__':
    make_empty_py_files()
    # asyncio.run(main())
