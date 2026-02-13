from src.parsing.resume_parser import parse_resume
from src.parsing.jd_parser import parse_jd
from io import BytesIO

def test_parse_resume_txt():
    sample_text = "Python developer with 3 years experience"
    file = BytesIO(sample_text.encode("utf-8"))
    file.name = "sample_resume.txt"
    file.type = "text/plain"
    
    text = parse_resume(file)
    assert "python developer" in text

def test_parse_jd_txt():
    sample_text = "Looking for a Python developer"
    file = BytesIO(sample_text.encode("utf-8"))
    file.name = "sample_jd.txt"
    file.type = "text/plain"
    
    text = parse_jd(file)
    assert "python developer" in text
