 __import__(name[,globals[,locals[,fromlist[,level]]]])¶

    Note

    This is an advanced function that is not needed in everyday Python
    programming, unlike importlib.import_module().

    This function is invoked by the import statement. It can be replaced (by
    importing the __builtin__ module and assigning to __builtin__.__import__) in
    order to change semantics of the import statement, but nowadays it is
    usually simpler to use import hooks (see PEP 302). Direct use of
    __import__() is rare, except in cases where you want to import a module
    whose name is only known at runtime.

    The function imports the module name, potentially using the given globals
    and locals to determine how to interpret the name in a package context. The
    fromlist gives the names of objects or submodules that should be imported
    from the module given by name. The standard implementation does not use its
    locals argument at all, and uses its globals only to determine the package
    context of the import statement.

    level specifies whether to use absolute or relative imports. The default is
    -1 which indicates both absolute and relative imports will be attempted. 0
    means only perform absolute imports. Positive values for level indicate the
    number of parent directories to search relative to the directory of the
    module calling __import__().

    When the name variable is of the form package.module, normally, the top-
    level package (the name up till the first dot) is returned, not the module
    named by name. However, when a non-empty fromlist argument is given, the
    module named by name is returned.
