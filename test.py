import argparse
import pprint
from test import run_tests

parser = argparse.ArgumentParser(description="Run application tests")

parser.add_argument("-t", "--test", type=str, default=None,
                    help="Name of a test to run")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
parser.add_argument("-s", "--silent", action="store_true",
                    help="silent execution")
args = parser.parse_args()

pp = pprint.PrettyPrinter(indent=2,compact=False)
if args.verbose:
    pp.pprint(args)

results = run_tests(args.verbose or not args.silent , args.test)

if not args.verbose:
    del results["results"]

pp.pprint(results)
