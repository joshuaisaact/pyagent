from functions.get_files_info import get_files_info

def test_get_files_current_directory():
    result = get_files_info(".", ".")
    assert "main.py" in result
    assert "config.py" in result
    assert "functions" in result
    assert "file_size" in result
    assert "bytes" in result
    assert "is_dir=" in result

def test_get_files_functions_directory():
    result = get_files_info(".", "functions")
    assert "get_files_info.py" in result
    assert "get_file_content.py" in result
    assert "file_size" in result
    assert "bytes" in result
    assert "is_dir=" in result

def test_get_files_outside_bin():
    result = get_files_info(".", "/bin")
    assert "Error:" in result
    assert '/bin' in result

def test_get_files_outside_parent():
    result = get_files_info(".", "../")
    assert "Error:" in result
    assert "outside the permitted working directory" in result

if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])