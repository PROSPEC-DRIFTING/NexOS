import time
import random
import os
import datetime
import json
import math
from pyfiglet import Figlet
from spellchecker import SpellChecker
import sys
import urllib.request
import urllib.error
import hashlib
import tempfile
import shutil
import subprocess

# ============================================================
# NEXOS™
# ============================================================
# Main NexOS terminal program
# ============================================================


VERSION = "1.1.9"

UPDATE_VERSION_URL = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPOSITORY/main/version.json"
UPDATE_FILE_URL = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPOSITORY/main/NexOS.py"

BACKUP_FILE = "NexOS_backup.py"


ACCOUNT_FILE = "account.json"
NOTES_FILE = "notes.json"
STOPWATCH_FILE = "stopwatch.json"
CALCULATOR_FILE = "calculator.json"


# ============================================================
# STARTUP
# ============================================================

def startup():
    os.system("clear")

    print("")
    print("================================================")
    print("                                                ")
    print("                 N E X O S ™                    ")
    print("                                                ")
    print("================================================")
    time.sleep(0.7)

    print("")
    print("              NEXSTEP™ PRESENTS")
    time.sleep(0.5)

    print("")
    print("                 NexOS™")
    print(f"                 Version {VERSION}")
    time.sleep(0.7)

    print("")
    print("Loading system...")
    time.sleep(0.4)

    print("[✓] Loading core")
    time.sleep(0.25)

    print("[✓] Loading applications")
    time.sleep(0.25)

    print("[✓] Loading account system")
    time.sleep(0.25)

    print("[✓] Loading notes")
    time.sleep(0.25)

    print("[✓] Loading calculator")
    time.sleep(0.25)

    print("[✓] Loading stopwatch")
    time.sleep(0.25)

    print("[✓] Loading system commands")
    time.sleep(0.25)

    print("")
    print("System ready.")
    time.sleep(0.5)

    print("")
    print("Tip:")
    time.sleep(0.35)

    print("Type 'help' if you're stuck")
    time.sleep(0.5)

    print("")


# ============================================================
# TERMINAL
# ============================================================

def terminal():

    current_user = None
    command_history = []

    while True:

        try:
            command = input("NexOS™> ").lower().strip()

        except KeyboardInterrupt:
            print("")
            print("Use 'shutdown' to safely close NexOS.")
            continue

        except EOFError:
            print("")
            print("NexOS™ shutting down...")
            break


        # ====================================================
        # COMMAND HISTORY
        # ====================================================

        if current_user is not None:
            if command != "":
                command_history.append(command)


        # ====================================================
        # HELP
        # ====================================================

        if command == "help":

            print("")
            print("================================")
            print("          NEXOS™ HELP")
            print("================================")

            print("")
            print("BASIC COMMANDS")
            print("----------------")
            print("help           - Display this help menu")
            print("about          - About NexOS")
            print("version        - Show NexOS version")
            print("clear          - Clear the terminal")
            print("shutdown       - Shut down NexOS")
            print("update log     - View update history")

            print("")
            print("APPLICATIONS")
            print("----------------")
            print("calculator     - Calculator")
            print("clock          - Digital clock")
            print("randomizer     - Random number generator")
            print("spell check    - Check spelling")
            print("stopwatch      - Stopwatch")
            print("notes          - Notes application")
            print("settings       - NexOS™ system settings")

            print("")
            print("ACCOUNT")
            print("----------------")
            print("sign in        - Create an account")
            print("log in         - Log into an account")
            print("history        - View command history")

            print("")
            print("OTHER")
            print("----------------")
            print("basic commands - Basic commands")
            print("applications   - Application list")
            print("system info    - System information")
            print("account features - Account commands")

            print("")
            print("Type a command exactly as shown.")
            print("================================")


        # ====================================================
        # BASIC COMMANDS
        # ====================================================

        elif command == "basic commands":

            print("")
            print("======================")
            print("    BASIC COMMANDS")
            print("======================")

            print("")
            print("about")
            print("Shows information about NexOS.")

            print("")
            print("version")
            print("Shows the current NexOS version.")

            print("")
            print("clear")
            print("Clears the terminal screen.")

            print("")
            print("shutdown")
            print("Shuts down NexOS.")

            print("")
            print("update log")
            print("Shows the NexOS update history.")


        # ====================================================
        # APPLICATIONS
        # ====================================================

        elif command == "applications":

            print("")
            print("======================")
            print("     APPLICATIONS")
            print("======================")

            print("")
            print("calculator")
            print("Advanced mathematical calculator.")

            print("")
            print("clock")
            print("ASCII digital clock.")

            print("")
            print("randomizer")
            print("Random number generator.")

            print("")
            print("spell check")
            print("Spell-checking application.")

            print("")
            print("stopwatch")
            print("Precision stopwatch with laps.")

            print("")
            print("notes")
            print("Personal notes application.")


        # ====================================================
        # SYSTEM INFO
        # ====================================================

        elif command == "system info":

            print("")
            print("======================")
            print("      SYSTEM INFO")
            print("======================")

            print("")
            print("Operating System : NexOS™")
            print(f"Version          : {VERSION}")
            print("Developer        : NEXSTEP™")
            print("Interface        : Terminal")
            print("Language         : Python")
            print("Status           : Operational")


        # ====================================================
        # ACCOUNT FEATURES
        # ====================================================

        elif command == "account features":

            print("")
            print("======================")
            print("   ACCOUNT FEATURES")
            print("======================")

            print("")
            print("sign in")
            print("Create a new NexOS account.")

            print("")
            print("log in")
            print("Log into an existing account.")

            print("")
            print("history")
            print("View your terminal command history.")


        # ====================================================
        # ABOUT
        # ====================================================

        elif command == "about":

            print("")
            print("------------------------------")

            time.sleep(0.2)

            print(
                "NexOS is a project developed by NEXSTEP "
                "and its team."
            )

            time.sleep(1)

            print("")
            print(
                "The project is being developed to create "
                "a simple and useful operating-system-style "
                "environment using Python."
            )

            time.sleep(1)

            print("")
            print("NexOS written by: Jayant")
            time.sleep(0.4)

            print("NexOS code by: Joell")
            time.sleep(0.4)

            print("NexOS refined by: Jaipal")
            time.sleep(0.4)

            print("NexOS founder: Jayant")
            time.sleep(0.4)

            print("NexOS co-founder: Aarav")
            time.sleep(0.4)

            print("------------------------------")


        # ====================================================
        # VERSION
        # ====================================================

        elif command == "version":

            print("")
            print("------------------------------")
            print(f"NexOS™ {VERSION}")
            print("")
            print("Type 'update log' to view version history.")
            print("")
            print("NEXSTEP™ - Making Tech Better")
            print("------------------------------")


        # ====================================================
        # CLEAR
        # ====================================================

        elif command == "clear":

            os.system("clear")


        # ====================================================
        # SHUTDOWN
        # ====================================================

        elif command == "shutdown":

            print("")
            print("------------------------------")

            time.sleep(0.5)
            print("Saving NexOS session...")

            time.sleep(0.5)
            print("Closing applications...")

            time.sleep(0.5)
            print("Shutting down NexOS™...")

            time.sleep(0.7)

            print("------------------------------")

            break


        # ====================================================
        # CALCULATOR
        # ====================================================

        elif command == "calculator":

            calculator()


        # ====================================================
        # CLOCK
        # ====================================================

        elif command == "clock":

            clock()


        # ====================================================
        # CREATE ACCOUNT
        # ====================================================

        elif command == "sign in":

            create_account()


        # ====================================================
        # LOGIN
        # ====================================================

        elif command == "log in":

            logged_in_user = login()

            if logged_in_user is not None:
                current_user = logged_in_user


        # ====================================================
        # UPDATE LOG
        # ====================================================

        elif command == "update log":

            update_log()


        # ====================================================
        # RANDOMIZER
        # ====================================================

        elif command == "randomizer":

            randomizer()


        # ====================================================
        # SPELLCHECK
        # ====================================================

        elif command == "spell check":

            spellcheck()


        # ====================================================
        # HISTORY
        # ====================================================

        elif command == "history":

            if current_user is None:

                print("You must be logged in to access history.")

            else:

                history(
                    current_user,
                    command_history
                )


        # ====================================================
        # NOTES
        # ====================================================

        elif command == "notes":

            notes(current_user)


        # ====================================================
        # STOPWATCH
        # ====================================================

        elif command == "stopwatch":

            stopwatch()


        # ====================================================
        # UNKNOWN COMMAND
        # ====================================================

        elif command != "":

            print("")
            print(f"Unknown command: {command}")
            print("Type 'help' to see available commands.")

        # ====================================================
        # SETTINGS
        # ====================================================

        elif command == "settings":
            settings(current_user=None)

