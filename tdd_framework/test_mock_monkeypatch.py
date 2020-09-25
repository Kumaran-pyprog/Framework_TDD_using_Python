import pytest
from unittest.mock import MagicMock
from linereader import readfromFile

def test_canCallReadFromFile():
    readfromFile("blah")

def test_returnCorrectstring(monkeypatch):
    mock_file=MagicMock()
    mock_file.read_line=MagicMock(return_value="test line")
    mock_open=MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    result=readfromFile("blah")
    mock_open.assert_called_once_with("blah","r")
    assert result == "test line"
