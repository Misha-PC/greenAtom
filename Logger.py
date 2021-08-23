from datetime import datetime
from config import cfg_path, log_


def log(source, message, file_path=cfg_path):
    if not log_:
        return
    with open(file_path, "a") as file:
        s = f"{datetime.now()} [{source}]: {message}."
        print(f"Log: {s}")
        file.write("\n" + s)
