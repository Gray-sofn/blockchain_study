import hashlib
import collections


# hashとは、データを一定の長さの文字列にしたもの
# sha256は256bitを表し、encode()でバイトデータに変換
# バイトデータ:b'test' [(t=)116, (e=)101, (s=)115, (t=)117]
# jexdigest():16進数の64文字で表現
# print(hashlib.sha256('test'.encode()).hexdigest())
# print(hashlib.sha256('test'.encode()).hexdigest())
# print(hashlib.sha256('test2'.encode()).hexdigest())
# print(hashlib.sha256('test2'.encode()).hexdigest())

# block = {'b': 2, 'a': 1}
# block2 = {'a': 1, 'b': 2}

# block = collections.OrderedDict(sorted(block.items(), key=lambda d:d[0]))
# block2 = collections.OrderedDict(sorted(block2.items(), key=lambda d:d[0]))

# print(hashlib.sha256(str(block).encode()).hexdigest())
# print(hashlib.sha256(str(block2).encode()).hexdigest())

def sorted_dict_by_key(unsorted_dict):
  return collections.OrderedDict(sorted(unsorted_dict.items(), key=lambda d:d[0]))

def pprint(chains):
  for i, chain in enumerate(chains):
    print(f'{"="*25} Chain {i} {"="*25}')
    for k, v in chain.items():
      if k == 'transactions':
        print(k)
        for d in v:
          print(f'{"-"*40}')
          for kk, vv in d.items():
            print(f'{kk:30}{vv}')
      else:
        print(f'{k:15}{v}')
  print(f'{"*"*25}')