# ============================================================
# NEXOS UPDATE SYSTEM
# ============================================================

def update_nexos():

    print("")
    print("=" * 55)
    print("                  N E X O S ™")
    print("                    UPDATER")
    print("=" * 55)

    print("")
    print(f"Current NexOS version: {VERSION}")
    print("")
    print("Checking for updates...")

    try:

        with urllib.request.urlopen(
            UPDATE_VERSION_URL,
            timeout=10
        ) as response:

            data = response.read().decode("utf-8")

        update_info = json.loads(data)

    except urllib.error.URLError as error:

        print("")
        print("Could not connect to the NexOS update server.")
        print(f"Error: {error}")

        return

    except json.JSONDecodeError:

        print("")
        print("The update server returned invalid data.")

        return

    except Exception as error:

        print("")
        print("An unexpected update error occurred.")
        print(f"Error: {error}")

        return


    latest_version = str(
        update_info.get(
            "version",
            VERSION
        )
    )


    download_url = update_info.get(
        "download_url",
        UPDATE_FILE_URL
    )


    print("")
    print(f"Installed version : {VERSION}")
    print(f"Latest version    : {latest_version}")


    if latest_version == VERSION:

        print("")
        print("NexOS is already up to date.")
        print("")
        return


    print("")
    print("================================")
    print("        UPDATE AVAILABLE")
    print("================================")

    print("")
    print(
        f"NexOS {latest_version} is available."
    )


    changelog = update_info.get(
        "changelog",
        []
    )


    if changelog:

        print("")
        print("What's new:")

        for change in changelog:

            print(
                f"  • {change}"
            )


    print("")

    confirm = input(
        "Install this update? (y/n): "
    ).lower().strip()


    if confirm != "y":

        print("")
        print("Update cancelled.")
        return


    print("")
    print("Downloading update...")


    try:

        with urllib.request.urlopen(
            download_url,
            timeout=30
        ) as response:

            new_code = response.read()

    except urllib.error.URLError as error:

        print("")
        print("Download failed.")
        print(f"Error: {error}")

        return

    except Exception as error:

        print("")
        print("Could not download the update.")
        print(f"Error: {error}")

        return


    if not new_code:

        print("")
        print("Downloaded update is empty.")
        print("Update cancelled.")

        return


    print(
        f"Downloaded {len(new_code)} bytes."
    )


    # ========================================================
    # VERIFY DOWNLOADED FILE
    # ========================================================

    print("")
    print("Verifying update...")


    try:

        decoded_code = new_code.decode(
            "utf-8"
        )

    except UnicodeDecodeError:

        print("")
        print("Update is not valid UTF-8 Python source.")
        print("Update cancelled.")

        return


    if "def terminal(" not in decoded_code:

        print("")
        print(
            "Update verification failed."
        )

        print(
            "The downloaded file does not appear to be NexOS."
        )

        print("Update cancelled.")

        return


    if "VERSION =" not in decoded_code:

        print("")
        print(
            "Update verification failed."
        )

        print(
            "The downloaded file does not contain a VERSION."
        )

        print("Update cancelled.")

        return


    print(
        "[✓] Update appears to be valid NexOS code."
    )


    # ========================================================
    # CREATE BACKUP
    # ========================================================

    current_file = os.path.abspath(
        sys.argv[0]
    )

    backup_file = os.path.join(
        os.path.dirname(current_file),
        BACKUP_FILE
    )


    print("")
    print("Creating backup...")


    try:

        shutil.copy2(
            current_file,
            backup_file
        )

        print(
            f"[✓] Backup created: {BACKUP_FILE}"
        )

    except Exception as error:

        print("")
        print("Could not create backup.")
        print(f"Error: {error}")

        print("")
        print("Update cancelled.")

        return


    # ========================================================
    # WRITE TEMPORARY UPDATE
    # ========================================================

    print("")
    print("Preparing update...")


    try:

        temporary_file = tempfile.NamedTemporaryFile(
            mode="wb",
            delete=False,
            suffix=".py",
            dir=os.path.dirname(current_file)
        )

        temporary_path = temporary_file.name

        temporary_file.write(
            new_code
        )

        temporary_file.close()

    except Exception as error:

        print("")
        print("Could not prepare update.")
        print(f"Error: {error}")

        return


    # ========================================================
    # TEST PYTHON SYNTAX
    # ========================================================

    print("")
    print("Checking Python syntax...")


    try:

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "py_compile",
                temporary_path
            ],
            capture_output=True,
            text=True
        )


        if result.returncode != 0:

            print("")
            print(
                "The update contains a Python syntax error."
            )

            print("")
            print(
                result.stderr
            )

            print("")
            print("Your current NexOS was NOT changed.")

            os.remove(
                temporary_path
            )

            return


    except Exception as error:

        print("")
        print("Could not test the update.")
        print(f"Error: {error}")

        try:

            os.remove(
                temporary_path
            )

        except OSError:

            pass

        return


    print(
        "[✓] Python syntax check passed."
    )


    # ========================================================
    # INSTALL UPDATE
    # ========================================================

    print("")
    print("Installing update...")


    try:

        shutil.move(
            temporary_path,
            current_file
        )

    except Exception as error:

        print("")
        print("Could not install update.")
        print(f"Error: {error}")

        try:

            os.remove(
                temporary_path
            )

        except OSError:

            pass

        return


    print(
        "[✓] NexOS updated successfully."
    )


    # ========================================================
    # RESTART
    # ========================================================

    print("")
    print("=" * 55)

    restart = input(
        "Restart NexOS now? (y/n): "
    ).lower().strip()


    if restart == "y":

        print("")
        print("Restarting NexOS...")

        time.sleep(1)

        try:

            os.execv(
                sys.executable,
                [
                    sys.executable,
                    current_file
                ]
            )

        except Exception as error:

            print("")
            print(
                "NexOS could not restart automatically."
            )

            print(
                f"Error: {error}"
            )

    else:

        print("")
        print(
            "Update installed."
        )

        print(
            "Restart NexOS manually to use the new version."
        )

# ============================================================
# HISTORY
# ============================================================

def history(current_user, command_history):

    if current_user is None:

        print("You must be logged in to access history.")
        return


    print("")
    print("----------------------")
    print(f"Command History - {current_user}")
    print("----------------------")


    if not command_history:

        print("No commands recorded.")
        return


    for number, command in enumerate(
        command_history,
        1
    ):

        print(
            f"{number} - {command}"
        )


# ============================================================
# STOPWATCH
# ============================================================

