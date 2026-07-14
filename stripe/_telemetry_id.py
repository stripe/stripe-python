import os
import secrets
from pathlib import Path
from typing import Optional

_cached_id: Optional[str] = None
_loaded: bool = False


def get_config_dir() -> Optional[Path]:
    if os.name == "nt":
        if appdata := os.environ.get("APPDATA"):
            return Path(appdata) / "Stripe"
        # APPDATA is set system wide, so it would be very unusual to hit this
        return None
    if xdg := os.environ.get("XDG_CONFIG_HOME"):
        return Path(xdg) / "stripe"
    return Path.home() / ".config" / "stripe"


def get_telemetry_id() -> Optional[str]:
    global _cached_id, _loaded
    if _loaded:
        return _cached_id

    try:
        if (config_dir := get_config_dir()) is None:
            return None

        file_path = config_dir / "telemetry_id"

        try:
            if content := file_path.read_text().strip():
                _cached_id = content
                return _cached_id
        except OSError:
            pass

        new_id = secrets.token_hex(16)

        try:
            config_dir.mkdir(parents=True, exist_ok=True)
            file_path.write_text(new_id)
        except OSError:
            return None

        _cached_id = new_id
        return _cached_id
    finally:
        _loaded = True
