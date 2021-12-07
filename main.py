from app import app, db
from app.models import User, Task

@app.shell_context_processor
def create_shell_context():
    """
    A function that registers listed items in the shell context
    """
    return{'db':db, 'User':User, 'Task':Task}