def stopwatch():

    stopwatch_file = STOPWATCH_FILE

    start_time = None
    elapsed = 0.0
    running = False

    laps = []

    lap_start_time = 0.0


    print("")
    print("=" * 50)
    print("              N E X O S ™")
    print("               STOPWATCH")
    print("=" * 50)

    print("")
    print("Press ENTER to start/stop")
    print("")
    print("Commands:")
    print("")
    print("lap          - Record a lap")
    print("laps         - Show all laps")
    print("last         - Show the last lap")
    print("time         - Show elapsed time")
    print("status       - Show stopwatch status")
    print("reset        - Reset stopwatch")
    print("clear laps   - Delete lap records")
    print("save         - Save stopwatch session")
    print("history      - Show saved sessions")
    print("help         - Show stopwatch help")
    print("exit         - Leave stopwatch")

    print("")
    print("=" * 50)


    while True:

        command = input(
            "Stopwatch> "
        ).lower().strip()


        # ====================================================
        # START / STOP
        # ====================================================

        if command == "":

            if not running:

                start_time = time.time() - elapsed

                lap_start_time = time.time()

                running = True

                print("Stopwatch started.")

            else:

                elapsed = time.time() - start_time

                running = False

                print(
                    "Stopwatch stopped at "
                    f"{format_stopwatch_time(elapsed)}"
                )


        # ====================================================
        # LAP
        # ====================================================

        elif command == "lap":

            if not running:

                print(
                    "Start the stopwatch first."
                )

                continue


            current_time = (
                time.time() - start_time
            )

            lap_time = (
                current_time
                - (
                    sum(
                        lap["time"]
                        for lap in laps
                    )
                )
            )


            lap_number = len(laps) + 1


            laps.append(
                {
                    "lap": lap_number,
                    "time": lap_time,
                    "total": current_time
                }
            )


            print(
                f"Lap {lap_number}: "
                f"{format_stopwatch_time(lap_time)}"
            )


        # ====================================================
        # SHOW LAPS
        # ====================================================

        elif command == "laps":

            if not laps:

                print(
                    "No laps recorded."
                )

                continue


            print("")
            print("-" * 65)
            print("                         LAPS")
            print("-" * 65)


            for lap in laps:

                print(
                    f"Lap {lap['lap']:<3} | "
                    f"Lap time: "
                    f"{format_stopwatch_time(lap['time'])} | "
                    f"Total: "
                    f"{format_stopwatch_time(lap['total'])}"
                )


            print("-" * 65)


        # ====================================================
        # LAST LAP
        # ====================================================

        elif command == "last":

            if not laps:

                print(
                    "No laps recorded."
                )

                continue


            last_lap = laps[-1]


            print("")
            print("Last lap:")
            print(
                f"Lap {last_lap['lap']} - "
                f"{format_stopwatch_time(last_lap['time'])}"
            )


        # ====================================================
        # CURRENT TIME
        # ====================================================

        elif command == "time":

            if running:

                current_time = (
                    time.time() - start_time
                )

            else:

                current_time = elapsed


            print(
                "Elapsed time:",
                format_stopwatch_time(
                    current_time
                )
            )


        # ====================================================
        # STATUS
        # ====================================================

        elif command == "status":

            if running:

                current_time = (
                    time.time() - start_time
                )

                print("Status: RUNNING")

            else:

                current_time = elapsed

                print("Status: STOPPED")


            print(
                "Elapsed:",
                format_stopwatch_time(
                    current_time
                )
            )


        # ====================================================
        # RESET
        # ====================================================

        elif command == "reset":

            if running:

                print(
                    "Stop the stopwatch before resetting."
                )

                continue


            confirm = input(
                "Reset stopwatch and delete laps? (y/n): "
            ).lower()


            if confirm == "y":

                start_time = None
                elapsed = 0.0
                running = False

                laps.clear()

                lap_start_time = 0.0

                print(
                    "Stopwatch reset."
                )

            else:

                print(
                    "Reset cancelled."
                )


        # ====================================================
        # CLEAR LAPS
        # ====================================================

        elif command == "clear laps":

            if not laps:

                print(
                    "There are no laps to clear."
                )

                continue


            confirm = input(
                "Delete all lap records? (y/n): "
            ).lower()


            if confirm == "y":

                laps.clear()

                print(
                    "Lap records cleared."
                )

            else:

                print(
                    "Cancelled."
                )


        # ====================================================
        # SAVE
        # ====================================================

        elif command == "save":

            if running:

                current_time = (
                    time.time() - start_time
                )

            else:

                current_time = elapsed


            session = {

                "date":
                datetime.datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

                "duration":
                current_time,

                "laps":
                laps.copy()
            }


            try:

                with open(
                    stopwatch_file,
                    "r"
                ) as file:

                    stopwatch_data = json.load(file)


            except (
                FileNotFoundError,
                json.JSONDecodeError
            ):

                stopwatch_data = {
                    "sessions": []
                }


            stopwatch_data.setdefault(
                "sessions",
                []
            )


            stopwatch_data["sessions"].append(
                session
            )


            with open(
                stopwatch_file,
                "w"
            ) as file:

                json.dump(
                    stopwatch_data,
                    file,
                    indent=4
                )


            print(
                "Stopwatch session saved."
            )


        # ====================================================
        # HISTORY
        # ====================================================

        elif command == "history":

            try:

                with open(
                    stopwatch_file,
                    "r"
                ) as file:

                    stopwatch_data = json.load(file)


            except (
                FileNotFoundError,
                json.JSONDecodeError
            ):

                print(
                    "No stopwatch history found."
                )

                continue


            sessions = stopwatch_data.get(
                "sessions",
                []
            )


            if not sessions:

                print(
                    "No saved sessions."
                )

                continue


            print("")
            print("-" * 65)
            print("                  STOPWATCH HISTORY")
            print("-" * 65)


            for number, session in enumerate(
                sessions,
                1
            ):

                print(
                    f"{number}. "
                    f"{session.get('date', 'Unknown date')} | "
                    f"{format_stopwatch_time(session.get('duration', 0))} | "
                    f"{len(session.get('laps', []))} laps"
                )


            print("-" * 65)


        # ====================================================
        # HELP
        # ====================================================

        elif command == "help":

            print("")
            print("=" * 50)
            print("             STOPWATCH HELP")
            print("=" * 50)

            print("")
            print("ENTER")
            print("Start or stop the stopwatch.")

            print("")
            print("lap")
            print("Record the current lap.")

            print("")
            print("laps")
            print("Display all laps.")

            print("")
            print("last")
            print("Display the last lap.")

            print("")
            print("time")
            print("Display elapsed time.")

            print("")
            print("status")
            print("Show stopwatch status.")

            print("")
            print("reset")
            print("Reset stopwatch.")

            print("")
            print("clear laps")
            print("Delete current laps.")

            print("")
            print("save")
            print("Save the current session.")

            print("")
            print("history")
            print("Show saved sessions.")

            print("")
            print("exit")
            print("Return to NexOS.")

            print("")
            print("=" * 50)


        # ====================================================
        # EXIT
        # ====================================================

        elif command == "exit":

            if running:

                confirm = input(
                    "Stopwatch is running. Exit anyway? (y/n): "
                ).lower()


                if confirm != "y":

                    continue


            print(
                "Leaving stopwatch..."
            )

            break


        # ====================================================
        # UNKNOWN COMMAND
        # ====================================================

        else:

            print(
                "Unknown stopwatch command."
            )

            print(
                "Type 'help' for commands."
            )


# ============================================================
# STOPWATCH FORMAT
# ============================================================

def format_stopwatch_time(seconds):

    minutes = int(
        seconds // 60
    )

    seconds_remaining = (
        seconds % 60
    )


    hours = (
        minutes // 60
    )

    minutes = (
        minutes % 60
    )


    return (
        f"{hours:02d}:"
        f"{minutes:02d}:"
        f"{seconds_remaining:06.3f}"
    )


# ============================================================
# NOTES
# ============================================================

