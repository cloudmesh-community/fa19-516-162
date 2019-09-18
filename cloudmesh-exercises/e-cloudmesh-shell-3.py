# fa19-516-162: Cloudmesh Shell
# E.Cloudmesh.Shell.3
# Write a new command and experiment with docopt syntax and argument interpretation of the dict with if conditions.
# Initial template copied from katukota.py

from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.katukota.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE

class KatukotaCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_katukota(self, args, arguments):
        """
        ::

          Usage:
                katukota --file=FILE
                katukota list

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        arguments.FILE = arguments['--file'] or None

        VERBOSE(arguments)

        m = Manager()

        if arguments.FILE:
            print("option a")
            m.list(path_expand(arguments.FILE))

        elif arguments.list:
            print("option b")
            m.list("just calling list without parameter")

        Console.error("This is just a sample")
        return ""
