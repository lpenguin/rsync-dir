import argparse

from . import rsyncdir


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('host')
    parser.add_argument('--to-dir', '-D')
    parser.add_argument('--user', '-U', required=False, help='User')

    args = parser.parse_args()
    rsyncdir.rsync_dir(host=args.host,
                       host_dir=args.to_dir,
                       user=args.user)

if __name__ == '__main__':
    main()