def notes(current_user):

    if current_user is None:

        print(
            "You must be logged in to access notes."
        )

        return


    try:

        with open(
            NOTES_FILE,
            "r"
        ) as file:

            notes_data = json.load(file)


    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):

        notes_data = {
            "users": {}
        }


    notes_data.setdefault(
        "users",
        {}
    )


    notes_data["users"].setdefault(
        current_user,
        {
            "notes": {}
        }
    )


    user_notes = (
        notes_data["users"]
        [current_user]
        .setdefault("notes", {})
    )


    print("")
    print("----------------------")
    print(f"Notes - {current_user}")
    print("----------------------")

    print("new       - Create a note")
    print("view      - View all notes")
    print("read      - Read a note")
    print("edit      - Edit a note")
    print("delete    - Delete a note")
    print("search    - Search notes")
    print("pin       - Pin a note")
    print("unpin     - Unpin a note")
    print("pinned    - Show pinned notes")
    print("archive   - Archive a note")
    print("unarchive - Restore an archived note")
    print("info      - Show note information")
    print("exit      - Leave Notes")


    while True:

        command = input(
            "Notes> "
        ).lower().strip()


        # ====================================================
        # NEW NOTE
        # ====================================================

        if command == "new":

            title = input(
                "Title: "
            ).strip()

            content = input(
                "Content: "
            ).strip()


            numeric_ids = []

            for key in user_notes:

                try:
                    numeric_ids.append(
                        int(key)
                    )

                except ValueError:
                    pass


            if numeric_ids:

                note_id = str(
                    max(numeric_ids) + 1
                )

            else:

                note_id = "1"


            now = datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )


            user_notes[note_id] = {

                "title":
                title,

                "content":
                content,

                "created":
                now,

                "modified":
                now,

                "pinned":
                False,

                "archived":
                False
            }


            print(
                f"Note {note_id} created successfully."
            )


        # ====================================================
        # VIEW
        # ====================================================

        elif command == "view":

            if not user_notes:

                print(
                    "You have no notes."
                )

                continue


            print("")
            print("----------------------")
            print("Your Notes")
            print("----------------------")


            found = False


            for note_id, note in user_notes.items():

                if not note.get(
                    "archived",
                    False
                ):

                    pin = (
                        " [PINNED]"
                        if note.get(
                            "pinned",
                            False
                        )
                        else ""
                    )


                    print(
                        f"{note_id} - "
                        f"{note.get('title', 'Untitled')}"
                        f"{pin}"
                    )

                    found = True


            if not found:

                print(
                    "No active notes."
                )


        # ====================================================
        # READ
        # ====================================================

        elif command == "read":

            note_id = input(
                "Note ID: "
            ).strip()


            if note_id in user_notes:

                note = user_notes[note_id]


                print("")
                print("----------------------")
                print(
                    note.get(
                        "title",
                        "Untitled"
                    )
                )
                print("----------------------")

                print(
                    note.get(
                        "content",
                        ""
                    )
                )

                print("----------------------")


            else:

                print(
                    "Note not found."
                )


        # ====================================================
        # EDIT
        # ====================================================

        elif command == "edit":

            note_id = input(
                "Note ID: "
            ).strip()


            if note_id not in user_notes:

                print(
                    "Note not found."
                )

                continue


            note = user_notes[note_id]


            print(
                "Press Enter to keep the current value."
            )


            new_title = input(
                f"Title [{note.get('title', '')}]: "
            )


            new_content = input(
                f"Content [{note.get('content', '')}]: "
            )


            if new_title:

                note["title"] = new_title


            if new_content:

                note["content"] = new_content


            note["modified"] = (
                datetime.datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            )


            print(
                "Note updated successfully."
            )


        # ====================================================
        # DELETE
        # ====================================================

        elif command == "delete":

            note_id = input(
                "Note ID: "
            ).strip()


            if note_id not in user_notes:

                print(
                    "Note not found."
                )

                continue


            title = user_notes[note_id].get(
                "title",
                "Untitled"
            )


            confirm = input(
                f"Delete '{title}'? (y/n): "
            ).lower()


            if confirm == "y":

                del user_notes[note_id]

                print(
                    "Note deleted."
                )

            else:

                print(
                    "Deletion cancelled."
                )


        # ====================================================
        # SEARCH
        # ====================================================

        elif command == "search":

            search_term = input(
                "Search: "
            ).lower().strip()


            found = False


            for note_id, note in user_notes.items():

                title = note.get(
                    "title",
                    ""
                ).lower()

                content = note.get(
                    "content",
                    ""
                ).lower()


                if (
                    search_term in title
                    or search_term in content
                ):

                    print(
                        f"{note_id} - "
                        f"{note.get('title', 'Untitled')}"
                    )

                    found = True


            if not found:

                print(
                    "No matching notes found."
                )


        # ====================================================
        # PIN
        # ====================================================

        elif command == "pin":

            note_id = input(
                "Note ID: "
            ).strip()


            if note_id in user_notes:

                user_notes[note_id]["pinned"] = True

                print(
                    "Note pinned."
                )

            else:

                print(
                    "Note not found."
                )


        # ====================================================
        # UNPIN
        # ====================================================

        elif command == "unpin":

            note_id = input(
                "Note ID: "
            ).strip()


            if note_id in user_notes:

                user_notes[note_id]["pinned"] = False

                print(
                    "Note unpinned."
                )

            else:

                print(
                    "Note not found."
                )


        # ====================================================
        # PINNED
        # ====================================================

        elif command == "pinned":

            print("")
            print("----------------------")
            print("Pinned Notes")
            print("----------------------")


            found = False


            for note_id, note in user_notes.items():

                if note.get(
                    "pinned",
                    False
                ):

                    print(
                        f"{note_id} - "
                        f"{note.get('title', 'Untitled')}"
                    )

                    found = True


            if not found:

                print(
                    "You have no pinned notes."
                )


        # ====================================================
        # ARCHIVE
        # ====================================================

        elif command == "archive":

            note_id = input(
                "Note ID: "
            ).strip()


            if note_id in user_notes:

                user_notes[note_id]["archived"] = True

                print(
                    "Note archived."
                )

            else:

                print(
                    "Note not found."
                )


        # ====================================================
        # UNARCHIVE
        # ====================================================

        elif command == "unarchive":

            note_id = input(
                "Note ID: "
            ).strip()


            if note_id in user_notes:

                user_notes[note_id]["archived"] = False

                print(
                    "Note restored."
                )

            else:

                print(
                    "Note not found."
                )


        # ====================================================
        # INFO
        # ====================================================

        elif command == "info":

            note_id = input(
                "Note ID: "
            ).strip()


            if note_id not in user_notes:

                print(
                    "Note not found."
                )

                continue


            note = user_notes[note_id]


            print("")
            print("----------------------")

            print(
                f"ID:       {note_id}"
            )

            print(
                f"Title:    {note.get('title', 'Untitled')}"
            )

            print(
                f"Created:  {note.get('created', 'Unknown')}"
            )

            print(
                f"Modified: {note.get('modified', 'Unknown')}"
            )

            print(
                f"Pinned:   {note.get('pinned', False)}"
            )

            print(
                f"Archived: {note.get('archived', False)}"
            )

            print("----------------------")


        # ====================================================
        # EXIT
        # ====================================================

        elif command == "exit":

            with open(
                NOTES_FILE,
                "w"
            ) as file:

                json.dump(
                    notes_data,
                    file,
                    indent=4
                )


            print(
                "Leaving Notes..."
            )

            break


        # ====================================================
        # UNKNOWN
        # ====================================================

        else:

            print(
                "Unknown Notes command."
            )

            print(
                "Type one of the Notes commands shown above."
            )


# ============================================================
# SPELLCHECK
# ============================================================

def spellcheck():

    spell = SpellChecker()


    print("")
    print("======================")
    print("     SPELL CHECK")
    print("======================")


    text = input(
        "Enter text: "
    )


    words = text.split()


    misspelled = spell.unknown(
        words
    )


    if not misspelled:

        print(
            "No spelling errors found!"
        )

        return


    print("")
    print("Possible corrections:")


    for word in misspelled:

        correction = spell.correction(
            word
        )


        print(
            f"{word} → {correction}"
        )


# ============================================================
# RANDOMIZER
# ============================================================

def randomizer():

    minimum = 1
    maximum = 100


    print("")
    print("==============================")
    print("          RANDOMIZER")
    print("==============================")

    print(
        "Current range:",
        minimum,
        "-",
        maximum
    )

    print("")
    print("Press ENTER to roll")
    print("Type 'settings' to change range")
    print("Type 'exit' to leave")


    while True:

        command = input(
            "Randomizer> "
        ).lower().strip()


        if command == "exit":

            print(
                "Leaving randomizer..."
            )

            break


        elif command == "":

            roll = random.randint(
                minimum,
                maximum
            )


            print(
                "You rolled:",
                roll
            )


        elif command == "settings":

            try:

                new_minimum = int(
                    input("Minimum: ")
                )

                new_maximum = int(
                    input("Maximum: ")
                )


                if new_minimum > new_maximum:

                    print(
                        "Minimum cannot be greater than maximum."
                    )

                else:

                    minimum = new_minimum
                    maximum = new_maximum


                    print(
                        "Range changed to",
                        minimum,
                        "-",
                        maximum
                    )


            except ValueError:

                print(
                    "Please enter numbers only."
                )


        elif command == "help":

            print("")
            print("settings - Change random range")
            print("ENTER    - Generate random number")
            print("exit     - Leave randomizer")


        else:

            print(
                "Unknown command."
            )


# ============================================================
# CALCULATOR
# ============================================================

