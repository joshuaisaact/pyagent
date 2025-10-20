from functions.get_files_info import get_files_info

def test_get_files_current_directory():
    result = get_files_info("calculator", ".")
    assert "main.py" in result
    assert "tests.py" in result
    assert "pkg" in result
    assert "file_size" in result
    assert "bytes" in result
    assert "is_dir=" in result

def test_get_files_pkg_directory():
    result = get_files_info("calculator", "pkg")
    assert "calculator.py" in result
    assert "render.py" in result
    assert "file_size" in result
    assert "bytes" in result
    assert "is_dir=" in result

def test_get_files_outside_bin():
    result = get_files_info("calculator", "/bin")
    assert "Error:" in result
    assert '/bin' in result

def test_get_files_outside_parent():
    result = get_files_info("calculator", "../")
    assert "Error:" in result
    assert "outside the permitted working directory" in result

if __name__ == "__main__":
    # Print outputs for the grader
    print(get_files_info("calculator", "."))
    print(get_files_info("calculator", "pkg"))
    print(get_files_info("calculator", "/bin"))
    print(get_files_info("calculator", "../"))

    # Run pytest for your own verification
    import pytest
    pytest.main([__file__, "-v"])