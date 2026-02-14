# Timetrace Debugger

A Time-Travel Debugging Engine for Python.

Timetrace enables reverse execution, execution timeline recording, and structured debugging of Python programs.

---

##  Overview

Traditional debuggers allow forward stepping only.

Timetrace allows you to:
- Step backward in execution
- Inspect historical variable states
- Analyze execution timelines
- Replay saved debugging sessions

This makes debugging faster, more analytical, and more educational.

---

##  Features

- Reverse execution stepping
- Execution timeline recording
- Call stack tracking
- Exception capture
- Thread & async tracing
- Conditional breakpoints
- Watchpoints
- Multi-file project support
- CLI-based interactive interface

---

##  Installation

```bash
pip install timetrace-debugger
```

Verify installation:

```bash
timetrace --help
```

---

##  Basic Usage

Run Timetrace on a Python file:

```bash
timetrace your_script.py
```

Example:

```bash
timetrace app.py
```

---

##  Debugger Commands

| Command | Action |
|----------|--------|
| n | Step forward |
| b | Step backward |
| si | Step into |
| so | Step over |
| su | Step out |
| p | Print current state |
| s | Show call stack |
| g <step> | Go to specific step |
| break <line> | Set breakpoint |
| break if <condition> | Conditional breakpoint |
| watch <var> | Watch variable |
| history <var> | View variable history |
| q | Quit debugger |

---

##  Using Timetrace Efficiently

To get the best results, follow these recommended debugging techniques:

---

### 1️ Step Forward to Understand Flow

Use:

```
n
```

to move line-by-line through execution.

Inspect variables using:

```
p
```

This helps understand program logic before locating issues.

---

### 2️ Step Backward to Identify Root Cause

If incorrect output appears:

1. Use:
   ```
   b
   ```
2. Move backward through execution.
3. Observe where the variable changed unexpectedly.

This avoids restarting the program repeatedly.

---

### 3️ Use Conditional Breakpoints

Instead of stepping through long loops:

```
break if x > 100
```

Execution pauses only when the condition becomes true.

Best for:
- Loop debugging
- Edge-case detection
- Logical condition failures

---

### 4️ Watch Critical Variables

Track variable changes:

```
watch x
```

View full history:

```
history x
```

Useful for:
- Recursive functions
- State mutation debugging
- Complex calculations

---

### 5️ Analyze Recursion Using Stack View

In recursive programs:

```
s
```

This displays the call stack.

Helps in:
- Understanding recursion depth
- Tracking nested calls
- Identifying infinite recursion

---

### 6️ Save & Replay Sessions

Save execution session:

```bash
timetrace script.py --save session.json
```

Replay later:

```bash
timetrace --replay session.json
```

Useful for:
- Sharing debugging sessions
- Reviewing past executions
- Demonstrations

---

### 7️ Multi-File Projects

Run Timetrace from your project root:

```bash
timetrace main.py
```

Ensures:
- Proper module tracing
- Accurate import resolution
- Complete execution capture

---

##  Academic Use

Timetrace is especially useful for:

- Understanding recursion
- Learning stack behavior
- Debugging lab assignments
- Visualizing variable changes
- Teaching program flow
- Improving analytical debugging skills

---

##  Limitations

- Very large programs may consume more memory
- Heavy multiprocessing not fully supported
- GUI applications are CLI-debug only
- Designed primarily for debugging logic, not high-load production systems

---

##  License

MIT License  
Copyright (c) 2026 Varkala Shashidhar
