
import argparse
from text_transformer.frontends import cli, tkui, webui

parser = argparse.ArgumentParser()
parser.add_argument('--tkui', action='store_true', help='Starts tkinter gui')
parser.add_argument('--webui', action='store_true', help='Starts web gui')
parser.add_argument('other', nargs=argparse.REMAINDER)

args = parser.parse_args()

if args.tkui:
    tkui.run()
elif args.webui:
    webui.run()
else:
    cli.run(args.other)
