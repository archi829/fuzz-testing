from hypothesis import given, strategies as st
from processor import sanitize_string, parse_int_list, reverse_words

strategy = st.text() | st.none()

@given(strategy)
def test_sanitize_string_no_crash(s):
    try:
        sanitize_string(s)
    except Exception as e:
        assert False, f"sanitize_string crashed with input: {s} : {e}"
    
@given(strategy)
def test_parse_int_list_safe(s):
    try:
        parse_int_list(s)
    except Exception as e:
        assert False, f"parse_int_list crashed with input: {s} : {e}"

@given(strategy)
def test_reverse_words_safe(s):
    try:
        reverse_words(s)
    except Exception as e:
        assert False, f"reverse_words crashed with input: {s} : {e}"