def calculator():

    calculator_file = CALCULATOR_FILE

    memory = 0
    last_answer = 0

    calculation_history = []


    # ========================================================
    # LOAD HISTORY
    # ========================================================

    try:

        with open(
            calculator_file,
            "r"
        ) as file:

            calculator_data = json.load(file)


        calculation_history = (
            calculator_data.get(
                "history",
                []
            )
        )


    except FileNotFoundError:

        calculation_history = []


    except json.JSONDecodeError:

        print(
            "Calculator history file is corrupted."
        )

        calculation_history = []


    # ========================================================
    # STARTUP
    # ========================================================

    print("")
    print("=" * 55)
    print("                 N E X O S ™")
    print("                  CALCULATOR")
    print("=" * 55)

    print("")
    print("Type a mathematical expression.")

    print("")
    print("Examples:")
    print("2 + 2")
    print("10 * 5")
    print("2 ** 8")
    print("sqrt(25)")
    print("sin(90)")
    print("log(100)")
    print("factorial(5)")

    print("")
    print("Commands:")
    print("help       - Calculator help")
    print("history    - Calculation history")
    print("clear      - Clear calculation history")
    print("M+         - Add previous answer to memory")
    print("M-         - Subtract previous answer")
    print("MR         - Recall memory")
    print("MC         - Clear memory")
    print("ans        - Previous answer")
    print("exit       - Leave calculator")

    print("")
    print("=" * 55)


    # ========================================================
    # FUNCTIONS
    # ========================================================

    allowed_functions = {

        "sqrt": math.sqrt,

        "sin": math.sin,

        "cos": math.cos,

        "tan": math.tan,

        "asin": math.asin,

        "acos": math.acos,

        "atan": math.atan,

        "log": math.log10,

        "ln": math.log,

        "factorial": math.factorial,

        "abs": abs,

        "floor": math.floor,

        "ceil": math.ceil
    }


    constants = {

        "pi": math.pi,

        "e": math.e
    }


    # ========================================================
    # CALCULATOR LOOP
    # ========================================================

    while True:

        command = input(
            "Calculator> "
        ).strip()


        lower_command = command.lower()


        # ====================================================
        # EXIT
        # ====================================================

        if lower_command == "exit":

            print(
                "Leaving calculator..."
            )

            break


        # ====================================================
        # HELP
        # ====================================================

        elif lower_command == "help":

            print("")
            print("=" * 55)
            print("              CALCULATOR HELP")
            print("=" * 55)

            print("")
            print("ARITHMETIC")
            print("----------------")
            print("+       Addition")
            print("-       Subtraction")
            print("*       Multiplication")
            print("/       Division")
            print("//      Floor division")
            print("%       Modulus")
            print("**      Power")

            print("")
            print("FUNCTIONS")
            print("----------------")
            print("sqrt(x)       Square root")
            print("sin(x)        Sine")
            print("cos(x)        Cosine")
            print("tan(x)        Tangent")
            print("asin(x)       Inverse sine")
            print("acos(x)       Inverse cosine")
            print("atan(x)       Inverse tangent")
            print("log(x)        Base-10 logarithm")
            print("ln(x)         Natural logarithm")
            print("factorial(x)  Factorial")
            print("abs(x)        Absolute value")
            print("floor(x)      Round down")
            print("ceil(x)       Round up")

            print("")
            print("CONSTANTS")
            print("----------------")
            print("pi")
            print("e")

            print("")
            print("MEMORY")
            print("----------------")
            print("M+")
            print("M-")
            print("MR")
            print("MC")

            print("")
            print("OTHER")
            print("----------------")
            print("ans")
            print("history")
            print("clear")
            print("exit")

            print("")
            print("=" * 55)


        # ====================================================
        # MEMORY ADD
        # ====================================================

        elif lower_command == "m+":

            memory += last_answer

            print(
                f"Memory: {memory}"
            )


        # ====================================================
        # MEMORY SUBTRACT
        # ====================================================

        elif lower_command == "m-":

            memory -= last_answer

            print(
                f"Memory: {memory}"
            )


        # ====================================================
        # MEMORY RECALL
        # ====================================================

        elif lower_command == "mr":

            print(
                f"Memory: {memory}"
            )


        # ====================================================
        # MEMORY CLEAR
        # ====================================================

        elif lower_command == "mc":

            memory = 0

            print(
                "Memory cleared."
            )


        # ====================================================
        # ANSWER
        # ====================================================

        elif lower_command == "ans":

            print(
                f"Previous answer: {last_answer}"
            )


        # ====================================================
        # HISTORY
        # ====================================================

        elif lower_command == "history":

            if not calculation_history:

                print(
                    "No calculations recorded."
                )

                continue


            print("")
            print("-" * 70)
            print("                    CALCULATION HISTORY")
            print("-" * 70)


            for number, calculation in enumerate(
                calculation_history,
                1
            ):

                print(
                    f"{number}. "
                    f"{calculation.get('expression', '')} "
                    f"= "
                    f"{calculation.get('result', '')}"
                )


            print("-" * 70)


        # ====================================================
        # CLEAR HISTORY
        # ====================================================

        elif lower_command == "clear":

            if not calculation_history:

                print(
                    "Calculation history is already empty."
                )

                continue


            confirm = input(
                "Clear all calculation history? (y/n): "
            ).lower()


            if confirm == "y":

                calculation_history.clear()


                save_calculator_history(
                    calculation_history
                )


                print(
                    "Calculation history cleared."
                )

            else:

                print(
                    "Cancelled."
                )


        # ====================================================
        # CALCULATION
        # ====================================================

        elif command != "":

            expression = command


            try:

                # --------------------------------------------
                # Previous answer
                # --------------------------------------------

                expression = expression.replace(
                    "ans",
                    str(last_answer)
                )


                # --------------------------------------------
                # Constants
                # --------------------------------------------

                for name, value in constants.items():

                    expression = expression.replace(
                        name,
                        str(value)
                    )


                # --------------------------------------------
                # Functions
                # --------------------------------------------

                for name in allowed_functions:

                    expression = expression.replace(
                        name,
                        f"allowed_functions['{name}']"
                    )


                allowed_names = {
                    "allowed_functions":
                    allowed_functions
                }


                # --------------------------------------------
                # Evaluation
                # --------------------------------------------

                result = eval(
                    expression,
                    {
                        "__builtins__": {}
                    },
                    allowed_names
                )


                # --------------------------------------------
                # Complex number check
                # --------------------------------------------

                if isinstance(
                    result,
                    complex
                ):

                    print(
                        "Complex numbers are not supported."
                    )

                    continue


                # --------------------------------------------
                # Save answer
                # --------------------------------------------

                last_answer = result


                # --------------------------------------------
                # Display
                # --------------------------------------------

                print(
                    f"= {result}"
                )


                # --------------------------------------------
                # History
                # --------------------------------------------

                calculation_history.append(
                    {

                        "expression":
                        command,

                        "result":
                        result,

                        "date":
                        datetime.datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        )
                    }
                )


                save_calculator_history(
                    calculation_history
                )


            except ZeroDivisionError:

                print(
                    "Error: Cannot divide by zero."
                )


            except ValueError:

                print(
                    "Error: Invalid mathematical value."
                )


            except OverflowError:

                print(
                    "Error: Number is too large."
                )


            except TypeError:

                print(
                    "Error: Invalid operation."
                )


            except SyntaxError:

                print(
                    "Error: Invalid mathematical expression."
                )


            except NameError:

                print(
                    "Error: Unknown function or value."
                )


            except Exception:

                print(
                    "Invalid calculation."
                )


    # ========================================================
    # SAVE BEFORE EXIT
    # ========================================================

    save_calculator_history(
        calculation_history
    )


# ============================================================
# SAVE CALCULATOR HISTORY
# ============================================================

def save_calculator_history(history_data):

    try:

        with open(
            CALCULATOR_FILE,
            "w"
        ) as file:

            json.dump(
                {
                    "history":
                    history_data
                },
                file,
                indent=4
            )


    except Exception:

        print(
            "Warning: Could not save calculator history."
        )


# ============================================================
# CLOCK
# ============================================================

def clock():

    figlet = Figlet(
        font="big"
    )


    print("")
    print("=" * 60)
    print("                    N E X O S ™")
    print("                       CLOCK")
    print("=" * 60)

    print("")
    print("Press CTRL+C to stop the clock.")
    print("")


    try:

        while True:

            os.system("clear")


            now = datetime.datetime.now()


            current_time = now.strftime(
                "%H:%M:%S"
            )


            current_date = now.strftime(
                "%A, %d %B %Y"
            )


            print("=" * 60)
            print("                    N E X O S ™")
            print("                       CLOCK")
            print("=" * 60)

            print("")

            print(
                figlet.renderText(
                    current_time
                )
            )


            print(
                current_date.center(60)
            )


            print("")
            print(
                "Press CTRL+C to exit".center(60)
            )

            print("=" * 60)


            time.sleep(1)


    except KeyboardInterrupt:

        os.system("clear")

        print(
            "Clock stopped."
        )


# ============================================================
# CREATE ACCOUNT
# ============================================================

def create_account():

    print("")
    print("======================")
    print("    CREATE ACCOUNT")
    print("======================")


    username = input(
        "Username: "
    ).strip()


    if username == "":

        print(
            "Username cannot be empty."
        )

        return


    password = input(
        "Password: "
    )


    if password == "":

        print(
            "Password cannot be empty."
        )

        return


    try:

        with open(
            ACCOUNT_FILE,
            "r"
        ) as file:

            accounts = json.load(file)


    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):

        accounts = {}


    if username in accounts:

        print(
            "That username already exists."
        )

        return


    accounts[username] = password


    with open(
        ACCOUNT_FILE,
        "w"
    ) as file:

        json.dump(
            accounts,
            file,
            indent=4
        )


    print(
        "Account created successfully."
    )


# ============================================================
# LOGIN
# ============================================================

