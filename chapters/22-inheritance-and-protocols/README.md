# Chapter 22: Inheritance and Protocols: Pluggable Importers

How do you let different kinds of importers plug into the same program? Think of a wall socket: any appliance with the right plug works. In this chapter we write a base Importer class, then CsvImporter and JsonImporter subclasses that inherit from it and override parse, call super().__init__, use them in one loop (polymorphism), make the base class abstract with ABC and abstractmethod and see the real TypeError, and finish with duck typing and typing.Protocol. The result is a pluggable importer family for Pocket Ledger.

## Files

- `importers.py`

## Run it

From this folder:

```bash
uv run importers.py
```


## Practice

Try these on your own copy of the files:

1. Write a `TsvImporter` that reads tab-separated text.
2. Make the base class abstract and try to create it.
3. Write a function that accepts anything with a `parse` method.

Tested with Python 3.15.1 and uv 0.13.5.
