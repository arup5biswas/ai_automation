from agent import tools, memory
from logs.logger import log

def run_agent(task: str, payload: str):

    if task == "error":
        result = tools.analyze_error(payload)

    elif task == "code":
        result = tools.review_code(payload)

    else:
        result = "Unknown task."

    memory.save(f"{task}: {payload} -> {result}")
    log(f"{task}: {payload} -> {result}")


    return result