def login():

    print("")
    print("======================")
    print("        LOGIN")
    print("======================")


    username = input(
        "Username: "
    ).strip()


    password = input(
        "Password: "
    )


    try:

        with open(
            ACCOUNT_FILE,
            "r"
        ) as file:

            accounts = json.load(file)


    except FileNotFoundError:

        print(
            "No accounts exist yet."
        )

        return None


    except json.JSONDecodeError:

        print(
            "Account database is corrupted."
        )

        return None


    if (
        username in accounts
        and accounts[username] == password
    ):

        print(
            f"Welcome back, {username}!"
        )

        return username


    print(
        "Username or password is incorrect."
    )

    return None


# ============================================================
# UPDATE LOG
# ============================================================

def update_log():

    print("")
    print("------------------------------")
    print("    U P D A T E     L O G")
    print("------------------------------")


    print("")
    print("Current Version: 1.1.5")

    print("")

    print(
        "Version 1.1.5 - Fixed bugs"
    )

    print(
        "Version 1.1.4 - Added dice"
    )

    print(
        "Version 1.1.3 - Added update log"
    )

    print(
        "Version 1.1.2 - Added accounts feature"
    )

    print(
        "Version 1.1.1 - Added folders"
    )

    print(
        "Version 1.1.0 - Fixed clock bugs"
    )

    print(
        "Version 1.0.9 - Fixed minor bugs"
    )

    print(
        "Version 1.0.8 - Fixed calculator bugs"
    )

    print(
        "Version 1.0.7 - Fixed shutdown command"
    )

    print(
        "Version 1.0.6 - Fixed clear bug and added shutdown"
    )

    print(
        "Version 1.0.5 - Converted clock to ASCII art"
    )

    print(
        "Version 1.0.4 - Fixed clock bugs"
    )

    print(
        "Version 1.0.3 - Added clock"
    )

    print(
        "Version 1.0.2 - Fixed bugs"
    )

    print(
        "Version 1.0.1 - Fixed minor bugs"
    )

    print(
        "Version 1.0.0 - Hello to NexOS!"
    )

    print("")
    print("------------------------------")

# ============================================================
# SETTINGS SYSTEM
# ============================================================

SETTINGS_FILE = "settings.json"


# ============================================================
# DEFAULT SETTINGS
# ============================================================

DEFAULT_SETTINGS = {

    "theme":
    "default",

    "clock_format":
    "24",

    "show_seconds":
    True,

    "show_date":
    True,

    "startup_animation":
    True,

    "startup_tip":
    True,

    "command_history":
    True,

    "max_history":
    100,

    "case_sensitive":
    False,

    "clear_after_apps":
    False,

    "login_required":
    False,

    "startup_delay":
    0.25
}


# ============================================================
# LOAD SETTINGS
# ============================================================

def load_settings():

    try:

        with open(
            SETTINGS_FILE,
            "r"
        ) as file:

            settings_data = json.load(file)

    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):

        settings_data = DEFAULT_SETTINGS.copy()

        save_settings(
            settings_data
        )

        return settings_data


    changed = False


    for key, value in DEFAULT_SETTINGS.items():

        if key not in settings_data:

            settings_data[key] = value

            changed = True


    if changed:

        save_settings(
            settings_data
        )


    return settings_data


# ============================================================
# SAVE SETTINGS
# ============================================================

def save_settings(settings_data):

    try:

        with open(
            SETTINGS_FILE,
            "w"
        ) as file:

            json.dump(
                settings_data,
                file,
                indent=4
            )

        return True


    except Exception as error:

        print(
            f"Warning: Could not save settings: {error}"
        )

        return False


# ============================================================
# SETTINGS MAIN MENU
# ============================================================

def settings(current_user=None):

    settings_data = load_settings()


    while True:

        print("")
        print("=" * 55)
        print("                 N E X O S ™")
        print("                   SETTINGS")
        print("=" * 55)

        print("")
        print("1. Account")
        print("2. Appearance")
        print("3. Clock")
        print("4. Startup")
        print("5. Terminal")
        print("6. System")
        print("7. Security")
        print("8. Data")
        print("9. Reset settings")
        print("10. Exit")

        print("")


        choice = input(
            "Settings> "
        ).strip()


        if choice == "1":

            account_settings(
                current_user
            )


        elif choice == "2":

            appearance_settings(
                settings_data
            )


        elif choice == "3":

            clock_settings(
                settings_data
            )


        elif choice == "4":

            startup_settings(
                settings_data
            )


        elif choice == "5":

            terminal_settings(
                settings_data
            )


        elif choice == "6":

            system_settings(
                settings_data
            )


        elif choice == "7":

            security_settings(
                settings_data
            )


        elif choice == "8":

            data_settings(
                settings_data
            )


        elif choice == "9":

            reset_settings(
                settings_data
            )


            settings_data = load_settings()


        elif choice == "10":

            save_settings(
                settings_data
            )

            print(
                "Leaving Settings..."
            )

            break


        else:

            print(
                "Invalid option."
            )


# ============================================================
# ACCOUNT SETTINGS
# ============================================================

def account_settings(current_user=None):

    while True:

        print("")
        print("=" * 45)
        print("             ACCOUNT SETTINGS")
        print("=" * 45)

        print("")

        if current_user is None:

            print("Current user: Not logged in")

        else:

            print(
                f"Current user: {current_user}"
            )

        print("")

        print("1. Account information")
        print("2. Change username")
        print("3. Change password")
        print("4. Delete account")
        print("5. Exit")

        print("")


        choice = input(
            "Account Settings> "
        ).strip()


        # ----------------------------------------------------
        # ACCOUNT INFORMATION
        # ----------------------------------------------------

        if choice == "1":

            if current_user is None:

                print(
                    "You must be logged in."
                )

                continue


            try:

                with open(
                    ACCOUNT_FILE,
                    "r"
                ) as file:

                    accounts = json.load(file)


            except (
                FileNotFoundError,
                json.JSONDecodeError
            ):

                print(
                    "Account database unavailable."
                )

                continue


            if current_user not in accounts:

                print(
                    "Account no longer exists."
                )

                continue


            print("")
            print("------------------------------")
            print("ACCOUNT INFORMATION")
            print("------------------------------")

            print(
                f"Username: {current_user}"
            )

            print(
                "Password: ********"
            )

            print("------------------------------")


        # ----------------------------------------------------
        # CHANGE USERNAME
        # ----------------------------------------------------

        elif choice == "2":

            if current_user is None:

                print(
                    "You must be logged in."
                )

                continue


            new_username = input(
                "New username: "
            ).strip()


            if new_username == "":

                print(
                    "Username cannot be empty."
                )

                continue


            if new_username == current_user:

                print(
                    "That is already your username."
                )

                continue


            try:

                with open(
                    ACCOUNT_FILE,
                    "r"
                ) as file:

                    accounts = json.load(file)


            except (
                FileNotFoundError,
                json.JSONDecodeError
            ):

                print(
                    "Account database unavailable."
                )

                continue


            if new_username in accounts:

                print(
                    "That username already exists."
                )

                continue


            password = accounts[current_user]


            del accounts[current_user]

            accounts[new_username] = password


            with open(
                ACCOUNT_FILE,
                "w"
            ) as file:

                json.dump(
                    accounts,
                    file,
                    indent=4
                )


            print(
                "Username changed successfully."
            )

            print(
                "You will need to log in again."
            )

            break


        # ----------------------------------------------------
        # CHANGE PASSWORD
        # ----------------------------------------------------

        elif choice == "3":

            if current_user is None:

                print(
                    "You must be logged in."
                )

                continue


            try:

                with open(
                    ACCOUNT_FILE,
                    "r"
                ) as file:

                    accounts = json.load(file)


            except (
                FileNotFoundError,
                json.JSONDecodeError
            ):

                print(
                    "Account database unavailable."
                )

                continue


            if current_user not in accounts:

                print(
                    "Account not found."
                )

                continue


            old_password = input(
                "Current password: "
            )


            if accounts[current_user] != old_password:

                print(
                    "Incorrect password."
                )

                continue


            new_password = input(
                "New password: "
            )


            if new_password == "":

                print(
                    "Password cannot be empty."
                )

                continue


            confirm_password = input(
                "Confirm new password: "
            )


            if new_password != confirm_password:

                print(
                    "Passwords do not match."
                )

                continue


            accounts[current_user] = new_password


            with open(
                ACCOUNT_FILE,
                "w"
            ) as file:

                json.dump(
                    accounts,
                    file,
                    indent=4
                )


            print(
                "Password changed successfully."
            )


        # ----------------------------------------------------
        # DELETE ACCOUNT
        # ----------------------------------------------------

        elif choice == "4":

            if current_user is None:

                print(
                    "You must be logged in."
                )

                continue


            confirm = input(
                "Delete this account permanently? (y/n): "
            ).lower().strip()


            if confirm != "y":

                print(
                    "Account deletion cancelled."
                )

                continue


            password = input(
                "Enter your password: "
            )


            try:

                with open(
                    ACCOUNT_FILE,
                    "r"
                ) as file:

                    accounts = json.load(file)


            except (
                FileNotFoundError,
                json.JSONDecodeError
            ):

                print(
                    "Account database unavailable."
                )

                continue


            if (
                current_user not in accounts
                or accounts[current_user] != password
            ):

                print(
                    "Incorrect password."
                )

                continue


            del accounts[current_user]


            with open(
                ACCOUNT_FILE,
                "w"
            ) as file:

                json.dump(
                    accounts,
                    file,
                    indent=4
                )


            print(
                "Account deleted."
            )

            print(
                "Returning to NexOS..."
            )

            break


        # ----------------------------------------------------
        # EXIT
        # ----------------------------------------------------

        elif choice == "5":

            break


        else:

            print(
                "Invalid option."
            )


