from functions.get_file_content import get_file_content

def test_get_file_content_existing_file():
    result = get_file_content(".", "config.py")
    assert "WORKING_DIR" in result or "MAX_CHARS" in result
    assert "Error:" not in result

def test_get_file_content_nonexistent_file():
    result = get_file_content(".", "nonexistent_file.txt")
    assert "Error:" in result
    assert "File not found" in result

def test_get_file_content_outside_working_directory():
    result = get_file_content(".", "/etc/passwd")
    assert "Error:" in result
    assert "outside the permitted working directory" in result

def test_get_file_content_directory_not_file():
    result = get_file_content(".", "functions")
    assert "Error:" in result
    assert "not a regular file" in result


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])