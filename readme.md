![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
# Timetrace Debugger

Timetrace Debugger is a time-travel debugging engine for Python.

It records execution state, tracks variable changes, and allows stepping
both backward and forward through program execution.

---

## Why Timetrace?

Traditional debuggers only move forward.

Timetrace allows you to:

- Step backward in time
- Inspect past variable states
- Analyze execution history
- Replay saved debugging sessions

---

## Features

- Reverse execution stepping
- Execution timeline recording
- Call stack tracking
- Exception capture
- Thread tracing
- Async support
- Conditional breakpoints
- Watchpoints
- Multi-file project support
- CLI-based interactive debugger

---

## Installation

```bash
pip install timetrace-debugger
```

---

## Quick Start

Run a Python script with time-travel debugging:

```bash
timetrace myscript.py
```

---

## CLI Commands

Inside the debugger:

| Command | Description |
|---------|-------------|
| n       | Next step |
| b       | Step backward |
| si      | Step into |
| so      | Step over |
| su      | Step out |
| s       | Show stack |
| break   | Set breakpoint |
| watch   | Watch variable |
| history | Show variable history |
| q       | Quit |

---

## Save & Replay Sessions

Save execution session:

```bash
timetrace myscript.py --save session.json
```

Replay saved session:

```bash
timetrace --replay session.json
```

---

## Requirements

- Python 3.8+

---

## License

MIT License  
Copyright (c) 2026 Varkala Shashidhar

---

## Author

Developed by Varkala Shashidhar  
