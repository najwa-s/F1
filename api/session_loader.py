import fastf1
from fastf1.core import Session

def load_session(year:int, gp:str, session_type:str) -> Session:
    """
        Load a session (example : Q FOR Qualifying, R for Race).

    """
    fastf1.Cache.enable_cache('data/raw')
    session = fastf1.get_session(year,gp,session_type)
    session.load()
    return session