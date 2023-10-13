#include <Python.h>

/**
 * print_python_bytes - prints information about Python bytes objects
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size, i;
    char *string;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    printf("  first 10 bytes:");
    for (i = 0; i < size && i < 10; i++)
        printf(" %02x", (unsigned char)string[i]);
    printf("\n");
}

/**
 * print_python_list - prints information about Python lists
 * @p: pointer to PyObject
 */
void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size, allocated, i;
    PyObject *item;

    printf("[*] Python list info\n");

    size = PyList_Size(p);
    allocated = list->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);

        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}
