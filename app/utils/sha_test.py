from utils.sha import *
from hashlib import sha1

def test_hash():
    assert hash(b'Celine') == sha1(b'Celine').hexdigest()
    assert hash(b'SLQJKHDKJSHdklqD') == sha1(b'SLQJKHDKJSHdklqD').hexdigest()
    assert hash(b'QslkJQLS') == sha1(b'QslkJQLS').hexdigest()
    assert hash(b'mOtDePaSSeEtReSEcURISE') == sha1(b'mOtDePaSSeEtReSEcURISE').hexdigest()
    assert hash(b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa') == sha1(b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').hexdigest()

def test_verif():
    hash = generate_password_hash('pASwOrd')
    assert check_password_hash(hash, 'pASwOrd')
    hash = generate_password_hash('SLQJKHDKJSHdklqD')
    assert check_password_hash(hash, 'SLQJKHDKJSHdklqD')
    hash = generate_password_hash('QslkJQLS')
    assert check_password_hash(hash, 'QslkJQLS')
    hash = generate_password_hash('mOtDePaSSeEtReSEcURISE')
    assert check_password_hash(hash, 'mOtDePaSSeEtReSEcURISE')