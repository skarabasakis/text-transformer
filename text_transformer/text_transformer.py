import sys, os
import argparse
from .frontends import cli, tkui, webui

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tkui', action='store_true', help='Starts tkinter gui')
    parser.add_argument('--webui', action='store_true', help='Starts web gui')
    parser.add_argument('other', nargs=argparse.REMAINDER)

    args = parser.parse_args()

    if args.tkui:
        tkui.run()
    elif args.webui:
        webui.run()
    elif args.other:
        cli.run(args.other)
    else:
        tkui.run()
