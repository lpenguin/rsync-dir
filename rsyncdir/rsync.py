from os import path
import subprocess

from . import utils
from .error import RsyncError


def rsync(to_host, from_dir, to_dir, exclude=None, exclude_from=None, user=None, ssh_key=None, verbose=False):
    """
    :type to_host: str
    :type from_dir: str
    :type to_dir: str
    :type exclude: list[str] or None
    :type exclude_from: list[str] or None
    :type user: str or None
    :type ssh_key: str or None
    """
    exclude = exclude or []
    exclude_from = exclude_from or []

    rsync_opts = [
        '-avz',
        '--progress',
        '--partial',
    ]

    if ssh_key:
        rsync_opts.append('-e')
        rsync_opts.append("ssh -i {}".format(path/abspath(ssh_key)))

    if user:
        user += '@'
    else:
        user = ''

    rsync_opts += utils.flatten([('--exclude', ex) for ex in exclude])
    rsync_opts += utils.flatten([('--exclude-from', ex) for ex in exclude_from])

    to_option = "{user}{to_host}:{to_dir}".format(
        to_host=to_host,
        user=user,
        to_dir=to_dir,
    )

    args = (
        ['rsync'] +
        rsync_opts +
        [from_dir, to_option]
    )

    # cmd = "rsync {rsync_opts} {from_dir} {user}{to_host}:{to_dir}".format(
    #     rsync_opts=' '.join(rsync_opts),
    #     from_dir=from_dir,
    #     to_host=to_host,
    #     user=user,
    #     to_dir=to_dir,
    # )

    print('Rsyncing {from_dir} with {to_host}:{to_dir}'.format(
        from_dir=from_dir,
        to_host=to_host,
        to_dir=to_dir,
    ))

    if verbose:
        print("Executing {}".format(' '.join(args)))

    try:
        return subprocess.check_output(args)
    except subprocess.CalledProcessError as ex:
        raise RsyncError(reason=ex.stderr)




