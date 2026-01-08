#Go to windows --> Edit the system enviroment variables --> Click enviroment Variables --> create new variable in USER Variables (Not in system variables) -->
# -->Variable name = OPENAI_API_KEY --> API Key = paste the key ur given or created --> Click ok --> restart vscode

import os

def get_openai_api_key() -> str:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. "
            "Set it in your environment variables and restart your terminal/IDE."
        )
    return key