# ============================================================
# APPEARANCE SETTINGS
# ============================================================

def appearance_settings(settings_data):

    while True:

        print("")
        print("=" * 45)
        print("            APPEARANCE SETTINGS")
        print("=" * 45)

        print("")

        print(
            f"1. Theme: {settings_data['theme']}"
        )

        print(
            "2. Startup banner: "
            + (
                "ON"
                if settings_data["startup_animation"]
                else "OFF"
            )
        )

        print(
            "3. Startup tip: "
            + (
                "ON"
                if settings_data["startup_tip"]
                else "OFF"
            )
        )

        print("4. Exit")

        print("")


        choice = input(
            "Appearance> "
        ).strip()


        # ----------------------------------------------------
        # THEME
        # ----------------------------------------------------

        if choice == "1":

            print("")
            print("Available themes:")
            print("1. Default")
            print("2. Minimal")
            print("3. Classic")

            theme = input(
                "Theme> "
            ).strip()


            if theme == "1":

                settings_data["theme"] = "default"


            elif theme == "2":

                settings_data["theme"] = "minimal"


            elif theme == "3":

                settings_data["theme"] = "classic"


            else:

                print(
                    "Invalid theme."
                )

                continue


            save_settings(
                settings_data
            )

            print(
                "Theme updated."
            )


        # ----------------------------------------------------
        # STARTUP BANNER
        # ----------------------------------------------------

        elif choice == "2":

            settings_data[
                "startup_animation"
            ] = not settings_data[
                "startup_animation"
            ]


            save_settings(
                settings_data
            )


            print(
                "Startup banner:",
                "ON"
                if settings_data[
                    "startup_animation"
                ]
                else "OFF"
            )


        # ----------------------------------------------------
        # STARTUP TIP
        # ----------------------------------------------------

        elif choice == "3":

            settings_data[
                "startup_tip"
            ] = not settings_data[
                "startup_tip"
            ]


            save_settings(
                settings_data
            )


            print(
                "Startup tip:",
                "ON"
                if settings_data[
                    "startup_tip"
                ]
                else "OFF"
            )


        elif choice == "4":

            break


        else:

            print(
                "Invalid option."
            )


# ============================================================
# CLOCK SETTINGS
# ============================================================

def clock_settings(settings_data):

    while True:

        print("")
        print("=" * 45)
        print("              CLOCK SETTINGS")
        print("=" * 45)

        print("")

        print(
            f"1. Time format: "
            f"{settings_data['clock_format']}-hour"
        )

        print(
            "2. Show seconds: "
            + (
                "ON"
                if settings_data["show_seconds"]
                else "OFF"
            )
        )

        print(
            "3. Show date: "
            + (
                "ON"
                if settings_data["show_date"]
                else "OFF"
            )
        )

        print("4. Exit")

        print("")


        choice = input(
            "Clock Settings> "
        ).strip()


        if choice == "1":

            print("")
            print("1. 12-hour")
            print("2. 24-hour")

            option = input(
                "Format> "
            ).strip()


            if option == "1":

                settings_data[
                    "clock_format"
                ] = "12"


            elif option == "2":

                settings_data[
                    "clock_format"
                ] = "24"


            else:

                print(
                    "Invalid option."
                )

                continue


            save_settings(
                settings_data
            )

            print(
                "Clock format updated."
            )


        elif choice == "2":

            settings_data[
                "show_seconds"
            ] = not settings_data[
                "show_seconds"
            ]


            save_settings(
                settings_data
            )


            print(
                "Show seconds:",
                "ON"
                if settings_data[
                    "show_seconds"
                ]
                else "OFF"
            )


        elif choice == "3":

            settings_data[
                "show_date"
            ] = not settings_data[
                "show_date"
            ]


            save_settings(
                settings_data
            )


            print(
                "Show date:",
                "ON"
                if settings_data[
                    "show_date"
                ]
                else "OFF"
            )


        elif choice == "4":

            break


        else:

            print(
                "Invalid option."
            )


# ============================================================
# STARTUP SETTINGS
# ============================================================

def startup_settings(settings_data):

    while True:

        print("")
        print("=" * 45)
        print("             STARTUP SETTINGS")
        print("=" * 45)

        print("")

        print(
            "1. Startup animation: "
            + (
                "ON"
                if settings_data["startup_animation"]
                else "OFF"
            )
        )

        print(
            "2. Startup tip: "
            + (
                "ON"
                if settings_data["startup_tip"]
                else "OFF"
            )
        )

        print(
            f"3. Startup delay: "
            f"{settings_data['startup_delay']} seconds"
        )

        print("4. Exit")

        print("")


        choice = input(
            "Startup Settings> "
        ).strip()


        if choice == "1":

            settings_data[
                "startup_animation"
            ] = not settings_data[
                "startup_animation"
            ]


            save_settings(
                settings_data
            )


        elif choice == "2":

            settings_data[
                "startup_tip"
            ] = not settings_data[
                "startup_tip"
            ]


            save_settings(
                settings_data
            )


        elif choice == "3":

            try:

                delay = float(
                    input(
                        "Startup delay in seconds: "
                    )
                )


                if delay < 0:

                    print(
                        "Delay cannot be negative."
                    )

                    continue


                if delay > 10:

                    print(
                        "Maximum delay is 10 seconds."
                    )

                    continue


                settings_data[
                    "startup_delay"
                ] = delay


                save_settings(
                    settings_data
                )


                print(
                    "Startup delay updated."
                )


            except ValueError:

                print(
                    "Please enter a number."
                )


        elif choice == "4":

            break


        else:

            print(
                "Invalid option."
            )


# ============================================================
# TERMINAL SETTINGS
# ============================================================

def terminal_settings(settings_data):

    while True:

        print("")
        print("=" * 45)
        print("             TERMINAL SETTINGS")
        print("=" * 45)

        print("")

        print(
            "1. Command history: "
            + (
                "ON"
                if settings_data["command_history"]
                else "OFF"
            )
        )

        print(
            f"2. Maximum history: "
            f"{settings_data['max_history']}"
        )

        print(
            "3. Case sensitive: "
            + (
                "ON"
                if settings_data["case_sensitive"]
                else "OFF"
            )
        )

        print(
            "4. Clear after applications: "
            + (
                "ON"
                if settings_data["clear_after_apps"]
                else "OFF"
            )
        )

        print("5. Exit")

        print("")


        choice = input(
            "Terminal Settings> "
        ).strip()


        if choice == "1":

            settings_data[
                "command_history"
            ] = not settings_data[
                "command_history"
            ]


            save_settings(
                settings_data
            )


        elif choice == "2":

            try:

                maximum = int(
                    input(
                        "Maximum history entries: "
                    )
                )


                if maximum < 1:

                    print(
                        "Value must be at least 1."
                    )

                    continue


                if maximum > 10000:

                    print(
                        "Maximum allowed value is 10000."
                    )

                    continue


                settings_data[
                    "max_history"
                ] = maximum


                save_settings(
                    settings_data
                )


                print(
                    "Maximum history updated."
                )


            except ValueError:

                print(
                    "Please enter a whole number."
                )


        elif choice == "3":

            settings_data[
                "case_sensitive"
            ] = not settings_data[
                "case_sensitive"
            ]


            save_settings(
                settings_data
            )


        elif choice == "4":

            settings_data[
                "clear_after_apps"
            ] = not settings_data[
                "clear_after_apps"
            ]


            save_settings(
                settings_data
            )


        elif choice == "5":

            break


        else:

            print(
                "Invalid option."
            )


# ============================================================
# SYSTEM SETTINGS
# ============================================================

