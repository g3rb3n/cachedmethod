import cachedmethod as cm
import json
import logging
import shutil
import os
]
cm.logger.setLevel(logging.WARN)

cache='./testcache/'

@cm.cached_method(cache)
def fun(d, l):
    return {'d':d,'l':l}

def empty_cache():
    for f in os.listdir(cache):
        os.remove(os.path.join(cache, f))

def cached_files():
    return len(os.listdir(cache))

def test_cachedmethod_equal_call():
    empty_cache()

    d = {
        'key':'bla',
        'z':'bla',
        'a':'bla'
    }
    l = [1,2,3,4]
    ro = fun(d, l)
    cached = cached_files()
    for i in range(0,100):
        rc = fun(d, l)
        assert ro == rc
        assert cached_files() == cached

def test_cachedmethod_other_call():
    empty_cache()
    d = {
        'key':'bla',
        'z':'bla',
        'a':'bla'
    }
    l = [1,2,3,4]
    cached = cached_files()
    for i in range(0,100):
        d['a'] = i
        rc = fun(d, l)
        assert cached_files() == cached + i + 1, 'Number of cached files should increase, expected %s found %s' % (cached + i + 1, cached_files())

def test_cachedmethod_fp():
    empty_cache()
    cached = cached_files()
    fp = fun
    rc = fp({}, [])
    assert cached_files() == cached + 1, 'Number of cached files should increase, expected %s found %s' % (cached + i + 1, cached_files())

@cm.cached_method(cache)
def f(fp):
    return fp({}, [])

def test_cachedmethod_fp_illegal():
    empty_cache()
    cached = cached_files()
    try:
        rc = f(fun)
    except Exception as e:
        return
    raise Exception('cached method should have raised an exception')

if __name__ == '__main__':
    test_cachedmethod_equal_call()
    test_cachedmethod_other_call()
    test_cachedmethod_fp()
    test_cachedmethod_fp_illegal()
