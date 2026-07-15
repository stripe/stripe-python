import os
import re

import pytest

import stripe._telemetry_id as telemetry_mod
from stripe._telemetry_id import get_config_dir, get_telemetry_id


@pytest.fixture(autouse=True)
def reset_telemetry_cache():
    """Reset the module-level cache before every test so each test starts fresh."""
    telemetry_mod._cached_id = None
    telemetry_mod._loaded = False
    yield
    telemetry_mod._cached_id = None
    telemetry_mod._loaded = False


class TestGetConfigDir:
    def test_xdg_config_home_respected(self, monkeypatch, tmp_path):
        monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))
        monkeypatch.delenv("APPDATA", raising=False)
        # Simulate non-Windows so XDG branch is taken
        monkeypatch.setattr(os, "name", "posix")

        result = get_config_dir()

        assert result == tmp_path / "stripe"

    def test_falls_back_to_home_config_stripe(self, monkeypatch, tmp_path):
        monkeypatch.delenv("XDG_CONFIG_HOME", raising=False)
        monkeypatch.delenv("APPDATA", raising=False)
        monkeypatch.setattr(os, "name", "posix")

        result = get_config_dir()

        assert result is not None
        # Should end with .config/stripe regardless of where $HOME is
        assert result.parts[-1] == "stripe"
        assert result.parts[-2] == ".config"


class TestGetTelemetryId:
    def test_returns_32_char_hex_string(self, monkeypatch, tmp_path):
        monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))
        monkeypatch.setattr(os, "name", "posix")

        result = get_telemetry_id()

        assert result is not None
        assert len(result) == 32
        assert re.fullmatch(r"[0-9a-f]{32}", result)

    def test_is_deterministic_after_first_call(self, monkeypatch, tmp_path):
        monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))
        monkeypatch.setattr(os, "name", "posix")

        first = get_telemetry_id()
        second = get_telemetry_id()

        assert first == second

    def test_reads_existing_id_from_file(self, monkeypatch, tmp_path):
        existing_id = "a" * 32
        config_dir = tmp_path / "stripe"
        config_dir.mkdir(parents=True)
        (config_dir / "telemetry_id").write_text(existing_id)

        monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))
        monkeypatch.setattr(os, "name", "posix")

        result = get_telemetry_id()

        assert result == existing_id

    def test_generates_and_persists_new_id_when_file_absent(
        self, monkeypatch, tmp_path
    ):
        monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))
        monkeypatch.setattr(os, "name", "posix")

        result = get_telemetry_id()

        assert result is not None
        persisted = (tmp_path / "stripe" / "telemetry_id").read_text()
        assert persisted == result

    def test_returns_none_when_write_fails(self, monkeypatch, tmp_path):
        # Make the config dir a file so mkdir fails and write can't succeed
        config_dir = tmp_path / "stripe"
        config_dir.write_text("not a directory")

        monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))
        monkeypatch.setattr(os, "name", "posix")

        result = get_telemetry_id()

        assert result is None

    def test_creates_parent_directories_if_missing(
        self, monkeypatch, tmp_path
    ):
        # tmp_path exists but the nested stripe subdir does not
        monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))
        monkeypatch.setattr(os, "name", "posix")

        assert not (tmp_path / "stripe").exists()

        result = get_telemetry_id()

        assert result is not None
        assert (tmp_path / "stripe").is_dir()
        assert (tmp_path / "stripe" / "telemetry_id").exists()
