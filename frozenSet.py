fs = frozenset({1,2,3})
print(fs)
fs.add(4)  # This will raise an AttributeError because frozenset is immutable

print(fs)