import os
from os import path

from .rsync import rsync
from .error import RsyncError


def rsync_dir(host, host_dir, user):
    """

    :type host: str
    :type host_dir: str or None
    :type user: str or None
    """
    current_dir = os.getcwd()
    gitignore_file = path.join(current_dir, '.gitignore')
    rsyncignore_file = path.join(current_dir, '.rsyncignore')
    git_dit = path.join('.git')

    exclude_from = []
    if path.exists(gitignore_file):
        exclude_from.append(gitignore_file)
    if path.exists(rsyncignore_file):
        exclude_from.append(rsyncignore_file)

    exclude = []
    if path.exists(git_dit):
        exclude.append(git_dit)

    if not host_dir:
        host_dir = path.basename(current_dir)

    if not current_dir.endswith('/'):
        current_dir += '/'

    try:
        out = rsync(to_host=host,
                    from_dir=current_dir,
                    exclude_from=exclude_from,
                    exclude=exclude,
                    user=user,
                    to_dir=host_dir,
                    verbose=True)
        print(out.decode())
    except RsyncError as err:
        print('Error occurred: {}'.format(err.reason))
