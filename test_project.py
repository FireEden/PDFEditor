import pytest


from project import get_file, save_file_name_check

def test_get_file(monkeypatch):
    #test invalid file names
    monkeypatch.setattr('builtins.input', lambda _: "test4.pdf")
    with pytest.raises(SystemExit):
        get_file()
    monkeypatch.setattr('builtins.input', lambda _: "tes@t2.pdf")
    with pytest.raises(SystemExit):
        get_file()
    monkeypatch.setattr('builtins.input', lambda _: "test2.docx")
    with pytest.raises(SystemExit):
        get_file()

def test_get_file_valid(monkeypatch):
    #test valid file names
    test_file = "PDF Sample.pdf"
    monkeypatch.setattr('builtins.input', lambda _: test_file)
    assert get_file()[1] == 5
    #assert(type(get_file()).__name__ == "Document")


def test_save_file_name_check(monkeypatch):
    #test invalid save file names
    monkeypatch.setattr('builtins.input', lambda _: "saved.test")
    assert save_file_name_check() == "Error"
    monkeypatch.setattr('builtins.input', lambda _: "s@@ved.pdf")
    assert save_file_name_check() == "Error"
    monkeypatch.setattr('builtins.input', lambda _: "savedpdf")
    assert save_file_name_check() == "Error"


def test_save_file_name_check_valid(monkeypatch):
    #test invalid save file names
    monkeypatch.setattr('builtins.input', lambda _: "saved2.pdf")
    assert save_file_name_check() == "saved2.pdf"
    monkeypatch.setattr('builtins.input', lambda _: "new saved file 2.pdf")
    assert save_file_name_check() == "new saved file 2.pdf"

