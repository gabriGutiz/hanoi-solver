from argparse import ArgumentParser

from src import Runner

parser = ArgumentParser()
parser.add_argument('--mode', type=int)

if __name__ == '__main__':
    args = parser.parse_args()
    mode = args.mode

    if not mode:
        mode = 3
    print(f'Starting game with mode {mode}...')
    Runner(int(mode))
