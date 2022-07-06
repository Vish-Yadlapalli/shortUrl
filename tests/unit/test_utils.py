import sys
sys.path.append('/home/viswa/dell_proj/shortUrl')
from core.utils import is_valid_url, generate_short_id

def test_is_valid_url():
    assert is_valid_url('htt://google.com') == False
    assert is_valid_url('') == False
    assert is_valid_url('htps://youtube.com') == False