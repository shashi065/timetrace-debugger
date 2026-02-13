import sys
import argparse
from timetrace.adapters.python_adapter import PythonAdapter
from timetrace.cli.debugger import DebuggerCLI
from timetrace.core.timeline import Timeline


def main():
    parser = argparse.ArgumentParser(
        prog="timetrace",
        description="Time-travel debugging framework"
    )

    parser.add_argument("script", nargs="?", help="Python script to debug")
    parser.add_argument("--save", help="Save session to file")
    parser.add_argument("--replay", help="Replay a saved session")

    args = parser.parse_args()

    # -----------------------------
    # REPLAY MODE
    # -----------------------------
    if args.replay:
        timeline = Timeline.load(args.replay)
        debugger = DebuggerCLI(timeline)
        debugger.start()
        return

    # -----------------------------
    # NORMAL RECORD MODE
    # -----------------------------
    if not args.script:
        parser.print_help()
        return

    adapter = PythonAdapter()
    timeline = adapter.run(args.script)

    # -----------------------------
    # SAVE SESSION
    # -----------------------------
    if args.save:
        timeline.save(args.save)
        print(f"Session saved to {args.save}")

    debugger = DebuggerCLI(timeline)
    debugger.start()


if __name__ == "__main__":
    main()