def system_settings(settings_data):

    while True:

        print("")
        print("=" * 50)
        print("               SYSTEM INFORMATION")
        print("=" * 50)

        print("")

        print(
            f"NexOS version : {VERSION}"
        )

        print(
            f"Python        : {os.sys.version.split()[0]}"
        )

        print(
            f"Platform      : {os.name}"
        )

        print(
            f"Settings file : {SETTINGS_FILE}"
        )

        print(
            f"Account file  : {ACCOUNT_FILE}"
        )

        print(
            f"Notes file    : {NOTES_FILE}"
        )

        print(
            f"Calculator    : {CALCULATOR_FILE}"
        )

        print(
            f"Stopwatch     : {STOPWATCH_FILE}"
        )

        print("")

        print("1. Show settings file")
        print("2. Check data files")
        print("3. Exit")

        print("")


        choice = input(
            "System Settings> "
        ).strip()


        if choice == "1":

            print("")
            print(
                json.dumps(
                    settings_data,
                    indent=4
                )
            )


        elif choice == "2":

            files = [
                ACCOUNT_FILE,
                NOTES_FILE,
                CALCULATOR_FILE,
                STOPWATCH_FILE,
                SETTINGS_FILE
            ]


            print("")

            for filename in files:

                if os.path.exists(filename):

                    print(
                        f"[✓] {filename}"
                    )

                else:

                    print(
                        f"[ ] {filename}"
                    )


        elif choice == "3":

            break


        else:

            print(
                "Invalid option."
            )


# ============================================================
# SECURITY SETTINGS
# ============================================================

def security_settings(settings_data):

    while True:

        print("")
        print("=" * 45)
        print("             SECURITY SETTINGS")
        print("=" * 45)

        print("")

        print(
            "1. Login required: "
            + (
                "ON"
                if settings_data["login_required"]
                else "OFF"
            )
        )

        print("2. Exit")

        print("")


        choice = input(
            "Security Settings> "
        ).strip()


        if choice == "1":

            settings_data[
                "login_required"
            ] = not settings_data[
                "login_required"
            ]


            save_settings(
                settings_data
            )


            print(
                "Login required:",
                "ON"
                if settings_data[
                    "login_required"
                ]
                else "OFF"
            )


        elif choice == "2":

            break


        else:

            print(
                "Invalid option."
            )


# ============================================================
# DATA SETTINGS
# ============================================================

def data_settings(settings_data):

    while True:

        print("")
        print("=" * 45)
        print("                DATA SETTINGS")
        print("=" * 45)

        print("")

        print("1. Clear calculator history")
        print("2. Clear stopwatch history")
        print("3. Clear notes")
        print("4. Clear settings")
        print("5. Exit")

        print("")


        choice = input(
            "Data Settings> "
        ).strip()


        # ----------------------------------------------------
        # CALCULATOR
        # ----------------------------------------------------

        if choice == "1":

            confirm = input(
                "Delete calculator history? (y/n): "
            ).lower().strip()


            if confirm == "y":

                try:

                    with open(
                        CALCULATOR_FILE,
                        "w"
                    ) as file:

                        json.dump(
                            {
                                "history": []
                            },
                            file,
                            indent=4
                        )


                    print(
                        "Calculator history cleared."
                    )


                except Exception:

                    print(
                        "Could not clear calculator history."
                    )


        # ----------------------------------------------------
        # STOPWATCH
        # ----------------------------------------------------

        elif choice == "2":

            confirm = input(
                "Delete stopwatch history? (y/n): "
            ).lower().strip()


            if confirm == "y":

                try:

                    with open(
                        STOPWATCH_FILE,
                        "w"
                    ) as file:

                        json.dump(
                            {
                                "sessions": []
                            },
                            file,
                            indent=4
                        )


                    print(
                        "Stopwatch history cleared."
                    )


                except Exception:

                    print(
                        "Could not clear stopwatch history."
                    )


        # ----------------------------------------------------
        # NOTES
        # ----------------------------------------------------

        elif choice == "3":

            confirm = input(
                "Delete ALL notes? (y/n): "
            ).lower().strip()


            if confirm == "y":

                try:

                    with open(
                        NOTES_FILE,
                        "w"
                    ) as file:

                        json.dump(
                            {
                                "users": {}
                            },
                            file,
                            indent=4
                        )


                    print(
                        "All notes cleared."
                    )


                except Exception:

                    print(
                        "Could not clear notes."
                    )


        # ----------------------------------------------------
        # SETTINGS
        # ----------------------------------------------------

        elif choice == "4":

            confirm = input(
                "Delete settings file? (y/n): "
            ).lower().strip()


            if confirm == "y":

                try:

                    if os.path.exists(
                        SETTINGS_FILE
                    ):

                        os.remove(
                            SETTINGS_FILE
                        )


                    print(
                        "Settings cleared."
                    )


                except Exception:

                    print(
                        "Could not clear settings."
                    )


        # ----------------------------------------------------
        # EXIT
        # ----------------------------------------------------

        elif choice == "5":

            break


        else:

            print(
                "Invalid option."
            )


# ============================================================
# RESET SETTINGS
# ============================================================

def reset_settings(settings_data):

    while True:

        print("")
        print("=" * 50)
        print("               RESET SETTINGS")
        print("=" * 50)

        print("")

        print("1. Reset appearance")
        print("2. Reset clock")
        print("3. Reset startup")
        print("4. Reset terminal")
        print("5. Reset security")
        print("6. Reset EVERYTHING")
        print("7. Cancel")

        print("")


        choice = input(
            "Reset> "
        ).strip()


        # ----------------------------------------------------
        # APPEARANCE
        # ----------------------------------------------------

        if choice == "1":

            settings_data[
                "theme"
            ] = DEFAULT_SETTINGS[
                "theme"
            ]


            save_settings(
                settings_data
            )


            print(
                "Appearance settings reset."
            )


        # ----------------------------------------------------
        # CLOCK
        # ----------------------------------------------------

        elif choice == "2":

            settings_data[
                "clock_format"
            ] = DEFAULT_SETTINGS[
                "clock_format"
            ]

            settings_data[
                "show_seconds"
            ] = DEFAULT_SETTINGS[
                "show_seconds"
            ]

            settings_data[
                "show_date"
            ] = DEFAULT_SETTINGS[
                "show_date"
            ]


            save_settings(
                settings_data
            )


            print(
                "Clock settings reset."
            )


        # ----------------------------------------------------
        # STARTUP
        # ----------------------------------------------------

        elif choice == "3":

            settings_data[
                "startup_animation"
            ] = DEFAULT_SETTINGS[
                "startup_animation"
            ]

            settings_data[
                "startup_tip"
            ] = DEFAULT_SETTINGS[
                "startup_tip"
            ]

            settings_data[
                "startup_delay"
            ] = DEFAULT_SETTINGS[
                "startup_delay"
            ]


            save_settings(
                settings_data
            )


            print(
                "Startup settings reset."
            )


        # ----------------------------------------------------
        # TERMINAL
        # ----------------------------------------------------

        elif choice == "4":

            settings_data[
                "command_history"
            ] = DEFAULT_SETTINGS[
                "command_history"
            ]

            settings_data[
                "max_history"
            ] = DEFAULT_SETTINGS[
                "max_history"
            ]

            settings_data[
                "case_sensitive"
            ] = DEFAULT_SETTINGS[
                "case_sensitive"
            ]

            settings_data[
                "clear_after_apps"
            ] = DEFAULT_SETTINGS[
                "clear_after_apps"
            ]


            save_settings(
                settings_data
            )


            print(
                "Terminal settings reset."
            )


        # ----------------------------------------------------
        # SECURITY
        # ----------------------------------------------------

        elif choice == "5":

            settings_data[
                "login_required"
            ] = DEFAULT_SETTINGS[
                "login_required"
            ]


            save_settings(
                settings_data
            )


            print(
                "Security settings reset."
            )


        # ----------------------------------------------------
        # EVERYTHING
        # ----------------------------------------------------

        elif choice == "6":

            confirm = input(
                "Reset ALL NexOS settings? (y/n): "
            ).lower().strip()


            if confirm == "y":

                new_settings = (
                    DEFAULT_SETTINGS.copy()
                )


                settings_data.clear()

                settings_data.update(
                    new_settings
                )


                save_settings(
                    settings_data
                )


                print(
                    "All settings have been reset."
                )


                break


            else:

                print(
                    "Reset cancelled."
                )


        # ----------------------------------------------------
        # CANCEL
        # ----------------------------------------------------

        elif choice == "7":

            print(
                "Reset cancelled."
            )

            break


        else:

            print(
                "Invalid option."
            )


# ============================================================
# START NEXOS
# ============================================================

startup()

terminal()
