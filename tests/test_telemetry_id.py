import re
import sys

import pytest

import stripe._telemetry_id as telemetry_mod
from stripe._telemetry_id import get_config_dir, get_telemetry_id

is_windows = sys.platform == "win32"


@pytest.fixture(autouse=True)
def reset_telemetry_cache():
    """Reset the module-level cache before every test so each test starts fresh."""
    telemetry_mod._cached_id = None
    telemetry_mod._loaded = False
    yield
    telemetry_mod._cached_id = None
    telemetry_mod._loaded = False


@pytest.fixture()
def config_home(monkeypatch, tmp_path):
    """Point the config dir at tmp_path using the platform-appropriate env var."""
    if is_windows:
        monkeypatch.setenv("APPDATA", str(tmp_path))
    else:
        monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))
    return tmp_path


# The subdirectory name differs by platform
stripe_subdir = "Stripe" if is_windows else "stripe"


class TestGetConfigDir:
    @pytest.mark.skipif(is_windows, reason="XDG not used on Windows")
    def test_xdg_config_home_respected(self, monkeypatch, tmp_path):
        monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))

        result = get_config_dir()

        assert result == tmp_path / "stripe"

    @pytest.mark.skipif(is_windows, reason="XDG fallback not used on Windows")
    def test_falls_back_to_home_config_stripe(self, monkeypatch):
        monkeypatch.delenv("XDG_CONFIG_HOME", raising=False)

        result = get_config_dir()

        assert result is not None
        assert result.parts[-1] == "stripe"
        assert result.parts[-2] == ".config"

    @pytest.mark.skipif(not is_windows, reason="APPDATA only used on Windows")
    def test_uses_appdata_on_windows(self, monkeypatch, tmp_path):
        monkeypatch.setenv("APPDATA", str(tmp_path))

        result = get_config_dir()

        assert result == tmp_path / "Stripe"


class TestGetTelemetryId:
    def test_returns_32_char_hex_string(self, config_home):
        result = get_telemetry_id()

        assert result is not None
        assert len(result) == 32
        assert re.fullmatch(r"[0-9a-f]{32}", result)

    def test_is_deterministic_after_first_call(self, config_home):
        first = get_telemetry_id()
        second = get_telemetry_id()

        assert first == second

    def test_reads_existing_id_from_file(self, config_home):
        existing_id = "a" * 32
        config_dir = config_home / stripe_subdir
        config_dir.mkdir(parents=True)
        (config_dir / "telemetry_id").write_text(existing_id)

        result = get_telemetry_id()

        assert result == existing_id

    def test_generates_and_persists_new_id_when_file_absent(self, config_home):
        result = get_telemetry_id()

        assert result is not None
        persisted = (config_home / stripe_subdir / "telemetry_id").read_text()
        assert persisted == result

    def test_returns_none_when_write_fails(self, config_home):
        # Make the config dir a file so mkdir fails and write can't succeed
        config_dir = config_home / stripe_subdir
        config_dir.write_text("not a directory")

        result = get_telemetry_id()

        assert result is None

    def test_creates_parent_directories_if_missing(self, config_home):
        assert not (config_home / stripe_subdir).exists()

        result = get_telemetry_id()

        assert result is not None
        assert (config_home / stripe_subdir).is_dir()
        assert (config_home / stripe_subdir / "telemetry_id").exists()
