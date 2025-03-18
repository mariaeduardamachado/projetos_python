# filepath: task-tracker-cli/cli/main.py

import sys
from commands.add_task import add_task
from commands.list_tasks import list_tasks
from commands.update_task import update_task
from commands.delete_task import delete_task

def main():
  if len(sys.argv) < 2:
    print("Usage: task-tracker-cli <command> [options]")
    sys.exit(1)

  command = sys.argv[1]

  if command == "add":
    add_task(sys.argv[2:])
  elif command == "list":
    list_tasks()
  elif command == "update":
    update_task(sys.argv[2:])
  elif command == "delete":
    delete_task(sys.argv[2:])
  else:
    print(f"Unknown command: {command}")
    sys.exit(1)

if __name__ == "__main__":
  main()