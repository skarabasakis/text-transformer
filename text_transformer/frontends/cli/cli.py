import sys
import argparse
from text_transformer import transformers

def setup_parser():
    parser = argparse.ArgumentParser(description='Transform text')
    parser.add_argument('transformer', choices=transformers.__all__, help='The transformer to use')
    return parser

def run(args=None):
    parser = setup_parser()
    args = parser.parse_args(args)
    print(transformers.transform(sys.stdin.read(), args.transformer))
